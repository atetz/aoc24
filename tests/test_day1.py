from typing import List

from day1.day1 import clean_input, create_location_lists, solve_part_one, solve_part_two

SAMPLE_INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3
"""


def test_clean_input():
    cleaned_input = clean_input(SAMPLE_INPUT)
    input_type = type(cleaned_input)
    input_as_string = "".join([str(s) for s in cleaned_input])
    assert " " not in input_as_string, "Space found in cleaned_input"
    assert "-" in input_as_string, "Input should have '-' characters"
    assert isinstance(cleaned_input, List), f"Output is not a list but {input_type}."
    assert isinstance(cleaned_input, List), f"Output is not a list but {input_type}."


def test_create_location_lists():
    cleaned_input = ["3-4", "4-3", "2-5", "1-3", "3-9", "3-3"]
    left_locations, right_locations = create_location_lists(cleaned_input)
    assert isinstance(
        left_locations, List
    ), f"Left output is not a list but {type(left_locations)}."
    assert isinstance(
        left_locations, List
    ), f"Right output is not a list but {type(right_locations)}."
    assert (
        left_locations[0] == 1
    ), f"Lowest number of left list should be 1, got {left_locations[0]}"
    assert (
        right_locations[1] == 3
    ), f"Lowest number of right list should be 3, got {left_locations[0]}"


def test_solve_part_one():
    left_locations = [1, 2, 3, 3, 3, 4]
    right_locations = [3, 3, 3, 4, 5, 9]
    result = solve_part_one(left_locations, right_locations)
    assert result == 11, f"Part one should return 11, not {result}"


def test_solve_part_two():
    left_locations = [1, 2, 3, 3, 3, 4]
    right_locations = [3, 3, 3, 4, 5, 9]
    result = solve_part_two(left_locations, right_locations)
    assert result == 31, f"Part two should return 31, not {result}"
