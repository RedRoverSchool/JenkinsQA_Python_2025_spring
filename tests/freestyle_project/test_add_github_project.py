from tests.freestyle_project.freestyle_data import Freestyle
import allure


@allure.epic("Freestyle Project Configuration")
@allure.story("General project Settings")
@allure.title("Add GitHub project")
@allure.testcase("TC_02.009.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/531", name="Github issue")
def test_add_github_project(freestyle):
    with allure.step("Enable GitHub checkbox"):
        freestyle.check_github_project_option()
    with allure.step("Assert GitHub checkbox is selected"):
        assert freestyle.is_github_project_option_enabled(), "GitHub checkbox isn't selected"

    with allure.step(f"Enter to the \"Project url\" input field GitHub repository URL: {Freestyle.github_project_url}"):
        freestyle.add_project_url(Freestyle.github_project_url)
    with allure.step("Save project configuration"):
        freestyle_project_page = freestyle.click_save_button()
    menu_texts = freestyle_project_page.get_menu_items_texts()
    expected_item = "GitHub"

    with allure.step(f"Assert {expected_item} appears in the project menu"):
        assert any(expected_item.lower() in text.lower() for text in menu_texts), \
            f"Expected item '{expected_item}' is not in the menu. Available menu items: {menu_texts}"
