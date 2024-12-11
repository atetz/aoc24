from collections import deque

from utils.helpers import read_puzzle_input_as_int_matrix


def check_bounds(bounds, point):
    x = point[0]
    y = point[1]
    return x >= 0 and x < bounds[0] and y >= 0 and y < bounds[1]


def add_point(point_a, point_b):
    x = point_a[0] + point_b[0]
    y = point_a[1] + point_b[1]
    return (x, y)


def solve_part_one(matrix, rows, cols, directions, trail_heads):
    # bfs implementation
    total_summits = 0
    for point in trail_heads:
        queue = deque([point])
        visited = {point}
        head_summits = set()

        while len(queue) > 0:
            prev_x, prev_y = queue.popleft()
            for direction in directions.values():
                next_x, next_y = add_point((prev_x, prev_y), direction)
                if not check_bounds((rows, cols), (next_x, next_y)):
                    continue
                if matrix[next_x][next_y] != matrix[prev_x][prev_y] + 1:
                    continue
                if (next_x, next_y) in visited:
                    continue
                visited.add((next_x, next_y))
                if matrix[next_x][next_y] == 9:
                    head_summits.add((next_x, next_y))
                else:
                    queue.append((next_x, next_y))
        total_summits += len(head_summits)
    return total_summits


def solve_part_two(matrix, rows, cols, directions, trail_heads):
    # bfs implementation
    total = 0
    for point in trail_heads:
        queue = deque([point])
        visited = {point: 1}
        tracks = 0
        while len(queue) > 0:
            prev_x, prev_y = queue.popleft()
            if matrix[prev_x][prev_y] == 9:
                tracks += visited[(prev_x, prev_y)]
            for direction in directions.values():
                next_x, next_y = add_point((prev_x, prev_y), direction)
                if not check_bounds((rows, cols), (next_x, next_y)):
                    continue
                if matrix[next_x][next_y] != matrix[prev_x][prev_y] + 1:
                    continue
                if (next_x, next_y) in visited:
                    visited[(next_x, next_y)] += visited[(prev_x, prev_y)]
                    continue
                visited[(next_x, next_y)] = visited[(prev_x, prev_y)]
                queue.append((next_x, next_y))
        total += tracks
    return total


def main():
    matrix = read_puzzle_input_as_int_matrix(
        10,
    )

    directions = {
        "north": (-1, 0),
        "east": (0, 1),
        "south": (1, 0),
        "west": (0, -1),
    }

    rows = len(matrix)
    cols = len(matrix[0])

    trail_heads = [
        (row, col)
        for row in range(rows)
        for col in range(cols)
        if matrix[row][col] == 0
    ]

    print(solve_part_one(matrix, rows, cols, directions, trail_heads))
    print(solve_part_two(matrix, rows, cols, directions, trail_heads))


if __name__ == "__main__":
    main()
