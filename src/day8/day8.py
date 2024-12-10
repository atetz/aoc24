from collections import defaultdict

from utils.helpers import read_puzzle_input_as_list


def create_point_map(data):
    point_map = defaultdict(list)
    for row_id, row in enumerate(data):
        for col_id, val in enumerate(row):
            if val.isalnum():
                point_map[val].append((row_id, col_id))
    return point_map


def subtract_point(point_a, point_b):
    x = point_a[0] - point_b[0]
    y = point_a[1] - point_b[1]
    return (x, y)


def add_point(point_a, point_b):
    x = point_a[0] + point_b[0]
    y = point_a[1] + point_b[1]
    return (x, y)


def check_bounds(bounds, point):
    x = point[0]
    y = point[1]
    return x >= 0 and x < bounds[0] and y >= 0 and y < bounds[1]


def cast_frequency(bounds, antinodes, antinode, move, direction):
    casting = True
    while casting:
        if direction == "backward":
            antinode = subtract_point(antinode, move)
        if direction == "forward":
            antinode = add_point(antinode, move)
        if check_bounds(bounds, antinode):
            antinodes.add(antinode)
        else:
            casting = False


def find_antinodes(bounds, point_map, part_two=False):
    antinodes = set()
    for antenna, points in point_map.items():
        for i, primary in enumerate(points):
            for secondary in points[i + 1 :]:
                move_to_secondary = subtract_point(secondary, primary)
                rear_antinode = subtract_point(primary, move_to_secondary)
                forward_antinode = add_point(secondary, move_to_secondary)
                if check_bounds(bounds, rear_antinode):
                    antinodes.add(rear_antinode)
                if check_bounds(bounds, forward_antinode):
                    antinodes.add(forward_antinode)
                if part_two:
                    antinodes.add(primary)
                    antinodes.add(secondary)
                    cast_frequency(
                        bounds,
                        antinodes,
                        rear_antinode,
                        move_to_secondary,
                        "backward",
                    )
                    cast_frequency(
                        bounds,
                        antinodes,
                        forward_antinode,
                        move_to_secondary,
                        "forward",
                    )

    return antinodes


def main():
    data = read_puzzle_input_as_list(8)

    bounds = (len(data), len(data[0]))
    point_map = create_point_map(data)

    print(f"part one: {len(find_antinodes(bounds, point_map))}")
    print(f"part two: {len(find_antinodes(bounds, point_map,True))}")


if __name__ == "__main__":
    main()
