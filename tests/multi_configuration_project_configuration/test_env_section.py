import allure


@allure.epic("Multi-configuration project Configuration")
@allure.story("Configure Environment")
@allure.title("Environment Section Is Displayed")
@allure.testcase("TC_04.007.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/883", name="Github issue")
def test_env_section_is_displayed(multi_config_project_config_page):
    multi_config_project_config_page = multi_config_project_config_page
    with allure.step("Assert that \"Environment\" section is displayed"):
        assert multi_config_project_config_page.get_environment_section().is_displayed()


@allure.epic("Multi-configuration project Configuration")
@allure.story("Configure Environment")
@allure.title("Delete_checkbox_is_selected")
@allure.testcase("TC_04.007.02")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/885", name="Github issue")
def test_delete_checkbox_is_selected(multi_config_project_config_page):
    with allure.step("Assert that 'Delete workspace' checkbox is selected"):
        page = multi_config_project_config_page.click_delete_workspace_checkbox()
        assert page.is_elements_selected(page.Locators.DELETE_WORKSPACE_CHECKBOX)
