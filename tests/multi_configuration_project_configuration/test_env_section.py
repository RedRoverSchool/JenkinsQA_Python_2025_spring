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

