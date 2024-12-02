from typing import List

from utils.helpers import read_puzzle_input

SAMPLE_DATA = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def check_safety_difference(a: int, b: int) -> bool:
    return abs(b - a) <= 3


def check_safety_level(report: List[int]) -> bool:
    increasing_condition = all(
        a < b and check_safety_difference(a, b) for a, b in zip(report, report[1:])
    )
    decreasing_condition = all(
        a > b and check_safety_difference(a, b) for a, b in zip(report, report[1:])
    )
    return increasing_condition or decreasing_condition


def check_dampened_safety_level(report: List[int]) -> bool:
    if check_safety_level(report):
        return True
    else:
        i = 0
        for value in report:
            adjusted_report = report.copy()
            adjusted_report.pop(i)
            if check_safety_level(adjusted_report):
                return True
            else:
                i += 1
        return False


def main():
    input = read_puzzle_input("src/day2/puzzle_input.txt")
    # input = SAMPLE_DATA
    input_lines = input.strip().split("\n")
    reports = [[int(x) for x in report.split()] for report in input_lines]

    # safe because difference is 3
    safe_difference = check_safety_difference(2, 5)
    assert safe_difference

    # safe because difference is 8
    unsafe_difference = check_safety_difference(2, 10)
    assert not unsafe_difference

    # Safe because the levels are all decreasing by 1 or 2.
    safe_decreasing_sample_report = [7, 6, 4, 2, 1]
    assert check_safety_level(safe_decreasing_sample_report)

    # Unsafe because 2 7 is an increase of 5.
    unsafe_increasing_sample_report = [1, 2, 7, 8, 9]
    assert not check_safety_level(unsafe_increasing_sample_report)

    # Unsafe because 6 2 is a decrease of 4.
    unsafe_decreasing_sample_report = [9, 7, 6, 2, 1]
    assert not check_safety_level(unsafe_decreasing_sample_report)

    # Unsafe because 1 3 is increasing but 3 2 is decreasing.
    unsafe_increasing_and_decreasing_sample_report = [1, 3, 2, 4, 5]
    assert not check_safety_level(unsafe_increasing_and_decreasing_sample_report)

    # Unsafe because 4 4 is neither an increase or a decrease.
    unsafe_none_difference_sample_report = [8, 6, 4, 4, 1]
    assert not check_safety_level(unsafe_none_difference_sample_report)

    # Safe because the levels are all increasing by 1, 2, or 3.
    safe_increasing_report = [1, 3, 6, 7, 9]
    assert check_safety_level(safe_increasing_report)

    safe_reports = sum([check_safety_level(report) for report in reports])

    # part one 379
    print(safe_reports)

    # Safe without removing any level
    safe_dampened_sample_report = [7, 6, 4, 2, 1]
    assert check_dampened_safety_level(safe_dampened_sample_report)

    # Unsafe regardless of which level is removed.
    unsafe_dampened_sample_report = [1, 2, 7, 8, 9]
    assert not check_dampened_safety_level(unsafe_dampened_sample_report)

    # Unsafe regardless of which level is removed.
    unsafe_dampened_sample_report = [9, 7, 6, 2, 1]
    assert not check_dampened_safety_level(unsafe_dampened_sample_report)

    # Safe by removing the second level, 3.
    unsafe_increasing_and_decreasing_sample_report = [1, 3, 2, 4, 5]
    assert check_dampened_safety_level(unsafe_increasing_and_decreasing_sample_report)

    # Safe by removing the third level, 4.
    unsafe_none_difference_sample_report = [8, 6, 4, 4, 1]
    assert check_dampened_safety_level(unsafe_none_difference_sample_report)

    # Safe without removing any level.
    safe_increasing_report = [1, 3, 6, 7, 9]
    assert check_dampened_safety_level(safe_increasing_report)

    dampened_safe_reports = sum(
        [check_dampened_safety_level(report) for report in reports]
    )

    print(dampened_safe_reports)


if __name__ == "__main__":
    main()
