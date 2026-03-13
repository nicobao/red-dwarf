import numpy as np
import pandas as pd
import pytest
from tests.fixtures import polis_convo_data
from reddwarf.utils import stats

from reddwarf.utils import stats, polismath, matrix
from reddwarf.data_loader import Loader
from tests import helpers

def test_importance_metric_no_votes():
    expected_importance = [ 1/4,   2/4,   1,     2,      4   ]
    comment_extremity =   [(1-1), (2-1), (4-1), (8-1), (16-1)]
    # extremity values    [ 0,     1,     3,     7,     15   ]

    calculated_importance = stats.importance_metric(
        n_agree=0,
        n_disagree=0,
        n_total=0,
        extremity=comment_extremity,
    )

    assert expected_importance == calculated_importance.tolist()

def test_importance_metric_limits_no_extremity_all_agree():
    comment_extremity = 0
    expected_importance = 1

    calculated_importance = stats.importance_metric(
        n_agree=10000,
        n_disagree=0,
        n_total=10000,
        extremity=comment_extremity,
    )
    assert expected_importance == pytest.approx(calculated_importance, abs=0.001)

def test_importance_metric_limits_no_extremity_all_disagree():
    comment_extremity = 0
    expected_importance = 0

    calculated_importance = stats.importance_metric(
        n_agree=0,
        n_disagree=10000,
        n_total=10000,
        extremity=comment_extremity,
    )
    assert expected_importance == pytest.approx(calculated_importance, abs=0.001)

def test_importance_metric_limits_no_extremity_split_full_engagement():
    comment_extremity = 0
    expected_importance = 1/4

    calculated_priority = stats.priority_metric(
        is_meta=False,
        n_agree=5000,
        n_disagree=5000,
        n_total=10000,
        extremity=comment_extremity,
    )
    assert calculated_priority == pytest.approx(expected_importance, abs=0.001)

def test_importance_metric_limits_no_extremity_all_pass():
    comment_extremity = 0
    expected_importance = 0

    calculated_importance = stats.importance_metric(
        n_agree=0,
        n_disagree=0,
        n_total=10000,
        extremity=comment_extremity,
    )
    assert expected_importance == pytest.approx(calculated_importance, abs=0.001)

def test_importance_metric_limits_high_extremity_all_agree():
    comment_extremity = 4.0
    expected_importance = comment_extremity+1

    calculated_importance = stats.importance_metric(
        n_agree=10000,
        n_disagree=0,
        n_total=10000,
        extremity=comment_extremity,
    )
    assert expected_importance == pytest.approx(calculated_importance, abs=0.001)

def test_importance_metric_limits_high_extremity_all_disagree():
    comment_extremity = 4.0
    expected_importance = 0

    calculated_importance = stats.importance_metric(
        n_agree=0,
        n_disagree=10000,
        n_total=10000,
        extremity=comment_extremity,
    )
    assert expected_importance == pytest.approx(calculated_importance, abs=0.001)

def test_importance_metric_limits_high_extremity_all_pass():
    comment_extremity = 4.0
    expected_importance = 0

    calculated_importance = stats.importance_metric(
        n_agree=0,
        n_disagree=0,
        n_total=10000,
        extremity=comment_extremity,
    )
    assert expected_importance == pytest.approx(calculated_importance, abs=0.001)

# TODO: Use this test to more fully show trends and effects.
@pytest.mark.skip()
def test_importance_metric_array():
    expected_importances = [0, 7**2]

    calculated_priority = stats.importance_metric(
        n_agree=   [    0,     0],
        n_disagree=[10000, 10000],
        n_total=   [10000, 10000],
        extremity= [  4.0,   4.0],
    )
    assert calculated_priority == pytest.approx(expected_importances, abs=0.001)

