import allure

from tests.api.tests_ui.multiconfig_config.data import project_name


@allure.epic("Multi-configuration Project")
@allure.story("Advanced Project Options")
@allure.title("API: Verify Advanced Project Options section is available")
@allure.description("Verify that the user can access the Advanced Project Options section by navigating to the Configure page of a multi-configuration project.")
@allure.testcase("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/893", name="TC_04.003.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/893", name="Github issue")
def test_advanced_project_section_exists(create_multiconfig_project_api, main_page):
    multi_config_project_page = main_page.go_to_multiconfig_project_page(project_name)
    advanced_section = multi_config_project_page.go_to_configure_page().get_advanced_section()

    with allure.step("Assert Advanced Project Options section is displayed"):
        assert advanced_section.is_displayed()