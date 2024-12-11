from sample_data.day9_sample import (
    SAMPLE_ARRANGED_FRAGMENTS,
    SAMPLE_DATA,
    SAMPLE_FRAGMENTS,
)

from day9.day9 import calculate_hash, fragment_disk, rearrange_fragments


def test_fragment_disk():
    expected_result = SAMPLE_FRAGMENTS
    assert fragment_disk(SAMPLE_DATA) == expected_result


def test_rearrange_fragments():
    expected_result = SAMPLE_ARRANGED_FRAGMENTS
    assert rearrange_fragments(SAMPLE_FRAGMENTS) == expected_result


def test_calculate_hash():
    expected_result = 1928
    assert calculate_hash(SAMPLE_ARRANGED_FRAGMENTS) == expected_result
