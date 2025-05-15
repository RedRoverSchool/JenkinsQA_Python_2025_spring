from pages.new_item_page import NewItemPage
from tests.new_item.data import new_folder_name


def test_create_new_folder(new_item_page: NewItemPage):
    folder_conf_page = new_item_page.create_new_folder(new_folder_name)
    items = folder_conf_page.header.go_to_the_main_page().get_item_list()
    assert items == [new_folder_name], f"Folder '{new_folder_name}' NOT FOUND"
