import itertools
import operator
from typing import Iterator, List

from utils.helpers import read_puzzle_input_as_string


def custom_concat_operator(a, b):
    return int(f"{a}{b}")


CALIBRATION_OPERATORS = {
    "+": operator.add,
    "*": operator.mul,
    "|": custom_concat_operator,
}


def get_calibration_result(nums, ops_iterator):
    num = nums[0]
    result = 0
    ops = next(ops_iterator)
    for i in range(len(nums) - 1):
        op = ops[i]
        result = CALIBRATION_OPERATORS[op](num, int(nums[i + 1]))
        # print(f"{num} {op} {int(nums[i + 1])} = {result}")
        num = result
    return result


def validate_calibration(
    ops_iterator: Iterator[str],
    calibration_value: int,
    calibration_nums: list[int],
    ops_count: int,
) -> bool:
    nums = len(calibration_nums)
    cycles = 1

    while cycles < ops_count ** (nums - 1):
        result = get_calibration_result(calibration_nums, ops_iterator)
        if result == calibration_value:
            return True
        cycles += 1
    return False


def solve_part_one(calibration_details: List[any]):
    visible_operators = "+*"
    result = 0
    for pairs in calibration_details:
        target = pairs[0]
        numbers = pairs[1]
        op_iterator = itertools.product(visible_operators, repeat=(len(numbers) - 1))
        if validate_calibration(op_iterator, target, numbers, len(visible_operators)):
            result += target
    return result


def solve_part_two(calibration_details: List[any]):
    visible_operators = "+*|"
    result = 0
    for pairs in calibration_details:
        target = pairs[0]
        numbers = pairs[1]
        op_iterator = itertools.product(visible_operators, repeat=(len(numbers) - 1))
        if validate_calibration(op_iterator, target, numbers, len(visible_operators)):
            result += target
    return result


def main():
    calibration_details = []
    input = read_puzzle_input_as_string(7, True)
    for line in input.splitlines():
        target, numbers = line.split(":")
        numbers = [int(num) for num in numbers.strip().split(" ")]
        calibration_details.append([int(target), numbers])
    part_one = solve_part_one(calibration_details)
    print(f"Part one: {part_one}")

    part_two = solve_part_two(calibration_details)
    print(f"Part two: {part_two}")


if __name__ == "__main__":
    main()
