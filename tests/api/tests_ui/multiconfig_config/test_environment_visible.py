import allure
from tests.api.tests_ui.multiconfig_config.data import project_name


@allure.epic("Multi-configuration Project")
@allure.story("Environment section")
@allure.title("API: Verify Environment section is available")
@allure.description("Verify the Environment section is visible on Configure page of a multi-configuration project")
@allure.testcase("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/883", name="TC_04.007.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/883", name="Github issue")
def test_environment_section_exists(create_multiconfig_project_api, main_page):
    multi_config_project_page = main_page.go_to_multiconfig_project_page(project_name)
    config_page = multi_config_project_page.go_to_configure_page()

    with allure.step("Get Environment section"):
        environment_section = config_page.get_environment_section()

    with allure.step("Assert Environment section is displayed"):
        assert environment_section.is_displayed()


@allure.epic("Multi-configuration Project")
@allure.story("Build Environment section")
@allure.title("UI: Verify 'delete_checkbox_is_selected' checkbox is selected")
@allure.description(
    "Ensure 'delete_checkbox' checkbox is selected on Configure page of a multi-configuration project")
@allure.testcase("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/885", name="TC_04.007.02")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/885", name="Github issue")
def test_delete_checkbox_is_selected(create_multiconfig_project_with_env_options_api, main_page):
    page = main_page.go_to_multiconfig_project_page(project_name).go_to_configure_page()
    with allure.step("Assert that 'Delete workspace' checkbox is selected"):
        assert page.is_elements_selected(page.Locators.DELETE_WORKSPACE_CHECKBOX)


@allure.epic("Multi-configuration Project")
@allure.story("Build Environment section")
@allure.title("UI: Verify 'Use secret text(s) or file(s)' checkbox is selected")
@allure.description(
    "Ensure 'Use secret text(s) or file(s)' checkbox is selected on Configure page of a multi-configuration project")
@allure.testcase("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/887", name="TC_04.007.03")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/887", name="Github issue")
def test_use_secret_text_checkbox_is_selected(create_multiconfig_project_with_env_options_api, main_page):
    page = main_page.go_to_multiconfig_project_page(project_name).go_to_configure_page()
    with allure.step("Assert 'Use secret text(s) or file(s)' checkbox is selected'"):
        assert page.is_elements_selected(page.Locators.USE_SECRET_TEXT)

