import pytest
from tests.new_folder_configuration.folder_data import FolderNames

@pytest.fixture
def folder_config_page(new_item_page):
    return new_item_page.create_new_folder(FolderNames.item_name)
