from day12.day12 import (
    add_point,
    calc_fence_price_per_region,
    check_bounds,
    count_corners,
    create_plot_map,
    get_cluster_corners,
    get_region_clusters,
)

SAMPLE = [
    "RRRRIICCFF",
    "RRRRIICCCF",
    "VVRRRCCFFF",
    "VVRCCCJFFF",
    "VVVVCJJCFE",
    "VVIVCCJJEE",
    "VVIIICJJEE",
    "MIIIIIJJEE",
    "MIIISIJEEE",
    "MMMISSJEEE",
]

DIRECTIONS = {"north": (-1, 0), "east": (0, 1), "south": (1, 0), "west": (0, -1)}


def test_create_plot_map():
    coord_1 = (0, 4)
    expected_value_1 = "I"
    coord_2 = (7, 6)
    expected_value_2 = "J"

    plot_map = create_plot_map(SAMPLE)

    assert coord_1 in plot_map[expected_value_1]
    assert coord_2 in plot_map[expected_value_2]


def test_add_point():
    point_a = (1, 2)
    point_b = (3, 4)
    expected = (4, 6)
    assert add_point(point_a, point_b) == expected


def test_check_bounds():
    bounds = (10, 10)
    point_inside = (5, 5)
    point_outside = (11, 5)
    assert check_bounds(bounds, point_inside) is True
    assert check_bounds(bounds, point_outside) is False


def test_get_region_clusters():
    plot_map = create_plot_map(SAMPLE)
    rows = len(SAMPLE)
    cols = len(SAMPLE[0])
    region = "R"
    clusters, perimiters = get_region_clusters(plot_map, rows, cols, DIRECTIONS, region)
    assert len(clusters) > 0
    assert len(perimiters) > 0


def test_calc_fence_price_per_region():
    clusters = {"R1": [(0, 0), (0, 1)], "R2": [(1, 0), (1, 1)]}
    perimiters = {"R1": 4, "R2": 6}
    expected_price = (2 * 4) + (2 * 6)
    assert calc_fence_price_per_region(clusters, perimiters) == expected_price


def test_count_corners():
    fences = {
        "north": {(0, 1), (2, 4), (0, 0), (0, 3), (0, 2)},
        "west": {(1, 0), (3, 2), (2, 2), (0, 0)},
        "south": {(2, 4), (1, 1), (2, 3), (1, 0), (3, 2)},
        "east": {(3, 2), (0, 3), (1, 3), (2, 4)},
    }
    expected_corners = 10
    assert count_corners(fences) == expected_corners


def test_get_cluster_corners():
    plot_map = create_plot_map(SAMPLE)
    rows = len(SAMPLE)
    cols = len(SAMPLE[0])
    region = "R"
    clusters, perimiters = get_region_clusters(plot_map, rows, cols, DIRECTIONS, region)
    cluster_corners = get_cluster_corners(DIRECTIONS, clusters)
    assert cluster_corners["R1"] == 10
