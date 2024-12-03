import re
from typing import List

from utils.helpers import read_puzzle_input


def get_valid_multiplier_pattern(cleaned_input: str) -> List:
    multiplier_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)", flags=re.MULTILINE)
    return multiplier_pattern.findall(cleaned_input)


def remove_disabled_instructions(cleaned_input: str) -> str:
    disabled_instructions_pattern = re.compile(
        r"(?:don't\(\))(.*?)(?:do\(\)|$)", flags=re.MULTILINE
    )
    return re.sub(disabled_instructions_pattern, "", cleaned_input)


def solve_part_one(cleaned_input: str) -> int:
    valid_multipliers = get_valid_multiplier_pattern(cleaned_input)
    return sum([int(a) * int(b) for a, b in valid_multipliers])


def solve_part_two(cleaned_input: str) -> int:
    enabled_instructions = remove_disabled_instructions(cleaned_input)
    return solve_part_one(enabled_instructions)


def main():
    input = read_puzzle_input("src/day3/puzzle_input.txt")
    cleaned_input = "".join(input.strip().splitlines())

    print(f"Part one: {solve_part_one(cleaned_input)}")
    print(f"Part two: {solve_part_two(cleaned_input)}")


if __name__ == "__main__":
    main()
