import pytest
import allure

from pages.multi_config_project_config_page import MultiConfigProjectConfigPage
from tests.multi_config.data import Project, project_name


@pytest.fixture
def multi_config_project_config_page(new_item_page):
    return new_item_page.create_new_multi_config_project(project_name)


@pytest.fixture
def multi_config_project_with_description(new_item_page):
    from tests.multi_config.data import project_name, description_text
    config_page = new_item_page.create_new_multi_config_project(project_name)
    return config_page.set_description(description_text, project_name)


@pytest.fixture(scope="function")
@allure.title("Prepare configuration page of enabled Multi-configuration project")
def multi_config_project_enabled(new_item_page) -> MultiConfigProjectConfigPage:
    return new_item_page.create_new_multi_config_project(Project.PROJECT_NAME)


@pytest.fixture(scope="function")
@allure.title("Prepare configuration page of disabled Multi-configuration project")
def multi_config_project_disabled(multi_config_project_enabled: MultiConfigProjectConfigPage):
    multi_config_project_enabled.click_switch_button()
    return multi_config_project_enabled


@pytest.fixture(scope="function")
@allure.title("Prepare project page of disabled Multi-configuration project")
def page_disabled_multi_config_project(multi_config_project_disabled: MultiConfigProjectConfigPage):
    return multi_config_project_disabled.submit_and_open_project_page(Project.PROJECT_NAME)
