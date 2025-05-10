import pytest

from pages.new_item_page import NewItemPage
from tests.new_item.data import folder_name_to_copy


@pytest.fixture(scope="function")
def new_item_page_for_copy(new_item_page: NewItemPage):
    return new_item_page.create_folder_and_open_page(folder_name_to_copy)
