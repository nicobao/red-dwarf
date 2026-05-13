from enum import Enum
from typing import Generic, Literal, Optional, TypeVar
from dataclasses import dataclass
import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.decomposition import PCA
from reddwarf.types.polis import PolisRepness
from reddwarf.utils.clusterer.base import run_clusterer
from reddwarf.utils.clusterer.kmeans import calculate_kmeans_silhouette_score
from reddwarf.utils.consensus import select_consensus_statements, ConsensusResult
from reddwarf.utils.matrix import (
    generate_raw_matrix,
    simple_filter_matrix,
    get_clusterable_participant_ids,
)
from reddwarf.utils.reducer.base import ReducerType, ReducerModel, run_reducer
from reddwarf.utils.clusterer.base import ClustererType, ClustererModel
from reddwarf.utils.stats import (
    calculate_comment_statistics_dataframes,
    populate_priority_calculations_into_statements_df,
    select_representative_statements,
)


T = TypeVar("T")


class AnalysisOutcome(str, Enum):
    SUCCESS = "success"
    INSUFFICIENT_DATA = "insufficient_data"


class InsufficientDataReason(str, Enum):
    EMPTY_VOTE_MATRIX = "empty_vote_matrix"
    NOT_ENOUGH_CLUSTERABLE_PARTICIPANTS = "not_enough_clusterable_participants"
    NOT_ENOUGH_UNIQUE_POINTS = "not_enough_unique_points"
    NOT_ENOUGH_SAMPLES_FOR_GROUP_COUNT = "not_enough_samples_for_group_count"


@dataclass(frozen=True)
class AnalysisSuccess(Generic[T]):
    outcome: Literal[AnalysisOutcome.SUCCESS]
    result: T


@dataclass(frozen=True)
class AnalysisInsufficientData:
    outcome: Literal[AnalysisOutcome.INSUFFICIENT_DATA]
    reason: InsufficientDataReason


@dataclass
class PcaProjectionResult:
    raw_vote_matrix: DataFrame
    filtered_vote_matrix: DataFrame
    reducer: ReducerModel
    participants_df: DataFrame
    statements_df: DataFrame
    participant_ids_to_cluster: list[int]
    participant_projections: dict
    statement_projections: Optional[dict]


@dataclass
class PolisClusteringResult:
    """
    Attributes:
        raw_vote_matrix (DataFrame): Raw sparse vote matrix before any processing.
        filtered_vote_matrix (DataFrame): Raw sparse vote matrix with moderated statements zero'd out.
        reducer (ReducerModel): scikit-learn reducer model fitted to vote matrix.
        clusterer (ClustererModel): scikit-learn clusterer model, fitted to participant projections. (includes `labels_`)
        group_comment_stats (DataFrame): A multi-index dataframes for each statement, indexed by group ID and statement.
        statements_df (DataFrame): A dataframe with all intermediary and final statement data/calculations/metadata.
        participants_df (DataFrame): A dataframe with all intermediary and final participant data/calculations/metadata.
        participant_projections (dict): A dict of participant projected coordinates, keyed to participant ID.
        statement_projections (Optional[dict]): A dict of statement projected coordinates, keyed to statement ID.
        group_aware_consensus (dict): A nested dict of statement group-aware-consensus values, keyed first by agree/disagree, then participant ID.
        consensus (ConsensusResult): A dict of the most statistically significant statements for each of agree/disagree.
        repness (PolisRepness): A dict of the most statistically significant statements most representative of each group.
    """

    raw_vote_matrix: DataFrame
    filtered_vote_matrix: DataFrame
    reducer: ReducerModel
    # TODO: Figure out how to guarantee PolisKMeans model returned.
    clusterer: ClustererModel | None
    group_comment_stats: DataFrame
    statements_df: DataFrame
    participants_df: DataFrame
    participant_projections: dict
    statement_projections: Optional[dict]
    group_aware_consensus: dict
    consensus: ConsensusResult
    repness: PolisRepness


TypedPolisClusteringResult = (
    AnalysisSuccess[PolisClusteringResult] | AnalysisInsufficientData
)


