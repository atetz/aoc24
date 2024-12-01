import re
from collections import Counter
from typing import List

from utils.helpers import read_puzzle_input


def clean_input(input: str) -> List[str]:
    return re.sub(r"\s{3}", "-", input).strip().split("\n")


def create_location_lists(cleaned_input: str) -> List[List]:
    left_locations = []
    right_locations = []

    for locations in cleaned_input:
        seperator = "-"
        left_locations.append(int(locations[: locations.index(seperator)]))
        right_locations.append(int(locations[locations.index(seperator) + 1 :]))

        left_locations.sort()
        right_locations.sort()
    return left_locations, right_locations


def solve_part_one(left_locations: List, right_locations: List) -> int:
    total_distance = 0
    for i in range(len(left_locations)):
        left_location = left_locations[i]
        right_location = right_locations[i]
        if left_location > right_location:
            total_distance += left_location - right_location
        else:
            total_distance += right_location - left_location
    print(f"Part one: {total_distance}")
    return total_distance


def solve_part_two(left_locations: List, right_locations: List) -> int:
    similarity_score = 0
    counts = Counter(right_locations)

    for location in left_locations:
        similarity_score += location * counts[location]

    print(f"Part two {similarity_score}")
    return similarity_score


def main():
    input = read_puzzle_input("src/day1/puzzle_input.txt")
    cleaned_input = clean_input(input)

    left_locations_list, right_locations_list = create_location_lists(cleaned_input)

    solve_part_one(left_locations_list, right_locations_list)
    solve_part_two(left_locations_list, right_locations_list)


if __name__ == "__main__":
    main()