def test_importance_metric_smaller_full_agree_pseudo_count():
    # Should approach 1 at higher volume of votes
    pseudo_counts =        [1,     10]
    # Approaches slower with higher pseudo-count.
    expected_importances = [0.9804, 0.84027778]

    calculated_priority = stats.importance_metric(
        n_agree=   [100, 100],
        n_disagree=[  0,   0],
        n_total=   [100, 100],
        extremity= [  0,   0],
        pseudo_count=pseudo_counts,
    )
    assert calculated_priority == pytest.approx(expected_importances, abs=0.001)

def test_priority_metric_no_votes():
    prio = lambda n: (81/16)*(4**n)
    # expected_values = [ 5.0625,  20.25,   81,      324,     1296   ]
    expected_priority = [ prio(0), prio(1), prio(2), prio(3), prio(4)]
    comment_extremity = [ 0,       1,       (4-1),   (8-1),   (16-1) ]
    # extremity values  [ 0,       1,        3,       7,       15    ]

    calculated_priority = stats.priority_metric(
        is_meta=False,
        n_agree=0,
        n_disagree=0,
        n_total=0,
        extremity=comment_extremity,
    )

    assert expected_priority == calculated_priority.tolist()

# TODO: Investigate why "medium-with-meta" and "medium-no-meta" don't pass.
@pytest.mark.parametrize("polis_convo_data", ["small-no-meta", "small-with-meta", "medium-no-meta", "medium-with-meta"], indirect=True)
def test_priority_metric_real_data(polis_convo_data):
    fixture = polis_convo_data
    votes_base = fixture.math_data["votes-base"]
    # Get index and statement_id because polismath lists (like pca sub-keys) are
    # indexed, and polismath objects (like priorities) are keyed to statement_id
    for idx, (statement_id, votes) in enumerate(votes_base.items()):
        expected_priority = fixture.math_data["comment-priorities"][statement_id]

        is_meta = int(statement_id) in fixture.math_data["meta-tids"]
        n_agree = np.asarray(votes["A"]).sum()
        n_disagree = np.asarray(votes["D"]).sum()
        n_total = np.asarray(votes["S"]).sum()
        comment_extremity = fixture.math_data["pca"]["comment-extremity"][idx]

        calculated_priority = stats.priority_metric(
            is_meta=is_meta,
            n_agree=n_agree,
            n_disagree=n_disagree,
            n_total=n_total,
            extremity=comment_extremity,
        )
        assert expected_priority == pytest.approx(calculated_priority)

def test_priority_metric_for_meta_default():
    meta_priority_default = 7
    expected_priority = meta_priority_default**2

    calculated_priority = stats.priority_metric(
        is_meta=True,
        n_agree=10,
        n_disagree=0,
        n_total=25,
        extremity=0,
    )

    assert calculated_priority == expected_priority

def test_priority_metric_for_meta_override():
    meta_priority_override = 10
    expected_priority = meta_priority_override**2

    calculated_priority = stats.priority_metric(
        is_meta=True,
        n_agree=10,
        n_disagree=0,
        n_total=25,
        extremity=1.0,
        meta_priority=meta_priority_override,
    )
    assert calculated_priority == expected_priority

def test_priority_metric_limits_no_extremity_all_passing():
    comment_extremity = 0
    expected_priority = 0

    calculated_priority = stats.priority_metric(
        is_meta=False,
        n_agree=0,
        n_disagree=0,
        n_total=10000,
        extremity=comment_extremity,
    )
    assert calculated_priority == pytest.approx(expected_priority)

def test_priority_metric_limits_no_extremity_all_disagree():
    comment_extremity = 0
    expected_priority = 0

    calculated_priority = stats.priority_metric(
        is_meta=False,
        n_agree=0,
        n_disagree=10000,
        n_total=10000,
        extremity=comment_extremity,
    )
    assert calculated_priority == pytest.approx(expected_priority, abs=0.001)

def test_priority_metric_limits_no_extremity_all_agree():
    comment_extremity = 0
    expected_priority = 1

    calculated_priority = stats.priority_metric(
        is_meta=False,
        n_agree=10000,
        n_disagree=0,
        n_total=10000,
        extremity=comment_extremity,
    )
    assert calculated_priority == pytest.approx(expected_priority, abs=0.001)

