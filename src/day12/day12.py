from collections import defaultdict, deque
from typing import Dict, List, Tuple

from utils.helpers import read_puzzle_input_as_list


def create_plot_map(data: List[str]) -> Dict[str, List[Tuple[int, int]]]:
    point_map = defaultdict(list)
    for row_id, row in enumerate(data):
        for col_id, val in enumerate(row):
            if val.isalnum():
                point_map[val].append((row_id, col_id))
    return point_map


def add_point(point_a: Tuple[int, int], point_b: Tuple[int, int]) -> Tuple[int, int]:
    row = point_a[0] + point_b[0]
    col = point_a[1] + point_b[1]
    return (row, col)


def check_bounds(bounds: Tuple[int, int], point: Tuple[int, int]) -> bool:
    row = point[0]
    col = point[1]
    return row >= 0 and row < bounds[0] and col >= 0 and col < bounds[1]


def get_region_clusters(
    plot_map: Dict[str, List[Tuple[int, int]]],
    rows: int,
    cols: int,
    directions: Dict[str, Tuple[int, int]],
    region: str,
) -> Tuple[Dict[str, List[Tuple[int, int]]], Dict[str, int]]:
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
    return clusters, perimiters


def calc_fence_price_per_region(
    clusters: Dict[str, List[Tuple[int, int]]], perimiters: Dict[str, int]
) -> int:
    return sum(len(cluster) * perimiters[group] for group, cluster in clusters.items())


def count_corners(fences: Dict[str, set[Tuple[int, int]]]) -> int:
    corners = 0
    for row, col in fences["north"]:
        if (row, col) in fences["west"]:
            corners += 1
        if (row, col) in fences["east"]:
            corners += 1
        if (row - 1, col - 1) in fences["east"] and (row, col) not in fences["west"]:
            corners += 1
        if (row - 1, col + 1) in fences["west"] and (row, col) not in fences["east"]:
            corners += 1

    for row, col in fences["south"]:
        if (row, col) in fences["west"]:
            corners += 1
        if (row, col) in fences["east"]:
            corners += 1
        if (row + 1, col - 1) in fences["east"] and (row, col) not in fences["west"]:
            corners += 1
        if (row + 1, col + 1) in fences["west"] and (row, col) not in fences["east"]:
            corners += 1
    return corners


def get_cluster_corners(
    directions: Dict[str, Tuple[int, int]], all_clusters: Dict[str, Tuple[int, int]]
) -> Dict[str, int]:
    cluster_corners = defaultdict(int)
    for cluster, grid in all_clusters.items():
        fences = defaultdict(set)
        for point in grid:
            for direction, move in directions.items():
                if add_point(point, move) not in grid:
                    fences[direction].add(point)
        cluster_corners[cluster] = count_corners(fences)
    return cluster_corners


def main() -> None:
    directions = {"north": (-1, 0), "east": (0, 1), "south": (1, 0), "west": (0, -1)}

    data = read_puzzle_input_as_list(12, True)
    rows = len(data)
    cols = len(data[0])
    plot_map = create_plot_map(data)

    all_clusters = {}
    all_perimiters = {}
    for region in plot_map.keys():
        clusters, perimiters = get_region_clusters(
            plot_map, rows, cols, directions, region
        )

        all_clusters.update(clusters)
        all_perimiters.update(perimiters)

    print(f"Part one: {calc_fence_price_per_region(all_clusters, all_perimiters)}")

    sides = get_cluster_corners(directions, all_clusters)

    print(f"Part two: {calc_fence_price_per_region(all_clusters, sides)}")


if __name__ == "__main__":
    main()
