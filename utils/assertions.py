import pytest_check as check


def soft_assert_list_length_equal(actual: list, expected: list):
    check.equal(len(actual), len(expected))


def soft_assert_lists_equal_by_index(actual: list, expected: list):
    for i in range(min(len(actual), len(expected))):
        check.equal(actual[i], expected[i])


def soft_assert_all_elements_true(actual: list):
    for value in actual:
        check.is_true(value)


def soft_assert_text_equal(actual: str, expected: str):
    check.equal(actual, expected)