def test_priority_metric_limits_no_extremity_split_full_engagement():
    comment_extremity = 0
    expected_priority = 1/4

    calculated_priority = stats.priority_metric(
        is_meta=False,
        n_agree=5000,
        n_disagree=5000,
        n_total=10000,
        extremity=comment_extremity,
    )
    assert calculated_priority == pytest.approx(expected_priority, abs=0.001)

def test_priority_metric_limits_high_extremity_all_passed():
    comment_extremity = 4.0
    expected_priority = 0

    calculated_priority = stats.priority_metric(
        is_meta=False,
        n_agree=0,
        n_disagree=0,
        n_total=10000,
        extremity=comment_extremity,
    )
    assert calculated_priority == pytest.approx(expected_priority)

def test_priority_metric_limits_high_extremity_all_agree():
    comment_extremity = 4.0
    expected_priority = (comment_extremity+1)**2

    calculated_priority = stats.priority_metric(
        is_meta=False,
        n_agree=10000,
        n_disagree=0,
        n_total=10000,
        extremity=comment_extremity,
    )
    assert calculated_priority == pytest.approx(expected_priority, abs=0.01)

def test_priority_metric_limits_high_extremity_all_disagree():
    comment_extremity = 4.0
    expected_priority = 0

    calculated_priority = stats.priority_metric(
        is_meta=False,
        n_agree=0,
        n_disagree=10000,
        n_total=10000,
        extremity=comment_extremity,
    )
    assert calculated_priority == pytest.approx(expected_priority, abs=0.001)

# TODO: Use this test to more fully show trends and effects.
def test_priority_metric_array():
    expected_priorities = [0, 7**2]

    calculated_priority = stats.priority_metric(
        is_meta=   [False,  True],
        n_agree=   [    0,     0],
        n_disagree=[10000, 10000],
        n_total=   [10000, 10000],
        extremity= [  4.0,   4.0],
    )
    assert calculated_priority == pytest.approx(expected_priorities, abs=0.001)

@pytest.mark.parametrize("polis_convo_data", ["small-no-meta", "small-with-meta", "medium-no-meta", "medium-with-meta"], indirect=True)
def test_group_aware_consensus_real_data(polis_convo_data):
    """
    Verify group-aware consensus on real Polis data.

    Tests both the Polis-compatible baseline (geometric mean of raw p_agree)
    and our effective agreement divergence (p_agree * (1 - p_disagree)).
    """
    fixture = polis_convo_data
    loader = Loader(filepaths=[
        f'{fixture.data_dir}/votes.json',
        f'{fixture.data_dir}/comments.json',
        f'{fixture.data_dir}/conversation.json',
    ])
    VOTES = loader.votes_data
    vote_matrix = matrix.generate_raw_matrix(votes=VOTES)

    # TODO: Why do moderated out statements not plug into comment stats? BUG?
    # STATEMENTS = loader.comments_data
    # _, _, mod_out, _ = stmnts.process_statements(statement_data=STATEMENTS)
    # vote_matrix = matrix.simple_filter_matrix(
    #     vote_matrix=vote_matrix,
    #     mod_out_statement_ids=mod_out,
    # )

    # Get list of all active participant ids, since Polis has some edge-cases
    # that keep specific participants, and we need to keep them from being filtered out.
    all_clustered_participant_ids, cluster_labels = polismath.extract_data_from_polismath(fixture.math_data)
    vote_matrix = vote_matrix.loc[all_clustered_participant_ids, :]

    # Generate stats for all groups and all statements.
    # This returns both per-group probabilities (P_v_g_c) and
    # the final group-aware consensus (C_v_c) which uses effective agreement.
    N_g_c, N_v_g_c, P_v_g_c, _, P_v_g_c_test, _, C_v_c = stats.calculate_comment_statistics(
        vote_matrix=vote_matrix,
        cluster_labels=cluster_labels,
    )

    n_groups = len(set(cluster_labels))

    # 1) Verify Polis baseline: geometric mean of raw p_agree still matches fixtures
    polis_baseline_agree = P_v_g_c[stats.votes.A, :, :].prod(axis=0) ** (1.0 / n_groups)
    calculated_baseline = {
        str(sid): float(polis_baseline_agree[i])
        for i, sid in enumerate(vote_matrix.columns)
    }
    expected_polis_gac = helpers.polis_gac_to_geometric_mean(n_groups, fixture.math_data["group-aware-consensus"])
    assert calculated_baseline == pytest.approx(expected_polis_gac)

    # 2) Verify effective agreement scores are in [0, 1] and <= Polis baseline
    for i, sid in enumerate(vote_matrix.columns):
        effective_score = float(C_v_c[stats.votes.A, i])
        baseline_score = float(polis_baseline_agree[i])
        assert 0 <= effective_score <= 1, f"Statement {sid}: score {effective_score} out of [0, 1]"
        assert effective_score <= baseline_score + 1e-9, (
            f"Statement {sid}: effective agreement {effective_score} should be "
            f"<= Polis baseline {baseline_score}"
        )


