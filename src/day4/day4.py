from collections import defaultdict
from typing import Dict, List, Tuple

from utils.helpers import read_puzzle_input_as_char_matrix


def validate_move(rows, cols, start_row, start_col, dir_row, dir_col, step):
    end_row = start_row + dir_row * step
    end_col = start_col + dir_col * step
    return 0 <= end_row < rows and 0 <= end_col < cols


def validate_word(target_word: str, letters: List[str]) -> bool:
    if not isinstance(letters, list) or not all(
        isinstance(letter, str) for letter in letters
    ):
        raise TypeError("Expected `letters` to be a list of strings.")
    return target_word == "".join(letters)


def solve_part_one(
    input_matrix: List[List[str]], directions: Dict[str, Tuple], target_word: str
) -> int:
    rows, cols = (len(input_matrix), len(input_matrix[0]))
    step = len(target_word) - 1
    word_count = 0

    for row in range(rows):
        for col in range(cols):
            if input_matrix[row][col] == target_word[0]:
                for direction, (dir_row, dir_col) in directions.items():
                    if validate_move(rows, cols, row, col, dir_row, dir_col, step):
                        result = [
                            input_matrix[row + i * dir_row][col + i * dir_col]
                            for i in range(len(target_word))
                        ]
                        if validate_word(target_word, result):
                            word_count += 1
    return word_count


def solve_part_two(
    input_matrix: List[List[str]], directions: Dict[str, Tuple], target_word: str
) -> int:
    rows, cols = (len(input_matrix), len(input_matrix[0]))
    center_coordinates = defaultdict(int)
    step = len(target_word) - 1

    for row in range(rows):
        for col in range(cols):
            if input_matrix[row][col] == target_word[0]:
                for direction, (dir_row, dir_col) in directions.items():
                    if "_" in direction:  # only diagonal directions
                        if validate_move(rows, cols, row, col, dir_row, dir_col, step):
                            result = [
                                input_matrix[row + i * dir_row][col + i * dir_col]
                                for i in range(len(target_word))
                            ]
                            if validate_word(target_word, result):
                                # save the center coordinate to find out what matches share same center.
                                center_coordinate = row + 1 * dir_row, col + 1 * dir_col
                                center_coordinates[center_coordinate] += 1

    return sum(count == 2 for count in center_coordinates.values())


def main() -> None:
    input_matrix = read_puzzle_input_as_char_matrix(4)

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

    part_one = solve_part_one(input_matrix, directions, "XMAS")
    print(f"Part one: {part_one}")

    part_two = solve_part_two(input_matrix, directions, "MAS")
    print(f"Part two: {part_two}")


if __name__ == "__main__":
    main()
