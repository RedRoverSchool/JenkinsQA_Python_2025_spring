from pages.new_item_page import NewItemPage
from tests.new_item.data import new_freestyle_project_name


def test_copy_from_option_exists(new_item_page: NewItemPage):
    new_item_page.create_new_freestyle_project(new_freestyle_project_name).go_to_the_main_page()
    new_item_page.click_new_item_button()
    assert new_item_page.copy_from_option_is_displayed()