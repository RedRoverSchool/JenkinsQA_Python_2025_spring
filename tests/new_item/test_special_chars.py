from pages.new_item_page import NewItemPage
from tests.new_item.data import special_chars


def test_special_chars_validation_error(new_item_page: NewItemPage):
    page = new_item_page
    any_errors_before = page.get_any_validation_errors()

    assert not any_errors_before, (
        "Validation error appears even before interacting with the Item name field"
    )

    for char in special_chars:
        page.enter_text(page.Locators.ITEM_NAME, char)
        page.click_element(page.Locators.PAGE_NAME)
        any_errors_after = page.get_any_validation_errors()

        assert len(any_errors_after) == 1, (
            f"Unexpected number of errors detected after inserting {char}"
        )

        expected_error_text = f"» ‘{char}’ is an unsafe character"
        page.wait_text_to_be_present(
            page.Locators.ANY_ENABLED_ERROR,
            expected_error_text,
        )
        page.find_element(*page.Locators.ITEM_NAME).clear()
