from day11.day11 import cached_count


def test_cached_count():
    cache = {}
    stones = [125, 17]
    blinks = 6
    expected_result = [7, 15]

    for i in range(len(stones)):
        assert cached_count(cache, stones[i], blinks) == expected_result[i]


def test_count_stones():
    cache = {}
    stones = [125, 17]
    blinks = 6
    expected_result = 22
    assert (
        sum(cached_count(cache, stone, blinks) for stone in stones) == expected_result
    )
