import allure
import pytest
import time

from pages.new_item_page import NewItemPage
from tests.new_item.data import Copy


@pytest.fixture(scope="function")
@allure.title("Prepare a page for copy with an existing item")
def prepare_page_for_copy(new_item_page: NewItemPage) -> NewItemPage:
    new_item_page.create_new_folder(Copy.FOLDER_NAME_TO_COPY)
    return new_item_page.header.go_to_the_main_page().go_to_new_item_page()


@pytest.fixture(scope="function")
@allure.title("Prepare a page for copy with multiple items")
def prepare_multiple_items(new_item_page: NewItemPage) -> NewItemPage:
    new_item_page.create_new_folder(Copy.FOLDER_NAME_TO_COPY)
    new_item_page.header.go_to_the_main_page().go_to_new_item_page()
    new_item_page.create_new_folder(Copy.FOLDER_NAME_TO_COPY_2)
    return new_item_page.header.go_to_the_main_page().go_to_new_item_page()


@pytest.fixture(scope="function")
@allure.title("Create unique folder name")
def unique_folder_name():
    return f"TestFolder_{int(time.time() * 1000)}"
