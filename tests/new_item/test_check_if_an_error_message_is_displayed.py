from pages.new_item_page import NewItemPage
from tests.new_item.data import expected_error

def test_check_if_an_error_message_is_displayed(new_item_page: NewItemPage):
    actual_error = new_item_page.get_error_message()
    assert actual_error == expected_error, \
        f"Expected error message '{expected_error}', but got '{actual_error}'"




