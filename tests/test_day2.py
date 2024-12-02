from typing import List

from day2.day2 import (
    check_dampened_safety_level,
    check_safety_difference,
    check_safety_level,
    extract_reports,
    solve_part_one,
    solve_part_two,
)

SAMPLE_DATA = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

REPORTS = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]


def check_list_of_int(input_list: any) -> bool:
    return isinstance(input_list, List) and all(
        isinstance(item, int) for item in input_list
    )


def test_extract_reports():
    reports = extract_reports(SAMPLE_DATA)
    for report in reports:
        assert check_list_of_int(report)


def test_safe_difference():
    safe_difference = check_safety_difference(2, 5)
    assert safe_difference, "difference of 3 between 2 and 5 should be safe!"


def test_unsafe_difference():
    unsafe_difference = check_safety_difference(2, 10)
    assert not unsafe_difference, "difference of 8 between 2,10 should be unsafe!"


def test_safe_decreasing_report():
    safe_decreasing_report = [7, 6, 4, 2, 1]
    assert check_safety_level(
        safe_decreasing_report
    ), "should be safe because the levels are all decreasing by 1 or 2."


def test_unsafe_increasing_report():
    unsafe_increasing_report = [1, 2, 7, 8, 9]
    assert not check_safety_level(
        unsafe_increasing_report
    ), "should be unsafe because 2 7 is an increase of 5."


def test_unsafe_decreasing_report():
    unsafe_decreasing_report = [9, 7, 6, 2, 1]
    assert not check_safety_level(
        unsafe_decreasing_report
    ), "should be unsafe because 6 2 is a decrease of 4."


def test_unsafe_increasing_and_decreasing_report():
    unsafe_increasing_and_decreasing_report = [1, 3, 2, 4, 5]
    assert not check_safety_level(
        unsafe_increasing_and_decreasing_report
    ), "should be unsafe because 1 3 is increasing but 3 2 is decreasing."


def test_unsafe_none_difference_report():
    unsafe_none_difference_report = [8, 6, 4, 4, 1]
    assert not check_safety_level(
        unsafe_none_difference_report
    ), "should be unsafe because 4 4 is neither an increase or a decrease."


def test_safe_increasing_report():
    safe_increasing_report = [1, 3, 6, 7, 9]
    assert check_safety_level(
        safe_increasing_report
    ), "should be safe because the levels are all increasing by 1, 2, or 3."


def test_safe_dampened_report_without_removing():
    safe_dampened_report = [7, 6, 4, 2, 1]
    assert check_dampened_safety_level(
        safe_dampened_report
    ), "should be safe without removing any level"


def test_unsafe_dampened_report_regardless_of_removal():
    unsafe_dampened_report = [1, 2, 7, 8, 9]
    assert not check_dampened_safety_level(
        unsafe_dampened_report
    ), "should be unsafe regardless of which level is removed."


def test_safe_dampened_report_by_removal():
    safe_dampened_report = [1, 3, 2, 4, 5]
    assert check_dampened_safety_level(
        safe_dampened_report
    ), " Should be safe by removing the second level, 3"


def test_solve_part_one():
    result = solve_part_one(REPORTS)
    assert result == 2, f"Part one should return 2, not {result}"


def test_solve_part_two():
    result = solve_part_two(REPORTS)
    assert result == 4, f"Part two should return 4, not {result}"
