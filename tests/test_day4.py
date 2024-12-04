import pytest

from day4.day4 import solve_part_one, solve_part_two, validate_move, validate_word

SAMPLE_MATRIX = [
    ["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"],
    ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A"],
    ["A", "M", "X", "S", "X", "M", "A", "A", "M", "M"],
    ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X"],
    ["X", "M", "A", "S", "A", "M", "X", "A", "M", "M"],
    ["X", "X", "A", "M", "M", "X", "X", "A", "M", "A"],
    ["S", "M", "S", "M", "S", "A", "S", "X", "S", "S"],
    ["S", "A", "X", "A", "M", "A", "S", "A", "A", "A"],
    ["M", "A", "M", "M", "M", "X", "M", "M", "M", "M"],
    ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X"],
]

MATRIX_DIRECTIONS = {
    "north": (-1, 0),
    "north_east": (-1, 1),
    "east": (0, 1),
    "south_east": (1, 1),
    "south": (1, 0),
    "south_west": (1, -1),
    "west": (0, -1),
    "north_west": (-1, -1),
}


def test_validate_move():
    assert not validate_move(
        4, 4, 0, 0, -1, 0, 1
    ), "Should not be able to go up from row 0."

    assert not validate_move(
        4, 4, 3, 0, 1, 0, 1
    ), "Should not be able to go down from the bottom row."

    assert not validate_move(
        4, 4, 0, 0, 0, -1, 1
    ), "Should not be able to go left from column 0."

    assert not validate_move(
        4, 4, 0, 3, 0, 1, 1
    ), "Should not be able to go right from the last column."

    assert not validate_move(
        4, 4, 0, 3, -1, 1, 1
    ), "Should not be able to go up-right from the top-right corner."

    assert not validate_move(
        4, 4, 3, 3, 1, 1, 1
    ), "Should not be able to go down-right from the bottom-right corner."

    assert not validate_move(
        4, 4, 3, 0, 1, -1, 1
    ), "Should not be able to go down-left from the bottom-left corner."

    assert not validate_move(
        4, 4, 0, 0, -1, -1, 1
    ), "Should not be able to go up-left from the top-left corner."

    assert validate_move(
        4, 4, 3, 0, -1, 0, 3
    ), "Should be able to go up 3 steps from (3, 0)."

    assert validate_move(
        4, 4, 0, 0, 0, 1, 3
    ), "Should be able to go right 3 steps from (0, 0)."

    assert validate_move(
        4, 4, 3, 0, -1, 1, 3
    ), "Should be able to go diagonally up-right from (3, 0)."

    assert validate_move(
        4, 4, 3, 3, -1, -1, 3
    ), "Should be able to go diagonally up-left from (3, 3)."


def test_validate_word():
    assert validate_word("XMAS", ["X", "M", "A", "S"])
    assert not validate_word("XMAS", ["X", "M", "S", "S"])
    with pytest.raises(TypeError, match="Expected `letters` to be a list of strings."):
        validate_word("XMAS", "XMAS")

    with pytest.raises(TypeError, match="Expected `letters` to be a list of strings."):
        validate_word("XMAS", [1, 2, 3])

    with pytest.raises(TypeError, match="Expected `letters` to be a list of strings."):
        validate_word("XMAS", None)


def test_solve_part_one():
    expected_result = 18
    result = solve_part_one(SAMPLE_MATRIX, MATRIX_DIRECTIONS, "XMAS")
    assert (
        expected_result == result
    ), f"Result should be {expected_result} and not {result}"


def test_solve_part_two():
    expected_result = 9
    result = solve_part_two(SAMPLE_MATRIX, MATRIX_DIRECTIONS, "MAS")
    assert (
        expected_result == result
    ), f"Result should be {expected_result} and not {result}"
