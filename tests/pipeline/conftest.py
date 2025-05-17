import pytest
from tests.pipeline.pipeline_data import pipeline_project_name, Script, BuildCounter
from pages.pipeline_config_page import PipelineConfigPage


@pytest.fixture(scope="function")
def pipeline_config_page(main_page):
    pipeline_config_page = main_page.go_to_new_item_page().create_new_pipeline_project(pipeline_project_name)
    pipeline_config_page.wait_for_element(PipelineConfigPage.Locators.DESCRIPTION_FIELD, 10)
    return pipeline_config_page


@pytest.fixture(scope="function")
def create_pipeline_with_script(pipeline_config_page):
    pipeline_config_page.type_script(Script.script)
    return pipeline_config_page.click_save_button()


@pytest.fixture(scope="function")
def create_multiple_builds(create_pipeline_with_script):
    pipeline_page = create_pipeline_with_script
    builds_amount = BuildCounter.build_history_limit_31

    for i in range(builds_amount):
        pipeline_page.click_build_now_button()
        counter = len(pipeline_page.get_builds_inner_links())
        if counter == i + 1:
            continue

    return pipeline_page
