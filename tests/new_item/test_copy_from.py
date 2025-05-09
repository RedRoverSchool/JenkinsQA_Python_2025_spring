import pytest

from pages.new_item_page import NewItemPage
from tests.new_item.data import (
    new_folder_name,
    invalid_folder_name,
    copy_from_placeholder,
    new_folder_copy,
    header_error,
    message_error
)


@pytest.mark.parametrize("folder_name, expected_result", [
    (new_folder_name, [new_folder_name]),
    (invalid_folder_name, [copy_from_placeholder])
])
def test_display_dropdown_text(new_item_page_for_copy, folder_name, expected_result):
    text = new_item_page_for_copy.enter_first_letter_in_copy_from(folder_name).get_dropdown_text()
    assert text == expected_result, f"Expected text '{expected_result}' NOT FOUND"

def test_error_message(new_item_page: NewItemPage):
    error_page = new_item_page.get_error_page_copy(new_folder_name, new_folder_copy, invalid_folder_name)
    assert error_page.get_header_error() == header_error, f"Expected header '{header_error}' NOT FOUND"
    assert error_page.get_message_error() == message_error, f"Expected message '{message_error}' NOT FOUND"