def test_group_aware_consensus_uses_geometric_mean():
    """
    Verify that group-aware consensus uses geometric mean (product^(1/n_groups))
    so that scores are comparable regardless of the number of groups.
    """
    # Build a vote matrix: 6 participants, 2 groups, 1 statement.
    # All participants agree on the statement.
    vote_matrix = pd.DataFrame(
        {0: [1, 1, 1, 1, 1, 1]},
        index=[0, 1, 2, 3, 4, 5],
    )
    # 2 groups of 3 participants each
    cluster_labels_2 = [0, 0, 0, 1, 1, 1]
    # 3 groups of 2 participants each
    cluster_labels_3 = [0, 0, 1, 1, 2, 2]

    *_, C_2 = stats.calculate_comment_statistics(
        vote_matrix=vote_matrix,
        cluster_labels=cluster_labels_2,
    )
    *_, C_3 = stats.calculate_comment_statistics(
        vote_matrix=vote_matrix,
        cluster_labels=cluster_labels_3,
    )

    agree_score_2_groups = C_2[0, 0]  # votes.A = 0
    agree_score_3_groups = C_3[0, 0]

    # With geometric mean, both should be reasonably close (same underlying consensus).
    # Without it (raw product), 3 groups would give much lower scores.
    # The effective agreement formula (p_agree * (1 - p_disagree)) amplifies
    # the Laplace smoothing gap between group sizes, so the tolerance is wider
    # than with raw p_agree alone.
    assert agree_score_2_groups == pytest.approx(agree_score_3_groups, abs=0.1)

    # Both should be above 0.5 (all participants agree)
    assert agree_score_2_groups > 0.5
    assert agree_score_3_groups > 0.5


def test_group_aware_consensus_penalizes_divided_groups():
    """
    Verify that a group split roughly evenly between agree and disagree
    drags down the consensus score compared to unanimous agreement.

    This is the core behavior of the effective agreement divergence from Polis.
    """
    # 2 groups of 5 participants, 1 statement.
    # Group 0: all agree. Group 1: split 3 agree / 2 disagree.
    vote_matrix_divided = pd.DataFrame(
        {0: [1, 1, 1, 1, 1, 1, 1, 1, -1, -1]},
        index=list(range(10)),
    )
    cluster_labels = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

    # Unanimous: both groups fully agree
    vote_matrix_unanimous = pd.DataFrame(
        {0: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]},
        index=list(range(10)),
    )

    *_, C_divided = stats.calculate_comment_statistics(
        vote_matrix=vote_matrix_divided,
        cluster_labels=cluster_labels,
    )
    *_, C_unanimous = stats.calculate_comment_statistics(
        vote_matrix=vote_matrix_unanimous,
        cluster_labels=cluster_labels,
    )

    divided_score = C_divided[stats.votes.A, 0]
    unanimous_score = C_unanimous[stats.votes.A, 0]

    # Divided group should significantly lower the consensus score
    assert divided_score < unanimous_score
    # A group split 3/2 should produce a score below the 0.6 consensus threshold
    assert divided_score < 0.6
    # Unanimous agreement should be well above 0.6
    assert unanimous_score > 0.6


