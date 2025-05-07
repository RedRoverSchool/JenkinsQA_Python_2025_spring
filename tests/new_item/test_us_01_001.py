from pages.new_item_page import NewItemPage
from tests.new_item.data import expected_item_types
from tests.new_item.data import new_freestyle_project_name
from selenium.common.exceptions import TimeoutException


def test_new_item_page_accessibility(new_item_page: NewItemPage):
    expected_input_field_name = "Enter an item name"
    field_name = new_item_page.get_input_field_name()
    assert expected_input_field_name == field_name.text, f"field name is {field_name}, expected {expected_input_field_name}"

def test_list_of_available_items(new_item_page: NewItemPage):
    visible_elements = new_item_page.get_item_types_text()
    assert visible_elements == expected_item_types, 'Items do not match'

def test_ok_button(new_item_page: NewItemPage):
    try:
        new_item_page.get_button_status()
        assert False, "OK button is clickable, but it should not be."
    except TimeoutException:
        assert True

def test_newly_created_item_is_visible_on_the_dashboard(new_item_page: NewItemPage):
    all_items = new_item_page.create_new_freestyle_project(new_freestyle_project_name).go_to_the_main_page().get_item_list()
    assert len(all_items) == 1, f"expected 1, but {len(all_items)} projects are displayed"
