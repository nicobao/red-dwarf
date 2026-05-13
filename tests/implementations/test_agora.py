from reddwarf.implementations.agora import run_pipeline_typed
from reddwarf.implementations.base import AnalysisOutcome, InsufficientDataReason


def test_agora_run_pipeline_typed_returns_base_insufficient_data_reason():
    result = run_pipeline_typed(votes=[])

    assert result.outcome == AnalysisOutcome.INSUFFICIENT_DATA
    assert result.reason == InsufficientDataReason.EMPTY_VOTE_MATRIX
