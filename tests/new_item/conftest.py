import pytest

from pages.job_page import JobPage
from pages.new_item_page import NewItemPage
from tests.new_item.data import new_folder_name, new_pipeline_name


@pytest.fixture(scope="function")
def new_item_page_for_copy(new_item_page: NewItemPage):
    return new_item_page.create_folder_and_open_page(new_folder_name)


@pytest.fixture(scope="function")
def prepare_folder_env(new_item_page: NewItemPage):
    return new_item_page.create_new_folder(new_folder_name).go_to_the_main_page()


@pytest.fixture(scope="function")
def prepare_pipeline_project_env(job_page: JobPage):
    return job_page.create_pipeline(new_pipeline_name).go_to_the_main_page()


@pytest.fixture(scope="function")
def job_page(driver) -> JobPage:
    item_name = new_folder_name
    return JobPage(driver, item_name)
