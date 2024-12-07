from day6.day6 import get_next_position

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


def test_navigation():
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
