from pages.new_item_page import NewItemPage
from tests.new_item.data import special_chars


def test_special_chars_validation_error(new_item_page: NewItemPage):
    page = new_item_page
    any_errors_before = page.get_any_validation_errors()

    assert not any_errors_before, (
        "Validation error appears even before interacting with the Item name field"
    )

    for char in special_chars:
        page.enter_text_in_field(page.Locator.ITEM_NAME, char)
        page.click_element(page.Locator.PAGE_NAME)
        any_errors_after = page.get_any_validation_errors()

        assert len(any_errors_after) == 1, (
            f"Unexpected number of errors detected after inserting {char}"
        )

        expected_error_text = f"» ‘{char}’ is an unsafe character"
        page.wait_text_to_be_present(
            page.Locator.ANY_ENABLED_ERROR,
            expected_error_text,
            message=f"Expected error message: {expected_error_text} was not found. Another message: {page.find_element(*page.Locator.ANY_ENABLED_ERROR).text} was displayed instead",
        )
        page.find_element(*page.Locator.ITEM_NAME).clear()
