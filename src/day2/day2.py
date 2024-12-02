from typing import List

from utils.helpers import read_puzzle_input


def extract_reports(report_data: str) -> List[int]:
    input_lines = report_data.strip().split("\n")
    return [[int(x) for x in report.split()] for report in input_lines]


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

    for i in range(len(report)):
        print(report)
        adjusted_report = report[:i] + report[i + 1 :]
        print(adjusted_report)
        if check_safety_level(adjusted_report):
            return True
    return False


def solve_part_one(reports: List[int]) -> int:
    safe_reports = sum([check_safety_level(report) for report in reports])
    print(f"Part one: {safe_reports}")
    return safe_reports


def solve_part_two(reports: List[int]) -> int:
    dampened_safe_reports = sum(
        [check_dampened_safety_level(report) for report in reports]
    )

    print(f"Part two: {dampened_safe_reports}")
    return dampened_safe_reports


def main():
    input = read_puzzle_input("src/day2/puzzle_input.txt")
    reports = extract_reports(input)

    solve_part_one(reports)
    solve_part_two(reports)


if __name__ == "__main__":
    main()
