import pytest
from tests.new_folder_configuration.variables import FolderNames

@pytest.fixture
def folder_config_page(driver, main_page):
    folder_name = FolderNames.item_name
    page = main_page.go_to_new_item_page().create_new_folder(folder_name)
    return page