def get_insufficient_data_reason(
    *,
    votes: list[dict],
    mod_out_statement_ids: list[int] | None = None,
    min_user_vote_threshold: int = 7,
    keep_participant_ids: list[int] | None = None,
    force_group_count: Optional[int] = None,
) -> InsufficientDataReason | None:
    """Return a typed insufficient-data reason, or None when compute can proceed."""
    if len(votes) == 0:
        return InsufficientDataReason.EMPTY_VOTE_MATRIX

    mod_out_statement_ids = mod_out_statement_ids or []
    keep_participant_ids = keep_participant_ids or []
    raw_vote_matrix = generate_raw_matrix(votes=votes)
    filtered_vote_matrix = simple_filter_matrix(
        vote_matrix=raw_vote_matrix,
        mod_out_statement_ids=mod_out_statement_ids,
    )
    participant_ids_to_cluster = get_clusterable_participant_ids(
        raw_vote_matrix,
        vote_threshold=min_user_vote_threshold,
    )
    if keep_participant_ids:
        keep_participant_ids_existing = filtered_vote_matrix.index.intersection(
            keep_participant_ids,
        ).to_list()
        participant_ids_to_cluster = sorted(
            list(set(participant_ids_to_cluster + keep_participant_ids_existing))
        )

    if len(participant_ids_to_cluster) < 2:
        return InsufficientDataReason.NOT_ENOUGH_CLUSTERABLE_PARTICIPANTS
    if force_group_count is not None and len(participant_ids_to_cluster) < force_group_count:
        return InsufficientDataReason.NOT_ENOUGH_SAMPLES_FOR_GROUP_COUNT

    clusterable_matrix = filtered_vote_matrix.loc[participant_ids_to_cluster, :].fillna(0)
    if len(np.unique(clusterable_matrix.values, axis=0)) < 2:
        return InsufficientDataReason.NOT_ENOUGH_UNIQUE_POINTS

    return None


def prepare_pca_projection(
    *,
    votes: list[dict],
    reducer_kwargs: dict | None = None,
    mod_out_statement_ids: list[int] | None = None,
    meta_statement_ids: list[int] | None = None,
    min_user_vote_threshold: int = 7,
    keep_participant_ids: list[int] | None = None,
    random_state: Optional[int] = None,
) -> PcaProjectionResult:
    """Build the vote matrix, filtering, and PCA projection once for reuse across k candidates."""
    reducer_kwargs = reducer_kwargs or {}
    mod_out_statement_ids = mod_out_statement_ids or []
    meta_statement_ids = meta_statement_ids or []
    keep_participant_ids = keep_participant_ids or []

    raw_vote_matrix = generate_raw_matrix(votes=votes)
    filtered_vote_matrix = simple_filter_matrix(
        vote_matrix=raw_vote_matrix,
        mod_out_statement_ids=mod_out_statement_ids,
    )
    X_participants, X_statements, reducer_model = run_reducer(
        vote_matrix=filtered_vote_matrix.values,
        reducer="pca",
        random_state=random_state,
        **reducer_kwargs,
    )
    participants_df = pd.DataFrame(
        X_participants,
        columns=pd.Index(["x", "y"]),
        index=filtered_vote_matrix.index,
    )
    participant_ids_to_cluster = get_clusterable_participant_ids(
        raw_vote_matrix,
        vote_threshold=min_user_vote_threshold,
    )
    if keep_participant_ids:
        keep_participant_ids_existing = participants_df.index.intersection(
            keep_participant_ids,
        ).to_list()
        participant_ids_to_cluster = sorted(
            list(set(participant_ids_to_cluster + keep_participant_ids_existing))
        )
    participants_df["to_cluster"] = participants_df.index.isin(participant_ids_to_cluster)

    statements_df = pd.DataFrame(
        X_statements,
        columns=pd.Index(["x", "y"]),
        index=filtered_vote_matrix.columns,
    )
    statements_df["to_zero"] = statements_df.index.isin(mod_out_statement_ids)
    statements_df["is_meta"] = statements_df.index.isin(meta_statement_ids)
    if isinstance(reducer_model, PCA):
        pca = reducer_model

        def get_with_default(lst, idx, default=None):
            try:
                return lst[idx]
            except IndexError:
                return default

        statements_df["mean"] = pca.mean_
        statements_df["pc1"] = get_with_default(pca.components_, 0)
        statements_df["pc2"] = get_with_default(pca.components_, 1)
        statements_df["pc3"] = get_with_default(pca.components_, 2)
        statements_df = populate_priority_calculations_into_statements_df(
            statements_df=statements_df,
            vote_matrix=raw_vote_matrix.loc[participant_ids_to_cluster, :],
        )

    participant_projections = dict(zip(filtered_vote_matrix.index, X_participants))
    statement_projections = (
        dict(zip(filtered_vote_matrix.columns, X_statements))
        if X_statements is not None
        else None
    )

    return PcaProjectionResult(
        raw_vote_matrix=raw_vote_matrix,
        filtered_vote_matrix=filtered_vote_matrix,
        reducer=reducer_model,
        participants_df=participants_df,
        statements_df=statements_df,
        participant_ids_to_cluster=participant_ids_to_cluster,
        participant_projections=participant_projections,
        statement_projections=statement_projections,
    )


