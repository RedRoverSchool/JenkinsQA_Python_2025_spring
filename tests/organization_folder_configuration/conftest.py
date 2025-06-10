import allure
import pytest

from tests.organization_folder_configuration.data import project_name, project_type
from pages.organization_folder_config_page import OrganizationFolderConfigPage


@pytest.fixture(scope="function")
@allure.title("Precondition: Create an Organization Folder project")
def organization_folder_config_page(new_item_page) -> OrganizationFolderConfigPage:
    org_folder_config_page = new_item_page.create_project(project_type, project_name)
    return org_folder_config_page
