from pages.new_item_page import NewItemPage
from tests.new_item.data import expected_item_types


def test_list_of_item_types_is_displayed(new_item_page: NewItemPage):
    actual_item_types = new_item_page.get_item_types_text()

    assert actual_item_types == expected_item_types, f"Expected: {expected_item_types}, but got: {actual_item_types}"