def _build_clustering_result_from_projection(
    *,
    projection: PcaProjectionResult,
    clusterer_model: ClustererModel | None,
    mod_out_statement_ids: list[int],
    pick_max: int,
    confidence: float,
) -> PolisClusteringResult:
    cluster_labels = clusterer_model.labels_ if clusterer_model else None
    participants_df = projection.participants_df.copy()
    label_series = pd.Series(
        cluster_labels,
        index=projection.participant_ids_to_cluster,
        dtype="Int64",
    )
    participants_df["cluster_id"] = label_series

    grouped_stats_df, gac_df = calculate_comment_statistics_dataframes(
        vote_matrix=projection.raw_vote_matrix.loc[projection.participant_ids_to_cluster, :],
        cluster_labels=cluster_labels,
    )
    statements_df = pd.concat([projection.statements_df.copy(), gac_df], axis=1)
    group_aware_consensus = {
        "agree": statements_df["group-aware-consensus-agree"].to_dict(),
        "disagree": statements_df["group-aware-consensus-disagree"].to_dict(),
    }
    consensus = select_consensus_statements(
        vote_matrix=projection.raw_vote_matrix,
        mod_out_statement_ids=mod_out_statement_ids,
        pick_max=pick_max,
        confidence=confidence,
        prob_threshold=0.5,
    )
    repness = select_representative_statements(
        grouped_stats_df=grouped_stats_df,
        mod_out_statement_ids=mod_out_statement_ids,
        pick_max=pick_max,
        confidence=confidence,
    )

    return PolisClusteringResult(
        participant_projections=projection.participant_projections,
        statement_projections=projection.statement_projections,
        group_aware_consensus=group_aware_consensus,
        consensus=consensus,
        repness=repness,
        raw_vote_matrix=projection.raw_vote_matrix,
        filtered_vote_matrix=projection.filtered_vote_matrix,
        reducer=projection.reducer,
        clusterer=clusterer_model,
        group_comment_stats=grouped_stats_df,
        statements_df=statements_df,
        participants_df=participants_df,
    )


def run_kmeans_on_pca_projection(
    *,
    projection: PcaProjectionResult,
    force_group_count: int,
    init_centers: Optional[list[list[float]]] = None,
    random_state: Optional[int] = None,
    mod_out_statement_ids: list[int] | None = None,
    pick_max: int = 5,
    confidence: float = 0.9,
) -> PolisClusteringResult:
    """Run one forced-k k-means candidate from an already prepared PCA projection."""
    clusterer_model = run_clusterer(
        clusterer="kmeans",
        X_participants_clusterable=projection.participants_df.loc[
            projection.participant_ids_to_cluster,
            ["x", "y"],
        ].values,
        max_group_count=force_group_count,
        force_group_count=force_group_count,
        init_centers=init_centers,
        random_state=random_state,
    )
    return _build_clustering_result_from_projection(
        projection=projection,
        clusterer_model=clusterer_model,
        mod_out_statement_ids=mod_out_statement_ids or [],
        pick_max=pick_max,
        confidence=confidence,
    )


