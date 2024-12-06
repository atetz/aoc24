from collections import defaultdict
from typing import Dict, List, Optional, Set, Tuple

FILE_BASE_PATH = "src/day"


def get_filename(day: int, sample: bool) -> str:
    if not isinstance(day, int) or not (1 <= day <= 25):
        raise ValueError("Day must be an integer between 1 and 25.")
    base = f"{FILE_BASE_PATH}{day}/"
    if not sample:
        return base + "puzzle_input.txt"
    return base + "sample_puzzle_input.txt"


def read_puzzle_input_as_list(day: int, sample: Optional[bool] = False) -> List[str]:
    with open(get_filename(day, sample)) as f:
        return f.read().splitlines()


def read_puzzle_input_as_string(day: int, sample: Optional[bool] = False) -> str:
    with open(get_filename(day, sample)) as f:
        return f.read()


def read_puzzle_input_as_single_line_string(
    day: int, sample: Optional[bool] = False
) -> str:
    with open(get_filename(day, sample)) as f:
        return "".join(f.read().splitlines())


def read_puzzle_input_as_char_matrix(
    day: int, sample: Optional[bool] = False
) -> List[str]:
    with open(get_filename(day, sample)) as f:
        lines = f.read().splitlines()
        return [[char for char in line] for line in lines]


def read_puzzle_input_as_position_map(
    day: int,
    sample: Optional[bool] = False,
) -> Dict[str, Set[Tuple[int, int]]]:
    data = read_puzzle_input_as_list(day, sample)
    char_position_map = defaultdict(set)

    for row_id, row in enumerate(data):
        for col_id, val in enumerate(row):
            char_position_map[val].add((row_id, col_id))

    return char_position_map
