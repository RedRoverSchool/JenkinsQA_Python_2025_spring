import allure

import utils.assertions as assertions
from tests.pipeline.pipeline_data import BuildTriggers


@allure.epic("Pipeline Configuration")
@allure.story("Build Triggers")
@allure.title("Displaying the \"Triggers\" section title")
@allure.testcase("TC_03.003.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/822", name="Github issue")
def test_display_triggers_section_title(pipeline_project_config_page):
    assert pipeline_project_config_page.get_text_title_triggers() == BuildTriggers.TITLE


@allure.epic("Pipeline Configuration")
@allure.story("Build Triggers")
@allure.title("Displaying the \"Triggers\" section description")
@allure.testcase("TC_03.003.02")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/831", name="Github issue")
def test_display_triggers_section_description(pipeline_project_config_page):
    assert pipeline_project_config_page.get_text_description_triggers() == BuildTriggers.DESCRIPTION


@allure.epic("Pipeline Configuration")
@allure.story("Build Triggers")
@allure.title("Displaying the \"Triggers\" section in the sidebar")
@allure.testcase("TC_03.003.03")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/832", name="Github issue")
def test_display_triggers_section_in_sidebar(pipeline_project_config_page):
    assert pipeline_project_config_page.get_text_sidebar_triggers() == BuildTriggers.TITLE


@allure.epic("Pipeline Configuration")
@allure.story("Build Triggers")
@allure.title("Displaying trigger checkbox labels")
@allure.testcase("TC_03.003.04")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/833", name="Github issue")
def test_display_trigger_checkbox_labels(pipeline_project_config_page):
    actual_labels = pipeline_project_config_page.get_text_trigger_labels()

    assertions.soft_assert_list_length_equal(actual_labels, BuildTriggers.TRIGGER_LABELS)
    assertions.soft_assert_lists_equal_by_index(actual_labels, BuildTriggers.TRIGGER_LABELS)


@allure.epic("Pipeline Configuration")
@allure.story("Build Triggers")
@allure.title("Display of trigger checkboxes")
@allure.testcase("TC_03.003.05")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/834", name="Github issue")
def test_all_trigger_checkboxes_are_visible(pipeline_project_config_page):
    actual_ids = pipeline_project_config_page.get_visible_trigger_checkboxes_ids()

    assertions.soft_assert_list_length_equal(actual_ids, BuildTriggers.TRIGGER_CHECKBOXES_IDS)
    assertions.soft_assert_lists_equal_by_index(actual_ids, BuildTriggers.TRIGGER_CHECKBOXES_IDS)


@allure.epic("Pipeline Configuration")
@allure.story("Build Triggers")
@allure.title("Default state of trigger checkboxes")
@allure.testcase("TC_03.003.06")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/835", name="Github issue")
def test_default_state_trigger_checkboxes_are_unchecked(pipeline_project_config_page):
    checkboxes_unchecked = pipeline_project_config_page.is_trigger_checkboxes_unchecked()

    assertions.soft_assert_list_length_equal(checkboxes_unchecked, BuildTriggers.TRIGGER_CHECKBOXES_IDS)
    assertions.soft_assert_all_elements_true(checkboxes_unchecked)


@allure.epic("Pipeline Configuration")
@allure.story("Build Triggers")
@allure.title("Enable trigger checkboxes by clicking labels")
@allure.testcase("TC_03.003.07")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/844", name="Github issue")
def test_enable_trigger_checkboxes_by_labels(pipeline_project_config_page):
    checkboxes_checked = pipeline_project_config_page.click_trigger_labels().is_trigger_checkboxes_checked()

    assertions.soft_assert_list_length_equal(checkboxes_checked, BuildTriggers.TRIGGER_CHECKBOXES_IDS)
    assertions.soft_assert_all_elements_true(checkboxes_checked)


@allure.epic("Pipeline Configuration")
@allure.story("Build Triggers")
@allure.title("Disable trigger checkboxes by clicking label")
@allure.testcase("TC_03.003.08")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/845", name="Github issue")
def test_disable_trigger_checkboxes_by_labels(pipeline_config_page_enable_trigger_checkboxes):
    pipeline_config_page_enable_trigger_checkboxes.click_trigger_labels()
    checkboxes_unchecked = pipeline_config_page_enable_trigger_checkboxes.is_trigger_checkboxes_unchecked()

    assertions.soft_assert_list_length_equal(checkboxes_unchecked, BuildTriggers.TRIGGER_CHECKBOXES_IDS)
    assertions.soft_assert_all_elements_true(checkboxes_unchecked)


@allure.epic("Pipeline Configuration")
@allure.story("Build Triggers")
@allure.title("Display of helper icons (tooltips) near trigger checkbox labels")
@allure.testcase("TC_03.003.09")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/846", name="Github issue")
def test_display_helper_icons_near_trigger_labels(pipeline_project_config_page):
    helper_icons = pipeline_project_config_page.is_helper_icons_displayed()

    assertions.soft_assert_list_length_equal(helper_icons, BuildTriggers.TRIGGER_CHECKBOXES_IDS)
    assertions.soft_assert_all_elements_true(helper_icons)


@allure.epic("Pipeline Configuration")
@allure.story("Build Triggers")
@allure.title("Helper tooltip help icon texts appear on hover")
@allure.testcase("TC_03.003.10")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/847", name="Github issue")
def test_appear_helper_tooltip_texts(pipeline_project_config_page):
    actual_helper_tooltips = pipeline_project_config_page.get_trigger_helper_tooltips()

    assertions.soft_assert_list_length_equal(actual_helper_tooltips, BuildTriggers.TRIGGER_CHECKBOXES_IDS)
    assertions.soft_assert_lists_equal_by_index(actual_helper_tooltips, BuildTriggers.TRIGGER_HELPER_TOOLTIPS)


@allure.epic("Pipeline Configuration")
@allure.story("Build Triggers")
@allure.title("Helper tooltip help icon disappears on mouse leave")
@allure.testcase("TC_03.003.11")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/848", name="Github issue")
def test_trigger_tooltips_disappear_on_mouse_leave(pipeline_project_config_page):
    tooltip_disappearance_statuses = pipeline_project_config_page.trigger_tooltips_disappeared()

    assertions.soft_assert_list_length_equal(tooltip_disappearance_statuses, BuildTriggers.TRIGGER_CHECKBOXES_IDS)
    assertions.soft_assert_all_elements_true(tooltip_disappearance_statuses)


@allure.epic("Pipeline Configuration")
@allure.story("Build Triggers")
@allure.title("Project creation with no triggers selected")
@allure.testcase("TC_03.003.12")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/849", name="Github issue")
def test_create_pipeline_project_without_triggers(pipeline_project_config_page):
    pipeline_page = pipeline_project_config_page.click_save_button_and_open_project_page()

    assertions.soft_assert_text_equal(pipeline_page.get_title(), BuildTriggers.PIPELINE_PAGE_TITLE)
    assertions.soft_assert_text_equal(pipeline_page.get_header_pipeline_page(), BuildTriggers.PIPELINE_PAGE_HEADER)
