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


def get_guard_distinct_steps(
    char_position_map: Dict[str, Set[Tuple[int, int]]],
    directions: Dict[str, str],
    right_turns: Dict[str, str],
) -> Set[Tuple[int, int]]:
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
    return distinct_steps


def move_in_bounds(
    position: Tuple[int, int], char_position_map: Dict[str, Set[Tuple[int, int]]]
) -> bool:
    if not any(position in positions for positions in char_position_map.values()):
        return False
    return True


def detect_loop(
    char_position_map: Dict[str, Set[Tuple[int, int]]],
    directions: Dict[str, str],
    right_turns: Dict[str, str],
) -> bool:
    distinct_steps = set()
    step_history = defaultdict(int)

    guard_direction = "north"
    guard_on_map = True

    map_path = char_position_map.get(".", None)
    obstacles = char_position_map.get("#", None)
    guard_start_position = next(iter(char_position_map.get("^")))
    guard_position = guard_start_position

    while guard_on_map:
        distinct_steps.add(guard_position)  # Always track distinct steps

        step_history_key = (guard_position, directions[guard_direction])
        if step_history.get(step_history_key, 0) == 1:
            return True
        if not step_history.get(step_history_key, False):
            step_history[step_history_key] = 1

        next_position = get_next_position(guard_position, directions[guard_direction])

        if not move_in_bounds(next_position, char_position_map):
            return False

        if next_position in map_path or next_position == guard_start_position:
            guard_position = next_position
        elif next_position in obstacles:
            guard_direction = right_turns[guard_direction]
            next_position = get_next_position(
                guard_position, directions[guard_direction]
            )

            if not move_in_bounds(next_position, char_position_map):
                return False

            if (
                next_position in char_position_map.get(".", None)
                or next_position == guard_start_position
            ):
                guard_position = next_position

        else:
            return False


def solve_part_two(
    char_position_map: Dict[str, Set[Tuple[int, int]]],
    directions: Dict[str, str],
    right_turns: Dict[str, str],
    guard_distinct_steps: Set[Tuple[int, int]],
) -> int:
    loops = 0
    for coord in guard_distinct_steps:
        char_position_map["."].discard(coord)
        char_position_map["#"].add(coord)

        if detect_loop(char_position_map, directions, right_turns):
            loops += 1

        char_position_map["#"].discard(coord)
        char_position_map["."].add(coord)

    return loops


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

    right_turns = {"north": "east", "east": "south", "south": "west", "west": "north"}

    char_position_map = read_puzzle_input_as_position_map(6)

    guard_distinct_steps = get_guard_distinct_steps(
        char_position_map, directions, right_turns
    )

    print(f"part one: {len(guard_distinct_steps)}")

    print(
        f"part two: {solve_part_two(char_position_map,directions,right_turns,guard_distinct_steps)}"
    )


if __name__ == "__main__":
    main()
