import re
from collections import Counter
from typing import List

from utils.helpers import read_puzzle_input_as_string


def clean_input(input: str) -> List[str]:
    return re.sub(r"\s{3}", "-", input).strip().split("\n")


def create_location_lists(cleaned_input: str) -> List[List]:
    left_locations = []
    right_locations = []

    for locations in cleaned_input:
        left, right = map(int, locations.split("-"))
        left_locations.append(left)
        right_locations.append(right)

    left_locations.sort()
    right_locations.sort()
    return left_locations, right_locations


def solve_part_one(left_locations: List, right_locations: List) -> int:
    total_distance = sum(
        abs(left - right) for left, right in zip(left_locations, right_locations)
    )
    print(f"Part one: {total_distance}")
    return total_distance


def solve_part_two(left_locations: List, right_locations: List) -> int:
    counts = Counter(right_locations)
    similarity_score = sum(location * counts[location] for location in left_locations)

    print(f"Part two {similarity_score}")
    return similarity_score


def main():
    input = read_puzzle_input_as_string(day=1)
    cleaned_input = clean_input(input)

    left_locations_list, right_locations_list = create_location_lists(cleaned_input)

    solve_part_one(left_locations_list, right_locations_list)
    solve_part_two(left_locations_list, right_locations_list)


if __name__ == "__main__":
    main()
