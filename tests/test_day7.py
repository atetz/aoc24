import itertools

from day7.day7 import validate_calibration

# def test_get_calibration_result():
#     operations_iterator = itertools.cycle("+*")
#     nums = [10, 19]
#     first_expected_result = 29
#     second_expected_result = 190
#     assert get_calibration_result(nums, operations_iterator) == first_expected_result
#     assert get_calibration_result(nums, operations_iterator) == second_expected_result


def test_succesfull_3n_calibration():
    calibration_value = 3267
    nums = [81, 40, 27]
    operations_iterator = itertools.product("+*", repeat=len(nums) - 1)
    assert validate_calibration(operations_iterator, calibration_value, nums, 2)


def test_succesfull_4n_calibration():
    calibration_value = 292
    nums = [11, 6, 16, 20]
    operations_iterator = itertools.product("+*", repeat=len(nums) - 1)
    assert validate_calibration(operations_iterator, calibration_value, nums, 2)


def test_unsuccesfull_4n_calibration():
    calibration_value = 7290
    nums = [6, 8, 6, 15]
    operations_iterator = itertools.product("+*", repeat=len(nums) - 1)
    assert not validate_calibration(operations_iterator, calibration_value, nums, 2)


def test_succesfull_5n_calibration():
    calibration_value = 270336
    nums = [2, 4, 8, 16, 32, 64, 128]
    operations_iterator = itertools.product("+*", repeat=len(nums) - 1)
    assert validate_calibration(operations_iterator, calibration_value, nums, 2)


def test_succesfull_7n_calibration():
    calibration_value = 261120
    nums = [2, 4, 8, 16, 32, 64, 128, 256, 512]
    operations_iterator = itertools.product("+*", repeat=len(nums) - 1)
    assert validate_calibration(operations_iterator, calibration_value, nums, 2)
