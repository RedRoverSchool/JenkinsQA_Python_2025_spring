import allure
import pytest

from pages.new_item_page import NewItemPage
from tests.new_item.data import Copy
from tests.new_item.data import new_folder_name


@pytest.fixture(scope="function")
@allure.title("Prepare for page for copy")
def prepare_page_for_copy(new_item_page: NewItemPage):
    new_item_page.create_new_folder(Copy.FOLDER_NAME_TO_COPY)
    return new_item_page.header.go_to_the_main_page().go_to_new_item_page()


@pytest.fixture(scope="function")
def prepare_folder_env(new_item_page: NewItemPage):
    return new_item_page.create_new_folder(new_folder_name).header.go_to_the_main_page()


