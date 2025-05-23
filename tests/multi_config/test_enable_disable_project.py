import allure

from tests.multi_config.data import ProjectToggle


@allure.epic("Multi-configuration project Configuration")
@allure.story("Enable or Disable the Project")
@allure.title("Enable and Disable the project by clicking on the switch button")
@allure.testcase("TC_04.001.02")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/657", name="Github issue")
def test_enable_project_by_toggle_switch(multi_config_project_enabled):
    with allure.step("Disable the switch button 'Enabled/Disabled'"):
        config_page = multi_config_project_enabled.click_switch_button()

    assert config_page.is_project_disabled(), "The project is not disabled"

    with allure.step("Enable the switch button 'Enabled/Disabled'"):
        config_page.click_switch_button()

    assert config_page.is_project_enabled(), "The project is not enabled"


@allure.epic("Multi-configuration project Configuration")
@allure.story("Enable or Disable the Project")
@allure.title("Display a warning message on the Project main page")
@allure.testcase("TC_04.001.03")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/658", name="Github issue")
def test_display_warning_message(page_disabled_multi_config_project):
    warning_message = page_disabled_multi_config_project.get_text_warning_message()

    assert warning_message == ProjectToggle.WARNING_MESSAGE, \
        f"Expected message '{ProjectToggle.WARNING_MESSAGE}' NOT FOUND"


@allure.epic("Multi-configuration project Configuration")
@allure.story("Enable or Disable the Project")
@allure.title("Disappear a warning message on the Project page")
@allure.testcase("TC_04.001.04")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/660", name="Github issue")
def test_disappear_warning_message(page_disabled_multi_config_project):
    page = page_disabled_multi_config_project.enable_project()

    assert page.wait_warning_message_to_disappear(), \
        f"Warning message {ProjectToggle.WARNING_MESSAGE} did not disappear"
    assert page.get_project_status_title() == ProjectToggle.STATUS_NOT_BUILT, \
        f"Expected project status '{ProjectToggle.STATUS_NOT_BUILT}' NOT FOUND"
