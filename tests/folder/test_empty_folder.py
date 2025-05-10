from pages.new_item_page import NewItemPage
from tests.folder.data import folder_name, empty_state_message


def test_empty_folder_message(new_item_page: NewItemPage):
    folder_config_page = new_item_page.create_new_folder(folder_name)
    message = folder_config_page.header.go_to_the_main_page().go_to_folder_page(folder_name).get_empty_state_message()
    assert message == empty_state_message, f"Expected message not found. Got: '{message}'"