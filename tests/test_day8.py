from day8.day8 import add_point, check_bounds, create_point_map, subtract_point


def test_create_point_map():
    data = ["a1b", "c2d", "3e4"]
    result = create_point_map(data)
    expected = {
        "a": [(0, 0)],
        "1": [(0, 1)],
        "b": [(0, 2)],
        "c": [(1, 0)],
        "2": [(1, 1)],
        "d": [(1, 2)],
        "3": [(2, 0)],
        "e": [(2, 1)],
        "4": [(2, 2)],
    }
    assert dict(result) == expected


def test_subtract_point():
    assert subtract_point((3, 4), (1, 2)) == (2, 2)
    assert subtract_point((0, 0), (0, 0)) == (0, 0)
    assert subtract_point((5, 3), (2, 6)) == (3, -3)


def test_add_point():
    assert add_point((1, 2), (3, 4)) == (4, 6)
    assert add_point((0, 0), (0, 0)) == (0, 0)
    assert add_point((5, 3), (-2, -1)) == (3, 2)


def test_check_bounds():
    bounds = (5, 5)
    assert check_bounds(bounds, (0, 0)) is True
    assert check_bounds(bounds, (4, 4)) is True
    assert check_bounds(bounds, (5, 5)) is False
    assert check_bounds(bounds, (-1, 3)) is False
    assert check_bounds(bounds, (3, -1)) is False
