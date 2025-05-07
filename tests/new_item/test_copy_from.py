import pytest
from tests.new_item.data import new_folder_name


@pytest.mark.parametrize("folder_name, expected_result", [
        (new_folder_name, [new_folder_name])
])
def test_copy_from_dropdown_text(new_item_page_for_copy, folder_name, expected_result):
    text = new_item_page_for_copy.enter_first_letter_in_copy_from(folder_name).get_dropdown_text()
    assert text == expected_result, f"Expected text '{expected_result}' NOT FOUND"
