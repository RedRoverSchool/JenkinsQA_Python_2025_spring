import time

from conftest import logger
from pages.pipeline_page import PipelinePage
from tests.pipeline.pipeline_data import BuildCounter, Config


def test_pipeline_builds_history_pagination_31(create_builds):
    total_builds = BuildCounter.build_history_limit_31
    limit_per_page = BuildCounter.build_history_page_limit
    amount_to_wait = BuildCounter.amount_to_wait
    expected_builds_on_second_page = total_builds - limit_per_page

    logger.info(f"Creating {total_builds} build(s) with page limit {limit_per_page}, wait for each {amount_to_wait} builds...")
    pipeline_page: PipelinePage = create_builds(total=total_builds, start=1, amount_to_wait=amount_to_wait)

    builds_on_first_page = len(pipeline_page.get_builds_list())

    assert builds_on_first_page == limit_per_page, \
        f"Expected {limit_per_page} builds on the first page, but got {builds_on_first_page}."
    assert pipeline_page.get_next_page_button().is_displayed(), "Next page button is not displayed when it should be."
    assert pipeline_page.get_next_page_button().is_enabled(), "Next page button is not enabled when it should be."
    assert pipeline_page.get_previous_page_button().is_displayed(), \
        "Previous page button is not displayed when it should be."
    assert pipeline_page.get_previous_page_button().get_attribute("class").endswith("disabled"), \
        "Previous page button does not have a 'disabled' class as expected."

    builds_on_second_page = len(pipeline_page.click_next_page_button().scroll_to_the_top_of_builds_list().get_builds_list())

    assert builds_on_second_page == expected_builds_on_second_page, \
        f"Expected {expected_builds_on_second_page} builds on the second page, but got {builds_on_second_page}."
    assert pipeline_page.get_next_page_button().is_displayed(), "Next page button is not displayed when it should be."
    assert pipeline_page.get_next_page_button().get_attribute("class").endswith("disabled"), \
        "Next page button does not have a 'disabled' class as expected."
    assert pipeline_page.get_previous_page_button().is_displayed(), \
        "Previous page button is not displayed when it should be."
    assert pipeline_page.get_previous_page_button().is_enabled(), \
        "Previous page button is not enabled when it should be."


def test_pipeline_builds_history_pagination_31_api(trigger_builds):
    total_builds = BuildCounter.build_history_limit_31
    limit_per_page = BuildCounter.build_history_page_limit
    expected_builds_on_second_page = total_builds - limit_per_page

    pipeline_page = trigger_builds

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

    assert builds_on_second_page == expected_builds_on_second_page, \
        f"Expected {expected_builds_on_second_page} builds on the second page, but got {builds_on_second_page}."
    assert pipeline_page.get_next_page_button().is_displayed(), "Next page button is not displayed when it should be."
    assert pipeline_page.get_next_page_button().get_attribute("class").endswith("disabled"), \
        "Next page button does not have a 'disabled' class as expected."
    assert pipeline_page.get_previous_page_button().is_displayed(), \
        "Previous page button is not displayed when it should be."
    assert pipeline_page.get_previous_page_button().is_enabled(), \
        "Previous page button is not enabled when it should be."
