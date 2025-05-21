import allure

from pages.main_page import MainPage
from pages.new_item_page import NewItemPage
from tests.new_item.data import new_pipeline_name, new_folder_name


@allure.epic("New Item")
@allure.story("Folder")
@allure.title("Adding an item to an existing folder [Create a Job]")
@allure.testcase("TC_01.004.02")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/348", name="Github issue")
def test_should_add_item_to_existing_folder(prepare_folder_env, main_page: MainPage):
    item_in_folder_list = main_page.go_to_the_folder_page(new_folder_name) \
        .click_on_create_job_inside_folder() \
        .create_new_pipeline(new_pipeline_name) \
        .header.go_to_the_main_page() \
        .go_to_the_folder_page(new_folder_name) \
        .get_item_list()
    with allure.step('Verify that the new item was created inside the folder'):
        assert [new_pipeline_name] == item_in_folder_list, f"{new_pipeline_name} was not created inside the folder"


@allure.epic("New Item")
@allure.story("Folder")
@allure.title("Move an existing item into an already created folder")
@allure.testcase("TC_01.004.05")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/416", name="Github issue")
def test_should_move_item_to_the_folder(prepare_folder_env, main_page: MainPage, new_item_page: NewItemPage):
    main_page.go_to_new_item_page()
    new_item_page.create_new_pipeline_project(new_pipeline_name)

    pipeline_page = main_page.go_to_the_pipeline_page(new_pipeline_name)
    pipeline_page.move_item_to_folder()
    folder_page = main_page.go_to_the_folder_page(new_folder_name)

    with allure.step('Verify that the pipeline was moved to the folder'):
        folder_items = folder_page.get_item_list()
        assert new_pipeline_name in folder_items, \
            f"Pipeline '{new_pipeline_name}' not found in folder"
