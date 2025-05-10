import pytest

from pages.new_item_page import NewItemPage
from tests.new_item.data import (
    folder_name_to_copy,
    non_existent_folder_name,
    item_not_found_message,
    copy_name,
    header_error,
    message_error,
    error_page_title
)


@pytest.mark.parametrize("item_name, expected_result", [
    (folder_name_to_copy, [folder_name_to_copy]),
    (non_existent_folder_name, [item_not_found_message])
])
def test_display_dropdown_text(new_item_page_for_copy, item_name, expected_result):
    text = new_item_page_for_copy.enter_first_character_in_copy_from(item_name).get_dropdown_text()
    assert text == expected_result, f"Expected text '{expected_result}' NOT FOUND"

def test_redirect_to_error_page(new_item_page: NewItemPage):
    error_page = new_item_page.get_error_page_copy(folder_name_to_copy, copy_name, non_existent_folder_name)
    assert error_page.get_header_error() == header_error, f"Expected header '{header_error}' NOT FOUND"
    assert error_page.get_message_error() == message_error, f"Expected message '{message_error}' NOT FOUND"
    assert error_page.get_title() == error_page_title, f"Expected title '{error_page_title}' NOT FOUND"