def test_consensus_small_group_unanimous():
    """
    A group of 2 with unanimous agreement should produce consensus > 0.6.

    With Laplace smoothing (pseudo_count=1), a group of 2 all-agree gets
    effective_agree ~0.562, falling below the 0.6 frontend threshold.
    With Jeffreys prior (pseudo_count=0.5), it gets ~0.694, above threshold.
    """
    # 2 groups: group 0 has 2 members, group 1 has 3 members. All agree.
    vote_matrix = pd.DataFrame(
        {0: [1, 1, 1, 1, 1]},
        index=[0, 1, 2, 3, 4],
    )
    cluster_labels = [0, 0, 1, 1, 1]

    *_, C_v_c = stats.calculate_comment_statistics(
        vote_matrix=vote_matrix,
        cluster_labels=cluster_labels,
    )

    consensus_agree = C_v_c[stats.votes.A, 0]

    # With Jeffreys prior, consensus should be well above 0.6
    assert consensus_agree > 0.6, (
        f"Small unanimous groups should produce consensus > 0.6, got {consensus_agree:.4f}"
    )
    # Specific expected value: ~0.729
    assert consensus_agree == pytest.approx(0.729, abs=0.01)


def test_consensus_small_group_unanimous_with_laplace():
    """
    Verify that passing pseudo_count=1 (Laplace) for consensus produces lower scores
    than the default Jeffreys prior, confirming the parameter works.
    """
    vote_matrix = pd.DataFrame(
        {0: [1, 1, 1, 1, 1]},
        index=[0, 1, 2, 3, 4],
    )
    cluster_labels = [0, 0, 1, 1, 1]

    *_, C_jeffreys = stats.calculate_comment_statistics(
        vote_matrix=vote_matrix,
        cluster_labels=cluster_labels,
    )
    *_, C_laplace = stats.calculate_comment_statistics(
        vote_matrix=vote_matrix,
        cluster_labels=cluster_labels,
        consensus_pseudo_count=1.0,
    )

    jeffreys_score = C_jeffreys[stats.votes.A, 0]
    laplace_score = C_laplace[stats.votes.A, 0]

    # Jeffreys should give higher consensus for unanimous small groups
    assert jeffreys_score > laplace_score
    # Laplace score should be ~0.600 (barely at the threshold)
    assert laplace_score == pytest.approx(0.600, abs=0.01)


def test_consensus_divided_group_detected():
    """
    A group genuinely divided (3/5 agree, 2/5 disagree) should produce
    consensus below 0.6 even with Jeffreys prior.

    This verifies the effective agreement formula still detects division.
    """
    # Group 0: 5 members all agree. Group 1: 5 members, 3 agree / 2 disagree.
    vote_matrix = pd.DataFrame(
        {0: [1, 1, 1, 1, 1, 1, 1, 1, -1, -1]},
        index=list(range(10)),
    )
    cluster_labels = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

    *_, C_v_c = stats.calculate_comment_statistics(
        vote_matrix=vote_matrix,
        cluster_labels=cluster_labels,
    )

    consensus_agree = C_v_c[stats.votes.A, 0]

    # Divided group should drag consensus below 0.6
    assert consensus_agree < 0.6, (
        f"Divided group (3/5 agree) should produce consensus < 0.6, got {consensus_agree:.4f}"
    )
    # Specific expected value: ~0.535
    assert consensus_agree == pytest.approx(0.535, abs=0.01)


