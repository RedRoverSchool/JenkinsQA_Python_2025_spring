import allure

from tests.multi_configuration_project_configuration.data import ProjectToggle


@allure.epic("Multi-configuration project Configuration")
@allure.story("Enable or Disable the Project")
@allure.title("Display the 'Enable or disable the current project' tooltip")
@allure.testcase("TC_04.001.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/542", name="Github issue")
def test_display_tooltip_enable_disable(multi_config_project_enabled):
    tooltip_enable_project = multi_config_project_enabled.get_switch_tooltip_text()

    assert tooltip_enable_project == ProjectToggle.TOOLTIP, \
        f"Expected tooltip {ProjectToggle.TOOLTIP} NOT FOUND"

    multi_config_project_enabled.click_switch_button().hover_over_help_discard_builds()
    tooltip_disable_project = multi_config_project_enabled.get_switch_tooltip_text()

    assert tooltip_disable_project == ProjectToggle.TOOLTIP, \
        f"Expected tooltip {ProjectToggle.TOOLTIP} NOT FOUND"


@allure.epic("Multi-configuration project Configuration")
@allure.story("Enable or Disable the Project")
@allure.title("Enable and Disable the project by clicking on the switch button")
@allure.testcase("TC_04.001.02")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/657", name="Github issue")
def test_enable_disable_project_by_toggle_switch(multi_config_project_enabled):
    config_page = multi_config_project_enabled.click_switch_button()

    assert config_page.is_project_disabled(), "The project is not disabled"

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
        f"Expected warning message '{ProjectToggle.WARNING_MESSAGE}' NOT FOUND"


@allure.epic("Multi-configuration project Configuration")
@allure.story("Enable or Disable the Project")
@allure.title("Disappear a warning message on the Project page")
@allure.testcase("TC_04.001.04")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/660", name="Github issue")
def test_disappear_warning_message(page_disabled_multi_config_project):
    page = page_disabled_multi_config_project.enable_project()

    assert page.wait_warning_message_to_disappear(), \
        f"Warning message {ProjectToggle.WARNING_MESSAGE} did not disappear"
    assert page.get_project_status_title() == ProjectToggle.STATUS_ENABLE_PROJECT, \
        f"Expected project status '{ProjectToggle.STATUS_ENABLE_PROJECT}' NOT FOUND"


@allure.epic("Multi-configuration project Configuration")
@allure.story("Enable or Disable the Project")
@allure.title("Switch button state reflects actual project state after saving and navigation")
@allure.testcase("TC_04.001.05")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/741", name="Github issue")
def test_switch_state_persists_after_save_and_navigation(page_disabled_multi_config_project):
    config_page = page_disabled_multi_config_project.go_to_configure_page()

    assert config_page.is_project_disabled(), "The project is not disabled"


@allure.epic("Multi-configuration project Configuration")
@allure.story("Enable or Disable the Project")
@allure.title("Project status changes on the Project page after enabling the project via Configure page")
@allure.testcase("TC_04.001.06")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/772", name="Github issue")
def test_project_status_changes_after_enabling_in_configure(page_disabled_multi_config_project):
    config_page = page_disabled_multi_config_project.go_to_configure_page()
    enable_project_page = config_page.click_switch_button().submit_and_open_project_page()

    assert enable_project_page.get_project_status_title() == ProjectToggle.STATUS_ENABLE_PROJECT, \
        f"Expected project status '{ProjectToggle.STATUS_ENABLE_PROJECT}' NOT FOUND"


@allure.epic("Multi-configuration project Configuration")
@allure.story("Enable or Disable the Project")
@allure.title("Project status changes on the Project page after disabling the project via Configure page")
@allure.testcase("TC_04.001.07")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/773", name="Github issue")
def test_project_status_changes_after_disabling_in_configure(multi_config_project_enabled):
    page = multi_config_project_enabled.click_switch_button().submit_and_open_project_page()

    assert page.get_project_status_title() == ProjectToggle.STATUS_DISABLE_PROJECT, \
        f"Expected project status '{ProjectToggle.STATUS_DISABLE_PROJECT}' NOT FOUND"


@allure.epic("Multi-configuration project Configuration")
@allure.story("Enable or Disable the Project")
@allure.title("Display of \"Enable\" button on Project main page when project is disabled")
@allure.testcase("TC_04.001.08")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/820", name="Github issue")
def test_display_enable_button_on_project_page(page_disabled_multi_config_project):
    assert page_disabled_multi_config_project.is_enable_button_displayed(), \
        "Enable button is not displayed on the disabled project's main page"
