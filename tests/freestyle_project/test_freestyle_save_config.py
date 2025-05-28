import allure
from tests.freestyle_project.freestyle_data import Freestyle


@allure.epic("Freestyle Project Configuration")
@allure.story("Save or Apply")
@allure.title("The \"Save\" and \"Apply\" buttons should be available when configuring a new project.")
@allure.testcase("TC_02.008.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/461", name="Github issue")
def test_buttons_available(freestyle):
    with allure.step("Assert that Save button is available"):
        assert freestyle.is_save_button_available()
        with allure.step("Assert that Apply button is available"):
            assert freestyle.is_apply_button_available()

@allure.epic("Freestyle Project Configuration")
@allure.story("Save or Apply")
@allure.title("""Clicking "Save" should:
- Keep and store all project settings.
- Redirect the user to the project dashboard.""")
@allure.testcase("TC_02.008.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/461", name="Github issue")
def test_save_config(freestyle):
    with allure.step("Click \"Save\" button"):
        project_page = freestyle.click_save_button()
    with allure.step("Assert that user was redirected to Freestyle Project Page"):
        assert project_page.get_h1_value() == Freestyle.project_name

@allure.epic("Freestyle Project Configuration")
@allure.story("Save or Apply")
@allure.title("""Clicking "Apply" should:
- Save changes without leaving the configuration page.
- Show a confirmation message that changes have been applied successfully.""")
@allure.testcase("TC_02.008.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/461", name="Github issue")
def test_applay_config(freestyle):
    with allure.step("Click \"Apply\" button"):
        freestyle.click_apply_button()
    with allure.step("Assert that confirmation message is visible."):
        assert freestyle.is_notification_was_visible()
    with allure.step("Assert that configuration saving occurred without leaving the configuration page"):
        assert freestyle.get_h1_text() == 'Configure'