def test_consensus_strongly_disputed():
    """
    One group all-agree vs one group all-disagree should produce very low consensus.
    """
    vote_matrix = pd.DataFrame(
        {0: [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]},
        index=list(range(10)),
    )
    cluster_labels = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

    *_, C_v_c = stats.calculate_comment_statistics(
        vote_matrix=vote_matrix,
        cluster_labels=cluster_labels,
    )

    consensus_agree = C_v_c[stats.votes.A, 0]

    # Strongly disputed should produce very low consensus
    assert consensus_agree < 0.1, (
        f"Strongly disputed statement should have consensus < 0.1, got {consensus_agree:.4f}"
    )


def test_consensus_representativeness_uses_laplace():
    """
    Verify that the Jeffreys prior only affects consensus, not representativeness.
    P_v_g_c (used for representativeness ratios) should still use pseudo_count=1.
    """
    vote_matrix = pd.DataFrame(
        {0: [1, 1, 1, 1, 1]},
        index=[0, 1, 2, 3, 4],
    )
    cluster_labels = [0, 0, 1, 1, 1]

    _, _, P_v_g_c, _, _, _, _ = stats.calculate_comment_statistics(
        vote_matrix=vote_matrix,
        cluster_labels=cluster_labels,
    )

    # Group 0 has 2 members, all agree.
    # With Laplace (pseudo_count=1): P_agree = (1+2)/(2+2) = 0.75
    p_agree_group0 = P_v_g_c[stats.votes.A, 0, 0]
    assert p_agree_group0 == pytest.approx(0.75, abs=0.001), (
        f"Representativeness probabilities should use Laplace (pseudo_count=1), "
        f"got P_agree={p_agree_group0:.4f} instead of 0.75"
    )


def test_format_comment_stats_repful_agree():
    statement = pd.Series({
        "statement_id": 1,
        "ns": 100,
        "na": 60, "pa": 0.6, "pat": 2.0,
        "nd": 40, "pd": 0.4, "pdt": 1.5,
        "ra": 0.8, "rat": 3.0,
        "rd": 0.5, "rdt": 2.0,
    })

    result = stats.format_comment_stats(statement)
    assert result == {
        "tid": 1,
        "n-success": 60,
        "n-trials": 100,
        "p-success": 0.6,
        "p-test": 2.0,
        "repness": 0.8,
        "repness-test": 3.0,
        "repful-for": "agree",
    }

def test_format_comment_stats_repful_disagree():
    statement = pd.Series({
        "statement_id": 2,
        "ns": 100,
        "na": 45, "pa": 0.45, "pat": 1.7,
        "nd": 55, "pd": 0.55, "pdt": 2.0,
        "ra": 0.5, "rat": 1.8,
        "rd": 0.7, "rdt": 2.5,
    })

    result = stats.format_comment_stats(statement)
    assert result == {
        "tid": 2,
        "n-success": 55,
        "n-trials": 100,
        "p-success": 0.55,
        "p-test": 2.0,
        "repness": 0.7,
        "repness-test": 2.5,
        "repful-for": "disagree",
    }

def test_format_comment_stats_consensus_agree():
    statement = pd.Series({
        "statement_id": 3,
        "ns": 100,
        "na": 70, "pa": 0.7, "pat": 2.2,
        "nd": 30, "pd": 0.3, "pdt": 1.0,
    })

    result = stats.format_comment_stats(statement)
    assert result == {
        "tid": 3,
        "n-success": 70,
        "n-trials": 100,
        "p-success": 0.7,
        "p-test": 2.2,
        "cons-for": "agree",
    }

def test_format_comment_stats_consensus_disagree():
    statement = pd.Series({
        "statement_id": 4,
        "ns": 100,
        "na": 40, "pa": 0.4, "pat": 1.2,
        "nd": 60, "pd": 0.6, "pdt": 2.3,
    })

    result = stats.format_comment_stats(statement)
    assert result == {
        "tid": 4,
        "n-success": 60,
        "n-trials": 100,
        "p-success": 0.6,
        "p-test": 2.3,
        "cons-for": "disagree",
    }