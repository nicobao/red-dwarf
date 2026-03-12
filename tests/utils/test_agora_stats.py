import numpy as np
import pandas as pd
import pytest
from numpy.testing import assert_array_equal

from reddwarf.utils.stats import (
    benjamini_hochberg,
    calculate_comment_statistics_dataframes,
    rank_representative_statements,
    z_to_pvalue,
)
from reddwarf.utils.consensus import rank_consensus_statements
from reddwarf.implementations.agora import compute_effective_agreement_gac


# --- z_to_pvalue ---


def test_z_to_pvalue_zero():
    assert z_to_pvalue(0.0) == pytest.approx(0.5)


def test_z_to_pvalue_large_positive():
    p = z_to_pvalue(5.0)
    assert p < 1e-5


def test_z_to_pvalue_negative():
    p = z_to_pvalue(-2.0)
    assert p > 0.5


def test_z_to_pvalue_array():
    result = z_to_pvalue(np.array([0.0, 5.0, -2.0]))
    assert result[0] == pytest.approx(0.5)
    assert result[1] < 1e-5
    assert result[2] > 0.5


# --- benjamini_hochberg ---


def test_benjamini_hochberg_basic():
    # 5 hypotheses, first 2 have small p-values
    p_values = np.array([0.001, 0.01, 0.3, 0.5, 0.9])
    selected = benjamini_hochberg(p_values, fdr_rate=0.10)
    # First two should be selected
    assert selected[0] == True
    assert selected[1] == True
    # Rest should not
    assert selected[2] == False
    assert selected[3] == False
    assert selected[4] == False


def test_benjamini_hochberg_empty():
    result = benjamini_hochberg(np.array([]), fdr_rate=0.10)
    assert len(result) == 0


def test_benjamini_hochberg_all_significant():
    p_values = np.array([0.001, 0.002, 0.003, 0.004])
    selected = benjamini_hochberg(p_values, fdr_rate=0.10)
    assert all(selected)


def test_benjamini_hochberg_none_significant():
    p_values = np.array([0.5, 0.6, 0.7, 0.8])
    selected = benjamini_hochberg(p_values, fdr_rate=0.10)
    assert not any(selected)


def test_benjamini_hochberg_adapts_to_size():
    """With many hypotheses, BH should be more conservative than a fixed threshold."""
    rng = np.random.default_rng(42)
    # 1000 p-values, 50 truly significant (very small) + 950 null (uniform)
    p_true = rng.uniform(1e-8, 1e-4, size=50)
    p_null = rng.uniform(0.05, 1.0, size=950)
    p_values = np.concatenate([p_true, p_null])

    selected_bh = benjamini_hochberg(p_values, fdr_rate=0.10)
    # Fixed threshold at 0.05 would select everything below 0.05
    selected_fixed = p_values < 0.05

    # BH should select fewer (or equal) than fixed threshold
    assert selected_bh.sum() <= selected_fixed.sum()
    # BH should still find some of the truly significant ones
    assert selected_bh.sum() > 0


# --- rank_representative_statements ---


def _make_grouped_stats_df():
    """Create a synthetic grouped_stats_df for testing rank functions."""
    # 2 groups, 3 statements
    data = []
    # Group 0: statement 0 strongly agree-rep, statement 1 weakly, statement 2 disagree-rep
    data.append({
        "group_id": 0, "statement_id": 0,
        "na": 8, "nd": 1, "ns": 10,
        "pa": 0.75, "pd": 0.15, "pat": 3.0, "pdt": -1.5,
        "ra": 1.8, "rd": 0.3, "rat": 4.0, "rdt": -2.0,
    })
    data.append({
        "group_id": 0, "statement_id": 1,
        "na": 5, "nd": 3, "ns": 10,
        "pa": 0.55, "pd": 0.35, "pat": 0.5, "pdt": -0.2,
        "ra": 1.1, "rd": 0.9, "rat": 0.3, "rdt": -0.1,
    })
    data.append({
        "group_id": 0, "statement_id": 2,
        "na": 1, "nd": 8, "ns": 10,
        "pa": 0.15, "pd": 0.75, "pat": -1.5, "pdt": 3.0,
        "ra": 0.3, "rd": 1.8, "rat": -2.0, "rdt": 4.0,
    })
    # Group 1: similar but different
    data.append({
        "group_id": 1, "statement_id": 0,
        "na": 3, "nd": 6, "ns": 10,
        "pa": 0.35, "pd": 0.65, "pat": -0.5, "pdt": 1.5,
        "ra": 0.7, "rd": 1.3, "rat": -1.0, "rdt": 2.0,
    })
    data.append({
        "group_id": 1, "statement_id": 1,
        "na": 6, "nd": 2, "ns": 10,
        "pa": 0.65, "pd": 0.25, "pat": 1.5, "pdt": -0.5,
        "ra": 1.3, "rd": 0.7, "rat": 2.0, "rdt": -1.0,
    })
    data.append({
        "group_id": 1, "statement_id": 2,
        "na": 4, "nd": 4, "ns": 10,
        "pa": 0.45, "pd": 0.45, "pat": 0.0, "pdt": 0.0,
        "ra": 1.0, "rd": 1.0, "rat": 0.0, "rdt": 0.0,
    })

    df = pd.DataFrame(data).set_index(["group_id", "statement_id"])
    return df


