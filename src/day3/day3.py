import re
from typing import List

from utils.helpers import read_puzzle_input


def get_valid_multiplier_pattern(cleaned_input: str) -> List:
    multiplier_pattern = re.compile(
        "mul\\((\\d{1,3}),(\\d{1,3})\\)", flags=re.MULTILINE
    )
    return multiplier_pattern.findall(cleaned_input)


def remove_disabled_instructions(cleaned_input: str) -> str:
    disabled_instructions_pattern = re.compile(
        "(?:don't\\(\\))(.*?)(?:do\\(\\)|$)", flags=re.MULTILINE
    )

    return re.sub(disabled_instructions_pattern, "", cleaned_input)


def solve_part_one(cleaned_input: str) -> int:
    valid_multipliers = get_valid_multiplier_pattern(cleaned_input)
    result = sum([int(a) * int(b) for a, b in valid_multipliers])
    print(f"Part one: {result}")
    return result


def solve_part_two(cleaned_input: str) -> int:
    enabled_instructions = remove_disabled_instructions(cleaned_input)
    result = sum(
        [int(a) * int(b) for a, b in get_valid_multiplier_pattern(enabled_instructions)]
    )
    print(f"Part two: {result}")
    return result


def main():
    input = read_puzzle_input("src/day3/puzzle_input.txt")
    cleaned_input = "".join(input.strip().splitlines())

    solve_part_one(cleaned_input)
    solve_part_two(cleaned_input)


if __name__ == "__main__":
    main()
