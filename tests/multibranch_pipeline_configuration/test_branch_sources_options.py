import allure
from tests.multibranch_pipeline_configuration.mbp_data import BranchSources


def test_available_branch_source_options(multibranch_pipeline_config_page):
    multibranch_pipeline_config_page.scroll_to_branch_sources_section()
    multibranch_pipeline_config_page.click_add_source_button()

    with allure.step('Assert that current "Add source" list is equal to the expected list'):
        assert multibranch_pipeline_config_page.get_add_source_items() == BranchSources.EXPECTED_SOURCES
