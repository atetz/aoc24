from collections import defaultdict, deque

from utils.helpers import read_puzzle_input_as_list


def create_plot_map(data):
    point_map = defaultdict(list)
    for row_id, row in enumerate(data):
        for col_id, val in enumerate(row):
            if val.isalnum():
                point_map[val].append((row_id, col_id))
    return point_map


def add_point(point_a, point_b):
    x = point_a[0] + point_b[0]
    y = point_a[1] + point_b[1]
    return (x, y)


def check_bounds(bounds, point):
    x = point[0]
    y = point[1]
    return x >= 0 and x < bounds[0] and y >= 0 and y < bounds[1]


def calc_fence_price_per_region(plot_map, rows, cols, directions, region):
    # bfs implementation
    # this function does more than name, refactor tomorrow.
    group = 0
    visited = set()
    clusters = defaultdict(list)
    perimiters = defaultdict(int)
    for point in plot_map[region]:
        if point not in visited:
            group += 1
            queue = deque([point])
            clusters[f"{region}{group}"].append(point)
            visited.add(point)
            while len(queue) > 0:
                prev_x, prev_y = queue.popleft()
                for direction in directions.values():
                    next_x, next_y = add_point((prev_x, prev_y), direction)
                    if not check_bounds((rows, cols), (next_x, next_y)):
                        perimiters[f"{region}{group}"] += 1
                        continue
                    if (next_x, next_y) not in plot_map[region]:
                        perimiters[f"{region}{group}"] += 1
                        continue
                    if (next_x, next_y) in visited:
                        continue
                    visited.add((next_x, next_y))
                    clusters[f"{region}{group}"].append((next_x, next_y))
                    queue.append((next_x, next_y))
    return sum(len(cluster) * perimiters[group] for group, cluster in clusters.items())


def main():
    directions = {
        "north": (-1, 0),
        "east": (0, 1),
        "south": (1, 0),
        "west": (0, -1),
    }

    data = read_puzzle_input_as_list(12)
    rows = len(data)
    cols = len(data[0])
    plot_map = create_plot_map(data)

    print(
        sum(
            calc_fence_price_per_region(plot_map, rows, cols, directions, region)
            for region in plot_map.keys()
        )
    )


if __name__ == "__main__":
    main()
