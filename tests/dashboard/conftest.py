import allure
import pytest

from tests.new_item.data import new_folder_name, new_pipeline_name, new_multi_config_project_name


@pytest.fixture
@allure.title("Prepare test environment with job and folders")
@allure.description("Creates a multi-configuration project, folder, and pipeline job for test environment setup.")
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
