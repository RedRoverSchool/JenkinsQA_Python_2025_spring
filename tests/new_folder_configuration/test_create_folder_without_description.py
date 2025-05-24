import allure
from tests.new_folder_configuration.folder_data import FolderNames


@allure.epic("Folder Configuration")
@allure.story("Display Name and Description")
@allure.title("Create a New Folder without Description")
@allure.testcase("TC_05.001.02")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/397")
def test_create_folder_without_description(folder_config_page):
    folder_config_page.click_save_button()

    assert folder_config_page.get_folder_name_after_click_save() == FolderNames.item_name, f"Folder '{FolderNames.item_name}' NOT FOUND"