def test_rank_representative_statements_all_present():
    df = _make_grouped_stats_df()
    result = rank_representative_statements(df)
    # 2 groups, 3 statements each
    assert set(result.keys()) == {0, 1}
    for gid in [0, 1]:
        statement_ids = {s.statement_id for s in result[gid]}
        assert statement_ids == {0, 1, 2}


def test_rank_representative_statements_ranking_order():
    df = _make_grouped_stats_df()
    result = rank_representative_statements(df)
    for gid in result:
        statements = result[gid]
        # Should be sorted by effect_size descending
        effect_sizes = [s.effect_size for s in statements]
        assert effect_sizes == sorted(effect_sizes, reverse=True)
        # Rank 1 should have highest effect size
        assert statements[0].rank == 1


def test_rank_representative_statements_direction_selection():
    df = _make_grouped_stats_df()
    result = rank_representative_statements(df)
    # Group 0, statement 0: strong agree (rat=4.0, pat=3.0 vs rdt=-2.0, pdt=-1.5)
    stmt_0_g0 = [s for s in result[0] if s.statement_id == 0][0]
    assert stmt_0_g0.repful_for == "agree"
    # Group 0, statement 2: strong disagree (rdt=4.0, pdt=3.0 vs rat=-2.0, pat=-1.5)
    stmt_2_g0 = [s for s in result[0] if s.statement_id == 2][0]
    assert stmt_2_g0.repful_for == "disagree"


def test_rank_representative_statements_effect_size():
    df = _make_grouped_stats_df()
    result = rank_representative_statements(df)
    # Group 0, statement 0: agree direction, effect_size = ra * pa = 1.8 * 0.75
    stmt_0_g0 = [s for s in result[0] if s.statement_id == 0][0]
    assert stmt_0_g0.effect_size == pytest.approx(1.8 * 0.75)
    # Group 0, statement 2: disagree direction, effect_size = rd * pd = 1.8 * 0.75
    stmt_2_g0 = [s for s in result[0] if s.statement_id == 2][0]
    assert stmt_2_g0.effect_size == pytest.approx(1.8 * 0.75)


def test_rank_representative_statements_mod_out():
    df = _make_grouped_stats_df()
    result = rank_representative_statements(df, mod_out_statement_ids=[1])
    for gid in result:
        statement_ids = {s.statement_id for s in result[gid]}
        assert 1 not in statement_ids
        assert len(statement_ids) == 2


def test_rank_representative_statements_zero_vote_filter():
    """Zero-vote statements should not inflate BH hypothesis count."""
    df = _make_grouped_stats_df()
    # Add a zero-vote statement (na=0, nd=0) to each group
    zero_vote_data = [
        {
            "group_id": 0, "statement_id": 99,
            "na": 0, "nd": 0, "ns": 10,
            "pa": 0.50, "pd": 0.50, "pat": 0.0, "pdt": 0.0,
            "ra": 1.0, "rd": 1.0, "rat": 0.0, "rdt": 0.0,
        },
        {
            "group_id": 1, "statement_id": 99,
            "na": 0, "nd": 0, "ns": 10,
            "pa": 0.50, "pd": 0.50, "pat": 0.0, "pdt": 0.0,
            "ra": 1.0, "rd": 1.0, "rat": 0.0, "rdt": 0.0,
        },
    ]
    df_with_zero = pd.concat([
        df, pd.DataFrame(zero_vote_data).set_index(["group_id", "statement_id"])
    ])

    result_with = rank_representative_statements(df_with_zero)
    result_without = rank_representative_statements(df)

    for gid in result_with:
        # Zero-vote statement should be present but never selected
        zero_stmt = [s for s in result_with[gid] if s.statement_id == 99][0]
        assert zero_stmt.selected is False
        assert zero_stmt.adjusted_p_value == 1.0

        # Selection of other statements should be identical (zero-vote doesn't inflate m)
        sel_with = {s.statement_id for s in result_with[gid] if s.selected and s.statement_id != 99}
        sel_without = {s.statement_id for s in result_without[gid] if s.selected}
        assert sel_with == sel_without


# --- rank_consensus_statements ---


