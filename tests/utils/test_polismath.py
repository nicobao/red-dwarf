import pytest
from reddwarf.utils import polismath
from tests.fixtures import polis_convo_data
from reddwarf.utils import matrix as MatrixUtils
from reddwarf.utils.polismath import get_corrected_centroid_guesses
from reddwarf.data_loader import Loader

# TODO: Figure out if in-conv is always equivalent. If so, remove this test.
@pytest.mark.parametrize("polis_convo_data", ["small-no-meta", "small-with-meta", "medium-with-meta", "medium-no-meta"], indirect=True)
def test_extract_data_from_polismath(polis_convo_data):
    fixture = polis_convo_data
    expected = fixture.math_data["in-conv"]

    actual_participant_ids, *_ = polismath.extract_data_from_polismath(fixture.math_data)

    assert sorted(expected) == actual_participant_ids

# This check is to ensure that the vote_data used to assemble the vote_matrix
# matches what polismath is calculating from. Sometimes votes from random
# participants just don't get returned via API.
#
# Any dataset used to testing should be parameterized here.
#
# Example: participant 50 has 4 votes in exports CSVs and polismath user-vote-count data:
#   https://pol.is/api/v3/math/pca2?conversation_id=6ukkcvfbre
# But no votes show up here:
#   https://pol.is/api/v3/votes?conversation_id=6ukkcvfbre&pid=50
#
# These conversations also have data integrity issues:
#   - https://pol.is/report/r64ajcsmp9butzxhzj44c ("small-no-meta-bad", see above)
#   - https://pol.is/report/r5ackfcj5dmawnt2de7x7
#   - https://pol.is/report/r45ru4zfmutun54ttskne
#
# TODO: Investigate what causes conversations to have missing votes.
#       For now, leaning on other conversations or CSV export mitigates the issue.
@pytest.mark.parametrize("polis_convo_data", ["small-no-meta", "small-with-meta", "medium-with-meta", "medium-no-meta"], indirect=True)
def test_user_vote_count_sanity_check(polis_convo_data):
    fixture = polis_convo_data
    expected_user_vote_counts = fixture.math_data["user-vote-counts"]
    # Convert keys from string to int for later comparison.
    expected_user_vote_counts = {int(k):v for k,v in expected_user_vote_counts.items()}

    loader = Loader(filepaths=[f"{fixture.data_dir}/votes.json"])
    real_vote_matrix = MatrixUtils.generate_raw_matrix(votes=loader.votes_data)
    actual_user_vote_counts = real_vote_matrix.count(axis="columns")

    assert expected_user_vote_counts == actual_user_vote_counts.to_dict()

@pytest.fixture
def mock_math_data():
    return {
        "group-clusters": [
            {"center": [1.0, 2.0]},
            {"center": [-3.0, 4.0]}
        ],
        "base-clusters": {
            "x": [5.0, -6.0],
            "y": [7.0, -8.0]
        }
    }

def test_get_corrected_centroid_guesses_default_flip(mock_math_data):
    result = get_corrected_centroid_guesses(mock_math_data)
    assert result == [[-1.0, -2.0], [3.0, -4.0]]

def test_get_corrected_centroid_guesses_unflip_x(mock_math_data):
    result = get_corrected_centroid_guesses(mock_math_data, flip_x=False)
    assert result == [[1.0, -2.0], [-3.0, -4.0]]

def test_get_corrected_centroid_guesses_unflip_y(mock_math_data):
    result = get_corrected_centroid_guesses(mock_math_data, flip_y=False)
    assert result == [[-1.0, 2.0], [3.0, 4.0]]

def test_get_corrected_centroid_guesses_group_unflip_both(mock_math_data):
    result = get_corrected_centroid_guesses(mock_math_data, source="group-clusters", flip_x=False, flip_y=False)
    assert result == [[1.0, 2.0], [-3.0, 4.0]]

def test_get_corrected_centroid_guesses_base_clusters_unflip_x(mock_math_data):
    result = get_corrected_centroid_guesses(mock_math_data, source="base-clusters", flip_x=False)
    assert result == [[5.0, -7.0], [-6.0, 8.0]]

def test_get_corrected_centroid_guesses_base_clusters_unflip_y(mock_math_data):
    result = get_corrected_centroid_guesses(mock_math_data, source="base-clusters", flip_y=False)
    assert result == [[-5.0, 7.0], [6.0, -8.0]]

def test_get_corrected_centroid_guesses_unknown_source(mock_math_data):
    with pytest.raises(ValueError, match="Unknown source 'invalid-source'"):
        get_corrected_centroid_guesses(mock_math_data, source="invalid-source")