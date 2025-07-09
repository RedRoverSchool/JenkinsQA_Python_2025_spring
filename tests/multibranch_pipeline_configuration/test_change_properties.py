import allure


@allure.epic("Multibranch pipeline Configuration")
@allure.story("Change Properties")
@allure.title("Verify Properties section is available")
@allure.description("Verify that the “Properties” section is visible and accessible when editing a Multibranch Pipeline configuration in Jenkins.")
@allure.testcase("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/878", name="TC_06.010.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/878", name="Github issue")
def test_property_section_exists(multibranch_pipeline_config_page):
    properties_section = multibranch_pipeline_config_page.get_properties_section()

    with allure.step("Assert Properties section is displayed"):
        assert properties_section.is_displayed()

@allure.epic("Multibranch pipeline Configuration")
@allure.story("Change Properties")
@allure.title("Add/Edit Properties Section Functionality")
@allure.description("Verify that within the ”Properties” section of a Multibranch Pipeline configuration, the user can add and edit custom properties that apply to all branches or define job-level behaviors.")
@allure.testcase("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/903", name="TC_06.010.02")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/903", name="Github issue")
def test_add_property(multibranch_pipeline_config_page):
    multibranch_pipeline_config_page.get_properties_section()
    new_roperty = multibranch_pipeline_config_page.add_properties()

    with allure.step("Assert new property added"):
        assert new_roperty == "Library"

    library_value = multibranch_pipeline_config_page.enter_item_name()
    
    multibranch_pipeline_config_page.click_save_property()
    main_page = multibranch_pipeline_config_page.main_page_availability()

    with allure.step("Assert redirecting to the project\n's main page completed"):
        assert main_page.is_displayed()

    multibranch_pipeline_config_page.click_on_configure()
    multibranch_pipeline_config_page.get_properties_section()
    value = multibranch_pipeline_config_page.find_added_property()

    with allure.step("Assert added/edited property value is correctly saved and displayed"):
        assert value == library_value, f"Value : {library_value} wasn't found"