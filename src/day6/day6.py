from collections import defaultdict
from typing import Dict, List, Set, Tuple

from utils.helpers import read_puzzle_input_as_position_map


def build_char_position_map(
    data: List[str],
) -> Dict[str, Set[Tuple[int, int]]]:
    char_position_map = defaultdict(set)

    for row_id, row in enumerate(data):
        for col_id, val in enumerate(row):
            char_position_map[val].add((row_id, col_id))

    return char_position_map


def get_next_position(
    position: Tuple[int, int],
    direction: Tuple[int, int],
) -> Tuple[int, int]:
    if not isinstance(position, Tuple) or not isinstance(direction, Tuple):
        return None
    return tuple(pos + (1 * dir) for pos, dir in zip(position, direction))


def solve_part_one(
    char_position_map: Dict[str, Set[Tuple[int, int]]],
    directions: Dict[str, str],
    right_turns: Dict[str, str],
):
    distinct_steps = set()

    guard_position = next(iter(char_position_map.get("^")))
    guard_direction = "north"

    guard_on_map = True
    while guard_on_map:
        distinct_steps.add(guard_position)

        next_position = get_next_position(guard_position, directions[guard_direction])

        if next_position in char_position_map.get(
            "^", None
        ) or next_position in char_position_map.get(".", None):
            guard_position = next_position
        elif next_position in char_position_map.get("#", None):
            guard_direction = right_turns[guard_direction]
            guard_position = get_next_position(
                guard_position, directions[guard_direction]
            )
        else:
            guard_on_map = False
    return len(distinct_steps)


def main():
    directions = {
        "north": (-1, 0),
        "north_east": (-1, 1),
        "east": (0, 1),
        "south_east": (1, 1),
        "south": (1, 0),
        "south_west": (1, -1),
        "west": (0, -1),
        "north_west": (-1, -1),
    }

    test_pos = (1, 1)
    for direction_name, direction_offset in directions.items():
        # Expected position after moving in the current direction
        expected_nex_positions = {
            "north": (0, 1),
            "north_east": (0, 2),
            "east": (1, 2),
            "south_east": (2, 2),
            "south": (2, 1),
            "south_west": (2, 0),
            "west": (1, 0),
            "north_west": (0, 0),
        }

        for direction, move in directions.items():
            # Assert that the function gives the correct result
            next_position = get_next_position(test_pos, move)
            assert (
                next_position == expected_nex_positions[direction]
            ), f"Test failed for direction: {direction_name}, Expected: {expected_nex_positions[direction]}, Got: {next_position}"

    right_turns = {"north": "east", "east": "south", "south": "west", "west": "north"}

    char_position_map = read_puzzle_input_as_position_map(6, True)

    print(f"part one: {solve_part_one(char_position_map,directions,right_turns)}")


if __name__ == "__main__":
    main()
