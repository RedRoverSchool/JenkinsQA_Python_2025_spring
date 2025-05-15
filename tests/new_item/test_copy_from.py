import pytest

from pages.new_item_page import NewItemPage
from tests.new_item.data import Copy


@pytest.mark.parametrize("item_name, expected_result", Copy.PARAMS)
def test_display_dropdown_text(prepare_page_for_copy, item_name, expected_result):
    text = prepare_page_for_copy.enter_first_character_in_copy_from(item_name).get_dropdown_text()

    assert text == expected_result, f"Expected text '{expected_result}' NOT FOUND"


def test_display_error_page_content(new_item_page: NewItemPage, prepare_page_for_copy):
    error_page = prepare_page_for_copy.go_to_error_page_copy(Copy.COPY_NAME, Copy.NON_EXISTENT_FOLDER_NAME)

    assert error_page.get_header_error() == Copy.HEADER_ERROR, \
        f"Expected header '{Copy.HEADER_ERROR}' NOT FOUND"
    assert error_page.get_message_error() == Copy.MESSAGE_ERROR, \
        f"Expected message '{Copy.MESSAGE_ERROR}' NOT FOUND"
