import allure
import pytest
from tests.new_item.data import new_folder_name
from pages.new_item_page import NewItemPage


@pytest.fixture(scope="function")
@allure.title("Preconditions: Creating a empty folder")
def prepare_folder_env(new_item_page: NewItemPage):
    return new_item_page.create_new_folder(new_folder_name).header.go_to_the_main_page()
