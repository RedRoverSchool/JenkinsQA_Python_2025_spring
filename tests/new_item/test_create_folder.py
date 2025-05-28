import allure

@allure.epic("New Item")
@allure.story("Create a new item")
@allure.title("Create folder")
@allure.testcase("TC_01.001.22")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/714", name="Github issue")
def test_create_folder_from_dashboard(new_item_page, unique_folder_name):

    folder_conf_page = new_item_page.create_new_folder(unique_folder_name)
    header = folder_conf_page.header.go_to_the_main_page().click_on_folder_by_name(unique_folder_name).get_header()

    assert header == unique_folder_name, \
        f"Имя папки '{unique_folder_name}' не отображается в заголовке страницы"