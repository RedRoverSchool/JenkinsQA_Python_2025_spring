import pytest

from pages.new_item_page import NewItemPage
from tests.new_item.data import Copy


@pytest.mark.parametrize("item_name, expected_result", Copy.PARAMS)
def test_display_dropdown_text(prepare_page_for_copy, item_name, expected_result):
    """
    TC: 01.003.02 | New Item > Copy from > Display dynamic dropdown in the "Copy from"
    Link: https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/396
    TC: 01.003.11 | New Item > Copy from > Display dynamic dropdown in the "Copy from" lowercase character
    Link: https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/670
    TC: 01.003.03 | New Item > Copy from > Display the dynamic drop-down with the text "No items"
    Link: https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/441
    """

    dropdown_text = prepare_page_for_copy.enter_first_character_in_copy_from(item_name).get_dropdown_text()

    assert dropdown_text, "Dropdown list is empty"
    assert dropdown_text == expected_result, f"Expected text '{expected_result}' NOT FOUND"


def test_error_page_displays_header_and_message(new_item_page: NewItemPage, prepare_page_for_copy):
    """
    TC: 01.003.04 | New Item > Copy from > Display an error message "No such job: item name"
    Link: https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/444
    """

    error_page = prepare_page_for_copy.go_to_error_page_copy(Copy.COPY_NAME, Copy.NON_EXISTENT_FOLDER_NAME)

    assert error_page.get_header_error() == Copy.HEADER_ERROR, \
        f"Expected header '{Copy.HEADER_ERROR}' NOT FOUND"
    assert error_page.get_message_error() == Copy.MESSAGE_ERROR, \
        f"Expected message '{Copy.MESSAGE_ERROR}' NOT FOUND"
