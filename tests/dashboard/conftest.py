import allure
import pytest

from tests.dashboard.data import DashboardTable
from tests.new_item.data import new_folder_name, new_pipeline_name, new_multi_config_project_name


@pytest.fixture
@allure.title("Prepare test environment with job and folders")
def create_job_and_folders_env(new_item_page):
    return new_item_page.create_new_multi_config_project(new_multi_config_project_name) \
                        .header.go_to_the_main_page() \
                        .go_to_new_item_page() \
                        .create_new_folder(new_folder_name) \
                        .header.go_to_the_main_page() \
                        .go_to_the_folder_page(new_folder_name) \
                        .click_on_create_job_inside_folder() \
                        .create_new_pipeline(new_pipeline_name) \
                        .header.go_to_the_main_page()


@pytest.fixture
@allure.title("Prepare test environment with job Pipeline")
def create_job_pipeline_env(new_item_page):
    return new_item_page.create_new_pipeline(new_pipeline_name).header.go_to_the_main_page()


@allure.title("Prepare test environment with all jobs")
@pytest.fixture(scope="function")
def created_projects(main_page):
    created = []
    for project_type, project_name in DashboardTable.PROJECT_NAMES.items():
        main_page.go_to_new_item_page().create_project(project_type, project_name)
        main_page.header.go_to_the_main_page()
        created.append((project_type, project_name))
    return created
