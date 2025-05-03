from pages.new_item_page import NewItemPage
from tests.new_item.data import new_folder_name

def test_check_create_new_item(new_item_page: NewItemPage):
    folder_config_page = new_item_page.create_new_folder(new_folder_name)
    folder_config_page.wait_for_url()
    items = folder_config_page.go_to_the_main_page().get_item_list()
    assert items == [new_folder_name], f"Folder '{new_folder_name}' NOT FOUND"