def _make_consensus_vote_matrix():
    """Create a synthetic vote matrix for consensus testing."""
    # 10 voters, 4 statements
    return pd.DataFrame(
        {
            0: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],      # strong agree
            1: [-1, -1, -1, -1, -1, -1, -1, -1, 1, 1],  # strong disagree
            2: [1, 1, 1, -1, -1, -1, 0, 0, 0, 0],    # mixed
            3: [1, 1, 1, 1, 1, 1, -1, -1, -1, -1],   # moderate agree
        },
        index=list(range(10)),
    )


def test_rank_consensus_statements_all_present():
    vm = _make_consensus_vote_matrix()
    result = rank_consensus_statements(vm)
    agree_ids = {s.statement_id for s in result.agree}
    disagree_ids = {s.statement_id for s in result.disagree}
    # All 4 statements should appear in both directions
    assert agree_ids == {0, 1, 2, 3}
    assert disagree_ids == {0, 1, 2, 3}


def test_rank_consensus_statements_ranking():
    vm = _make_consensus_vote_matrix()
    result = rank_consensus_statements(vm)
    # Agree: ranked by pa descending
    agree_pa = [s.pa for s in result.agree]
    assert agree_pa == sorted(agree_pa, reverse=True)
    # Disagree: ranked by pd descending
    disagree_pd = [s.pd for s in result.disagree]
    assert disagree_pd == sorted(disagree_pd, reverse=True)


def test_rank_consensus_statements_effect_size_matches_probability():
    vm = _make_consensus_vote_matrix()
    result = rank_consensus_statements(vm)
    for s in result.agree:
        assert s.effect_size == pytest.approx(s.pa)
    for s in result.disagree:
        assert s.effect_size == pytest.approx(s.pd)


# --- effective agreement GAC ---


def test_effective_agreement_penalizes_divided_groups():
    """A group split between agree/disagree should lower GAC vs unanimous."""
    # 2 groups of 5 participants, 1 statement.
    # Group 0: all agree. Group 1: split 3 agree / 2 disagree.
    vote_matrix_divided = pd.DataFrame(
        {0: [1, 1, 1, 1, 1, 1, 1, 1, -1, -1]},
        index=list(range(10)),
    )
    cluster_labels = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

    vote_matrix_unanimous = pd.DataFrame(
        {0: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]},
        index=list(range(10)),
    )

    grouped_divided, _ = calculate_comment_statistics_dataframes(
        vote_matrix=vote_matrix_divided, cluster_labels=cluster_labels,
    )
    grouped_unanimous, _ = calculate_comment_statistics_dataframes(
        vote_matrix=vote_matrix_unanimous, cluster_labels=cluster_labels,
    )

    gac_divided = compute_effective_agreement_gac(grouped_divided, [0], n_groups=2)
    gac_unanimous = compute_effective_agreement_gac(grouped_unanimous, [0], n_groups=2)

    # Divided group should lower the score
    assert gac_divided["agree"][0] < gac_unanimous["agree"][0]
    # A group split 3/2 should produce a score below 0.5
    assert gac_divided["agree"][0] < 0.5
    # Unanimous agreement should be well above 0.5
    assert gac_unanimous["agree"][0] > 0.5


def test_effective_agreement_gac_bounded():
    """All GAC scores should be in [0, 1] and <= raw pa baseline."""
    vote_matrix = pd.DataFrame(
        {
            0: [1, 1, 1, -1, -1, 1],
            1: [-1, -1, 1, 1, 1, -1],
            2: [1, 1, 1, 1, 1, 1],
        },
        index=list(range(6)),
    )
    cluster_labels = [0, 0, 0, 1, 1, 1]

    grouped_stats_df, _ = calculate_comment_statistics_dataframes(
        vote_matrix=vote_matrix, cluster_labels=cluster_labels,
    )
    n_groups = 2
    statement_ids = vote_matrix.columns.tolist()

    gac = compute_effective_agreement_gac(grouped_stats_df, statement_ids, n_groups)

    for sid in statement_ids:
        ea = gac["agree"][sid]
        ed = gac["disagree"][sid]
        assert 0 <= ea <= 1, f"agree GAC {ea} out of [0,1] for statement {sid}"
        assert 0 <= ed <= 1, f"disagree GAC {ed} out of [0,1] for statement {sid}"

        # Effective agreement should be <= raw pa geometric mean
        pa_product = 1.0
        for gid in range(n_groups):
            pa = grouped_stats_df.loc[(gid, sid), "pa"]
            pa_product *= pa
        raw_baseline = pa_product ** (1.0 / n_groups)
        assert ea <= raw_baseline + 1e-9, (
            f"Statement {sid}: effective agreement {ea} > raw baseline {raw_baseline}"
        )
