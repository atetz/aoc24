"""
unpolished as i want to start day 5. But the gist is that I found another, cool way to query the matrix.
"""

from collections import defaultdict

SAMPLE = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

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

lines = SAMPLE.strip().splitlines()

char_matrix = defaultdict(set)
for row_id, row in enumerate(lines):
    for col_id, val in enumerate(row):
        char_matrix[val].add((row_id, col_id))
# add coordinates to key of char.

part1 = 0

for row_id, col_id in char_matrix["X"]:
    for direction, (dir_row, dir_col) in directions.items():
        for move, char in enumerate("MAS", 1):  # rest of the word, start at 1.
            if (
                row_id + (dir_row * move),
                col_id + (dir_col * move),
            ) not in char_matrix[char]:
                break
        else:
            part1 += 1
print(part1)


part2 = 0
center_coordinates = defaultdict(int)

for row_id, col_id in char_matrix["M"]:
    for direction, (dir_row, dir_col) in directions.items():
        for move, char in enumerate("AS", 1):  # rest of the word, start at 1.
            if "_" not in direction:
                break
            if (
                row_id + (dir_row * move),
                col_id + (dir_col * move),
            ) not in char_matrix[char]:
                break
        else:
            center_coordinate = row_id + 1 * dir_row, col_id + 1 * dir_col
            center_coordinates[center_coordinate] += 1
            part2 += 1

print(sum(count == 2 for count in center_coordinates.values()))