def calculate_projection_silhouette_score(
    *,
    projection: PcaProjectionResult,
    clusterer_model: ClustererModel,
) -> float | None:
    """Calculate the candidate silhouette score from a prepared PCA projection."""
    return calculate_kmeans_silhouette_score(
        X_to_cluster=projection.participants_df.loc[
            projection.participant_ids_to_cluster,
            ["x", "y"],
        ].values,
        labels=clusterer_model.labels_,
    )


def run_pipeline_typed(**kwargs) -> TypedPolisClusteringResult:
    reason = get_insufficient_data_reason(
        votes=kwargs["votes"],
        mod_out_statement_ids=kwargs.get("mod_out_statement_ids", []),
        min_user_vote_threshold=kwargs.get("min_user_vote_threshold", 7),
        keep_participant_ids=kwargs.get("keep_participant_ids", []),
        force_group_count=kwargs.get("force_group_count"),
    )
    if reason is not None:
        return AnalysisInsufficientData(
            outcome=AnalysisOutcome.INSUFFICIENT_DATA,
            reason=reason,
        )
    return AnalysisSuccess(
        outcome=AnalysisOutcome.SUCCESS,
        result=run_pipeline(**kwargs),
    )


def run_pipeline(
    votes: list[dict],
    reducer: ReducerType = "pca",
    reducer_kwargs: dict = {},
    clusterer: ClustererType = "kmeans",
    clusterer_kwargs: dict = {},
    mod_out_statement_ids: list[int] = [],
    meta_statement_ids: list[int] = [],
    min_user_vote_threshold: int = 7,
    keep_participant_ids: list[int] = [],
    init_centers: Optional[list[list[float]]] = None,
    max_group_count: int = 5,
    force_group_count: Optional[int] = None,
    random_state: Optional[int] = None,
    pick_max: int = 5,
    confidence: float = 0.9,
) -> PolisClusteringResult:
    """
    An essentially feature-complete implementation of the Polis clustering algorithm.

    Still missing:
        - base-cluster calculations (so can't match output of conversations larger than 100 participants),
        - k-smoothing, which holds back k-value (group count) until re-calculated 3 consecutive times,
        - some advanced participant filtering that involves past state (you can use keep_participant_ids to mimic manually).

    Args:
        votes (list[dict]): Raw list of vote dicts, with keys for "participant_id", "statement_id", "vote" and "modified"
        reducer (ReducerType): Selects the type of reducer model to use.
        reducer_kwargs (dict): Extra params to pass to reducer model during initialization.
        clusterer (ClustererType): Selects the type of clusterer model to use.
        clusterer_kwargs (dict): Extra params to pass to clusterer model during initialization.
        mod_out_statement_ids (list[int]): List of statement IDs to moderate/zero out
        meta_statement_ids (list[int]): List of meta statement IDs
        min_user_vote_threshold (int): Minimum number of votes a participant must make to be included in clustering
        keep_participant_ids (list[int]): List of participant IDs to keep in clustering algorithm, regardless of normal filters.
        max_group_count (): Max number of group (k-values) to test using k-means and silhouette scores
        init_centers (list[list[float]]): Initial guesses of [x,y] coordinates for k-means (Length of list must match max_group_count)
        force_group_count (int): Instead of using silhouette scores, force a specific number of groups (k value)
        random_state (int): If set, will force determinism during k-means clustering
        confidence (float): Percent confidence interval (in decimal), within which selected statements are deemed significant
        pick_max (int): Max number of statements selected for consensus (per direction) and representative (per group).


    Returns:
        PolisClusteringResult: A dataclass containing clustering results, including intermediate calculations.
    """
    raw_vote_matrix = generate_raw_matrix(votes=votes)

    filtered_vote_matrix = simple_filter_matrix(
        vote_matrix=raw_vote_matrix,
        mod_out_statement_ids=mod_out_statement_ids,
    )

    # Run reducer and generate participant projections (and statement projections if possible).
    X_participants, X_statements, reducer_model = run_reducer(
        vote_matrix=filtered_vote_matrix.values,
        reducer=reducer,
        random_state=random_state,
        **reducer_kwargs,
    )
    participants_df = pd.DataFrame(X_participants, columns=pd.Index(["x", "y"]), index=filtered_vote_matrix.index)

    participant_ids_to_cluster = get_clusterable_participant_ids(
        raw_vote_matrix, vote_threshold=min_user_vote_threshold
    )
    if keep_participant_ids:
        # Ensure we're not trying to keep any participant IDs that don't exist in matrix.
        # TODO: Does this break any assumptions?
        keep_participant_ids_existing = participants_df.index.intersection(keep_participant_ids).to_list()
        participant_ids_to_cluster = sorted(
            list(set(participant_ids_to_cluster + keep_participant_ids_existing))
        )

    clusterer_model = run_clusterer(
        clusterer=clusterer,
        X_participants_clusterable=participants_df.loc[participant_ids_to_cluster, :].values,
        max_group_count=max_group_count,
        force_group_count=force_group_count,
        init_centers=init_centers,
        random_state=random_state,
        **clusterer_kwargs,
    )

    cluster_labels = clusterer_model.labels_ if clusterer_model else None

    label_series = pd.Series(
        cluster_labels,
        index=participant_ids_to_cluster,
        dtype="Int64",  # Allows nullable/NaN values.
    )
    participants_df["to_cluster"] = participants_df.index.isin(
        participant_ids_to_cluster
    )
    participants_df["cluster_id"] = label_series

    grouped_stats_df, gac_df = calculate_comment_statistics_dataframes(
        vote_matrix=raw_vote_matrix.loc[participant_ids_to_cluster, :],
        cluster_labels=cluster_labels,
    )

    def get_with_default(lst, idx, default=None):
        try:
            return lst[idx]
        except IndexError:
            return default

    statements_df = pd.DataFrame(X_statements, columns=pd.Index(["x", "y"]), index=filtered_vote_matrix.columns)
    statements_df["to_zero"] = statements_df.index.isin(mod_out_statement_ids)
    statements_df["is_meta"] = statements_df.index.isin(meta_statement_ids)
    if isinstance(reducer_model, PCA):
        pca = reducer_model
        statements_df["mean"] = pca.mean_
        statements_df["pc1"] = get_with_default(pca.components_, 0)
        statements_df["pc2"] = get_with_default(pca.components_, 1)
        statements_df["pc3"] = get_with_default(pca.components_, 2)
        # Can't run with without statement extremities from statement projections.
        statements_df = populate_priority_calculations_into_statements_df(
            statements_df=statements_df,
            vote_matrix=raw_vote_matrix.loc[participant_ids_to_cluster, :],
        )
    statements_df = pd.concat([statements_df, gac_df], axis=1)

    participant_projections = dict(zip(filtered_vote_matrix.index, X_participants))

    if X_statements is not None:
        statement_projections = dict(zip(filtered_vote_matrix.columns, X_statements))
    else:
        statement_projections = None

    group_aware_consensus = {
        "agree": statements_df["group-aware-consensus-agree"].to_dict(),
        "disagree": statements_df["group-aware-consensus-disagree"].to_dict(),
    }

    consensus = select_consensus_statements(
        vote_matrix=raw_vote_matrix,
        mod_out_statement_ids=mod_out_statement_ids,
        pick_max=pick_max,
        confidence=confidence,
        prob_threshold=0.5,
    )

    repness = select_representative_statements(
        grouped_stats_df=grouped_stats_df,
        mod_out_statement_ids=mod_out_statement_ids,
        pick_max=pick_max,
        confidence=confidence,
    )

    return PolisClusteringResult(
        participant_projections=participant_projections,
        statement_projections=statement_projections,
        group_aware_consensus=group_aware_consensus,
        consensus=consensus,
        repness=repness,

        # Raw & Intermediary values
        raw_vote_matrix=raw_vote_matrix,
        filtered_vote_matrix=filtered_vote_matrix,
        reducer=reducer_model,
        clusterer=clusterer_model,
        group_comment_stats=grouped_stats_df,
        statements_df=statements_df,
        participants_df=participants_df,
    )
