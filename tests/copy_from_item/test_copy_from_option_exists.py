from pages.new_item_page import NewItemPage
from pages.main_page import MainPage
from tests.new_item.data import new_freestyle_project_name


def test_copy_from_option_exists(new_item_page: NewItemPage , main_page: MainPage):
    new_item_page.create_new_freestyle_project(new_freestyle_project_name).header.go_to_the_main_page()
    main_page.go_to_new_item_page()
    assert new_item_page.copy_from_option_is_displayed()