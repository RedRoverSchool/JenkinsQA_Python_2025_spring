import allure
import pytest
from tests.freestyle_project.freestyle_data import Freestyle


@allure.epic("Freestyle Project Configuration")
@allure.story("Set up Environment")
@allure.title("\"Environment\" section should be available, helper tooltip appears, empty environment is permissible")
@allure.testcase("TC_02.005.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/407", name="Github issue")
def test_exist_environment_section(freestyle):
    with allure.step("Assert that \"Environment\" section is available"):
        assert freestyle.get_environment_element().is_displayed()

@allure.epic("Freestyle Project Configuration")
@allure.story("Set up Environment")
@allure.title("The helper tooltip appears when the mouse cursor hovers over the question marks")
@allure.testcase("TC_02.005.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/407", name="Github issue")
@pytest.mark.parametrize('tp_link, tp_expected_text', Freestyle.tooltip_environment)
def test_tooltip_environment_items(freestyle, tp_link, tp_expected_text):
    with allure.step("Get helper tooltip text"):
        freestyle.scroll_to_post_build_actions()
        tp_text = freestyle.get_tooltip(tp_link)
    with allure.step(f"Assert that current tooltip is equal to \"{tp_expected_text}\""):
        assert tp_text == tp_expected_text

@allure.epic("Freestyle Project Configuration")
@allure.story("Set up Environment")
@allure.title("If no environment settings are configured, the project should still be creatable")
@allure.testcase("TC_02.005.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/407", name="Github issue")
def test_create_freestyle_without_environment(freestyle):
    with allure.step("Saving Freestyle Project without environment settings"):
        freestyle_page = freestyle.click_save_button()
    with allure.step("Assert thet Freestyle Project is created"):
        assert freestyle_page.get_title() == f"{Freestyle.project_name} [Jenkins]"
