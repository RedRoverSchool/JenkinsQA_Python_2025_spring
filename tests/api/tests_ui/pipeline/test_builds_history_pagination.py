import logging
import allure

from pages.pipeline_page import PipelinePage
from tests.api.tests_ui.pipeline.data import BuildsCounter

logger = logging.getLogger(__name__)

@allure.epic("Pipeline Management")
@allure.story("View Build History monitor")
@allure.title("Paginate builds when count exceeds 30")
@allure.description("Verify that when the number of builds exceeds 30, pagination controls are displayed \
                    and allow the user to navigate through the build history.")
@allure.testcase("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/868", "TC_19.009.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/868", name="Github issue")
def test_builds_history_pagination_31(trigger_builds_31, main_page):
    total_builds = BuildsCounter.builds_history_limit_31
    limit_per_page = BuildsCounter.builds_history_page_limit
    expected_builds_on_second_page = total_builds - limit_per_page
    expected_build_number_on_the_second_page = "#1"

    pipeline_name = trigger_builds_31
    pipeline_page: PipelinePage = main_page.go_to_pipeline_page(pipeline_name)

    builds_on_first_page = len(pipeline_page.get_builds_list())

    assert builds_on_first_page == limit_per_page, \
        f"Expected {limit_per_page} builds on the first page, but got {builds_on_first_page}."
    assert pipeline_page.get_next_page_button().is_displayed(), "Next page button is not displayed when it should be."
    assert pipeline_page.get_next_page_button().is_enabled(), "Next page button is not enabled when it should be."
    assert pipeline_page.get_previous_page_button().is_displayed(), \
        "Previous page button is not displayed when it should be."
    assert pipeline_page.get_previous_page_button().get_attribute("class").endswith("disabled"), \
        "Previous page button does not have a 'disabled' class as expected."

    builds_on_second_page = len(pipeline_page.click_next_page_button().get_builds_list())
    build_number = pipeline_page.get_single_build_number()

    assert builds_on_second_page == expected_builds_on_second_page, \
        f"Expected {expected_builds_on_second_page} builds on the second page, but got {builds_on_second_page}."
    assert build_number == expected_build_number_on_the_second_page
    assert pipeline_page.get_next_page_button().is_displayed(), "Next page button is not displayed when it should be."
    assert pipeline_page.get_next_page_button().get_attribute("class").endswith("disabled"), \
        "Next page button does not have a 'disabled' class as expected."
    assert pipeline_page.get_previous_page_button().is_displayed(), \
        "Previous page button is not displayed when it should be."
    assert pipeline_page.get_previous_page_button().is_enabled(), \
        "Previous page button is not enabled when it should be."

    builds_on_the_first_page_when_return = len(pipeline_page.click_previous_page_button().get_builds_list())

    assert builds_on_the_first_page_when_return == limit_per_page, \
        f"Expected {limit_per_page} builds on the first page, but got {builds_on_first_page}."
    assert pipeline_page.get_next_page_button().is_displayed(), "Next page button is not displayed when it should be."
    assert pipeline_page.get_next_page_button().is_enabled(), "Next page button is not enabled when it should be."
    assert pipeline_page.get_previous_page_button().is_displayed(), \
        "Previous page button is not displayed when it should be."
    assert pipeline_page.get_previous_page_button().get_attribute("class").endswith("disabled"), \
        "Previous page button does not have a 'disabled' class as expected."
