from pages.main_page import MainPage
from tests.new_item.data import new_pipeline_name, new_folder_name


def test_should_add_item_to_existing_folder(prepare_folder_env, main_page: MainPage):
    item_in_folder_list = main_page.go_to_the_folder_page(new_folder_name) \
        .click_on_create_job_inside_folder() \
        .create_new_pipeline(new_pipeline_name) \
        .header.go_to_the_main_page() \
        .go_to_the_folder_page(new_folder_name) \
        .get_item_list()

    assert [new_pipeline_name] == item_in_folder_list, f"{new_pipeline_name} was not created inside the folder"
