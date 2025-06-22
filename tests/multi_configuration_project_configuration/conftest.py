import pytest
import allure

from pages.multi_config_project_config_page import MultiConfigProjectConfigPage
from tests.multi_configuration_project_configuration.data import ProjectToggle, project_name


@allure.title("Create Multi-configuration project")
@pytest.fixture
def multi_config_project_config_page(new_item_page):
    return new_item_page.create_new_multi_config_project(project_name)


@pytest.fixture
def multi_config_project_with_description(new_item_page):
    from tests.multi_configuration_project_configuration.data import project_name, description_text
    config_page = new_item_page.create_new_multi_config_project(project_name)
    return config_page.set_description(description_text, project_name)


@pytest.fixture(scope="function")
@allure.title("Create Multi-configuration project")
def multi_config_project_enabled(new_item_page) -> MultiConfigProjectConfigPage:
    return new_item_page.create_new_multi_config_project(ProjectToggle.PROJECT_NAME)


@pytest.fixture(scope="function")
@allure.title("Prepare project page of disabled Multi-configuration project")
def page_disabled_multi_config_project(multi_config_project_enabled: MultiConfigProjectConfigPage):
    multi_config_project_enabled.click_switch_button()
    return multi_config_project_enabled.submit_and_open_project_page()
