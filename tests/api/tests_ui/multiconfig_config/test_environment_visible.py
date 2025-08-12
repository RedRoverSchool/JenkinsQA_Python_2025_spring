import allure
from tests.api.tests_ui.multiconfig_config.data import project_name
import pytest
from pages.multi_config_project_config_page import MultiConfigProjectConfigPage


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
def test_delete_checkbox_is_selected(create_multiconfig_project_with_env_options_delete_api, main_page):
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
def test_use_secret_text_checkbox_is_selected(create_multiconfig_project_with_env_options_use_secrets_api, main_page):
    page = main_page.go_to_multiconfig_project_page(project_name).go_to_configure_page()
    with allure.step("Assert 'Use secret text(s) or file(s)' checkbox is selected'"):
        assert page.is_elements_selected(page.Locators.USE_SECRET_TEXT)


@allure.epic("Multi-configuration Project")
@allure.story("Build Environment section")
@allure.title("UI: Verify 'Add timestamps to the Console Output' checkbox is selected")
@allure.description(
    "Ensure 'Add timestamps to Console Output' checkbox is selected on Configure page of multi-configuration project")
@allure.testcase("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/889", name="TC_04.007.04")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/889", name="Github issue")
def test_add_timestamps_checkbox_selected(create_multiconfig_project_with_env_options_add_timestamps_api, main_page):
    page = main_page.go_to_multiconfig_project_page(project_name).go_to_configure_page()
    with allure.step("Assert 'Add timestamps to the Console Output' checkbox is selected"):
        assert page.is_elements_selected(page.Locators.ADD_TIMESTAMP_CHECKBOX)


@allure.testcase("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/891", name="TC_04.007.04")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/891", name="Github issue")
def test_Inspect_build_log_published_build_checkbox_selected(create_multiconfig_project_with_env_options_build_lod_api,
                                                             main_page):
    page = main_page.go_to_multiconfig_project_page(project_name).go_to_configure_page()
    with allure.step("Assert 'Inspect build log for published build' checkbox is selected"):
        assert page.is_elements_selected(page.Locators.BUILD_SCANS_CHECKBOX)


@allure.epic("Multi-configuration Project")
@allure.story("Build Environment section")
@allure.title("UI: Verify 'Add timestamps to the Console Output' checkbox is selected")
@allure.description(
    "Ensure 'Add timestamps to Console Output' checkbox is selected on Configure page of multi-configuration project")
@allure.testcase("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/898", name="TC_04.007.06")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/898", name="Github issue")
def test_terminate_build_selected(create_multiconfig_project_with_env_options_terminate_build_api, main_page):
    page = main_page.go_to_multiconfig_project_page(project_name).go_to_configure_page()
    with allure.step("Assert 'Terminate a build if it's stuck' checkbox is selected"):
        assert page.is_elements_selected(page.Locators.TERMINATE_BUILD_CHECKBOX)


@allure.epic("Multi-configuration Project")
@allure.story("Build Environment section")
@allure.title("UI: 'Use secret text(s) or file(s)' is selected and config can be saved")
@allure.description("Assert checkbox is selected, click Save, verify redirect to Project page")
@allure.testcase(url="https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/901", name="TC_04.007.07")
@allure.link(url="https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/901", name="Github issue")
def test_use_secret_text_checkbox_and_save(create_multiconfig_project_with_env_options_use_secrets_api, main_page):
    config_page = main_page.go_to_multiconfig_project_page(project_name).go_to_configure_page()

    with allure.step("Assert 'Use secret text(s) or file(s)' checkbox is selected"):
        assert config_page.is_elements_selected(config_page.Locators.USE_SECRET_TEXT)

    with allure.step("Click Save and wait for Project page"):
        project_page = config_page.submit_and_open_project_page()

    with allure.step("Verify redirect to Project page (not /configure)"):
        assert "/configure" not in project_page.driver.current_url.lower()


CASES = [
    ("Delete workspace", "create_multiconfig_project_with_env_options_delete_api", "DELETE_WORKSPACE_CHECKBOX"),
    ("Use secret text(s) or file(s)", "create_multiconfig_project_with_env_options_use_secrets_api", "USE_SECRET_TEXT"),
    ("Add timestamps to the Console Output", "create_multiconfig_project_with_env_options_add_timestamps_api",
     "ADD_TIMESTAMP_CHECKBOX"),
    ("Inspect build log for published build scans", "create_multiconfig_project_with_env_options_build_lod_api",
     "BUILD_SCANS_CHECKBOX"),
    ("Terminate a build if it's stuck", "create_multiconfig_project_with_env_options_terminate_build_api",
     "TERMINATE_BUILD_CHECKBOX"),
]


@pytest.mark.parametrize(
    "title, fixture_name, locator_name",
    CASES,
    ids=[c[0] for c in CASES]
)
@allure.epic("Multi-configuration Project")
@allure.story("Build Environment section")
@allure.title("UI: 'Use secret text(s) or file(s)' is selected and config can be saved")
@allure.description("Assert checkboxes is selected, click Save, verify redirect to Project page")
@allure.testcase(url="https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/901", name="TC_04.007.07")
@allure.link(url="https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/901", name="Github issue")
def test_env_checkbox_selected_and_save(title, fixture_name, locator_name, request, main_page):
    request.getfixturevalue(fixture_name)

    main_page.driver.get(main_page.base_url + f"/job/{project_name}/configure")
    config_page = MultiConfigProjectConfigPage(main_page.driver, project_name).wait_for_url()

    allure.dynamic.title(f"UI: '{title}' checkbox is selected and config can be saved")
    allure.dynamic.description("Assert checkbox is selected, click Save, verify redirect to Project page")
    allure.dynamic.link(
        "https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/887",
        name="Github issue"
    )

    locator = getattr(config_page.Locators, locator_name)
    with allure.step(f"Assert '{title}' checkbox is selected"):
        assert config_page.is_elements_selected(locator)

    with allure.step("Click Save and wait for Project page"):
        project_page = config_page.submit_and_open_project_page()

    with allure.step("Verify redirect to Project page (not /configure)"):
        assert "/configure" not in project_page.driver.current_url.lower()
