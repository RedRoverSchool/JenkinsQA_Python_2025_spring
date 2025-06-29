import allure


@allure.epic("Multibranch pipeline Configuration")
@allure.story("Change Branch Sources")
@allure.title("Verify Branch Sources section is available")
@allure.description("Verify that the “Branch Sources” section is present on the configuration page of a Multibranch Pipeline project.")
@allure.testcase("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/882", name="TC_06.004.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/882", name="Github issue")
def test_branch_sources_section_exists(multibranch_pipeline_config_page):
    branch_sources_section = multibranch_pipeline_config_page.get_branch_sources_section()

    with allure.step("Assert Branch Sources section is displayed"):
        assert branch_sources_section.is_displayed()