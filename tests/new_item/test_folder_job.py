from pages.new_item_page import NewItemPage
from tests.new_item.data import new_pipeline_name
from pages.main_page import MainPage
from pages.job_page import JobPage


def test_should_add_item_to_existing_folder(prepare_folder_env, new_item_page: NewItemPage, main_page: MainPage,
                                            job_page: JobPage):
    main_page.click_on_folder_item()
    job_page.create_new_job()
    job_page.create_pipeline(new_pipeline_name).go_to_the_main_page()
    main_page.click_on_folder_item()
    assert job_page.item_is_present(new_pipeline_name), f"{new_pipeline_name} was not created inside the folder"
