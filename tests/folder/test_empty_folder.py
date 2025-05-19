from pages.new_item_page import NewItemPage
from tests.folder.data import Folder


def test_empty_folder_message(new_item_page: NewItemPage):
    folder_config_page = new_item_page.create_new_folder(Folder.FOLDER_NAME)
    message = (folder_config_page.header
               .go_to_the_main_page()
               .go_to_the_folder_page(Folder.FOLDER_NAME)
               .get_empty_state_message()
               )

    assert message == Folder.EMPTY_STATE_MESSAGE, f"Expected message not found. Got: '{message}'"

