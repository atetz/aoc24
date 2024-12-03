from day3.day3 import get_valid_multiplier_pattern, remove_disabled_instructions

SAMPLE_DATA_P1 = (
    "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
)
SAMPLE_DATA_P2 = (
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
)


def test_should_have_no_mulipliers():
    input_string = "mul[3,7]mul(32,64]mul(0)"
    result = get_valid_multiplier_pattern(input_string)
    assert result == [], f"result {result} ivalid! Should return empty list! []"


def test_should_have_4_multipliers():
    input_string = (
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    )
    result = get_valid_multiplier_pattern(input_string)
    result_length = len(result)
    assert (
        result_length == 4
    ), f"Result list should have 4 elements. Found {result_length}"

    tuple_1 = result[0]
    tuple_3 = result[2]
    expected_value_tuple_1 = ("2", "4")
    expected_value_tuple_3 = ("11", "8")
    assert (
        tuple_1 == expected_value_tuple_1
    ), f"The first tuple should contain {expected_value_tuple_1} not {tuple_1} "
    assert (
        tuple_3 == expected_value_tuple_3
    ), f"The first tuple should contain {expected_value_tuple_3} not {tuple_3} "


def test_should_return_enabled_instructions():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    expected_result = "xmul(2,4)&mul[3,7]!^?mul(8,5))"
    result = remove_disabled_instructions(input)
    assert (
        expected_result == result
    ), f"result should be '{expected_result}' not '{result}' "


def test_should_not_return_usefull_instructions():
    input = "^xmul(2,4]don't()&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undon't()?mul(8,5))"
    expected_result = "^xmul(2,4]"
    result = remove_disabled_instructions(input)

    assert (
        expected_result == result
    ), f"result should be '{expected_result}' not '{result}' "


def test_return_should_equal_input_instructions():
    input = "[how()who(703,56)'$mul(472,810)from()->>}mul(5,623)what()}from(904,521)](who()<mul(476,844)!$ [mul(627,570)(}select()"
    result = remove_disabled_instructions(input)
    assert input == result, f"result should be equal to the input '{input}'"
