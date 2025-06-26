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


@allure.epic("Multi-configuration project Configuration")
@allure.story("Configure Environment")
@allure.title("Use_secret_text_is_selected")
@allure.testcase("TC_04.007.03")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/887", name="Github issue")
def test_use_secret_text_is_selected(multi_config_project_config_page):
    with allure.step("Assert that 'Use secret text' checkbox is selected"):
        page = multi_config_project_config_page.click_use_secret_text_checkbox()
        assert page.is_elements_selected(page.Locators.USE_SECRET_TEXT)


@allure.epic("Multi-configuration project Configuration")
@allure.story("Configure Environment")
@allure.title("Add_timestamps_to_console_output_is_selected")
@allure.testcase("TC_04.007.04")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/889", name="Github issue")
def test_add_timestamps_to_console_output_is_selected(multi_config_project_config_page):
    with allure.step("Assert that 'Add timestamps to the Console output' checkbox is selected"):
        page = multi_config_project_config_page.click_add_timestamps_to_console_output_checkbox()
        assert page.is_elements_selected(page.Locators.ADD_TIMESTAMP_CHECKBOX)


@allure.epic("Multi-configuration project Configuration")
@allure.story("Configure Environment")
@allure.title("Inspect build log for published build scans is_selected")
@allure.testcase("TC_04.007.05")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/891", name="Github issue")
def test_inspect_build_log_for_published_build_scans_is_selected(multi_config_project_config_page):
    with allure.step("Assert that 'Inspect build log for published build scans' checkbox is selected"):
        page = multi_config_project_config_page.click_build_scans_checkbox()
        assert page.is_elements_selected(page.Locators.BUILD_SCANS_CHECKBOX)


@allure.epic("Multi-configuration project Configuration")
@allure.story("Configure Environment")
@allure.title("Terminate a build if it's stuck is_selected")
@allure.testcase("TC_04.007.06")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/898", name="Github issue")
def test_terminate_a_build_is_selected(multi_config_project_config_page):
    with allure.step("Assert that 'Terminate a build' checkbox is selected"):
        page = multi_config_project_config_page.click_terminate_build_checkbox()
        assert page.is_elements_selected(page.Locators.TERMINATE_BUILD_CHECKBOX)
