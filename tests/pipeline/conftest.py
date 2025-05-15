import pytest
from tests.pipeline.pipeline_data import pipeline_project_name, script, script1
from pages.pipeline_config_page import PipelineConfigPage


@pytest.fixture(scope="function")
def pipeline_config_page(main_page):
    pipeline_config_page = main_page.go_to_new_item_page().create_new_pipeline_project(pipeline_project_name)
    pipeline_config_page.wait_for_element(PipelineConfigPage.Locators.DESCRIPTION_FIELD, 10)
    return pipeline_config_page


@pytest.fixture(scope="function")
def create_pipeline_with_script(pipeline_config_page):
    pipeline_config_page.type_script(script1)
    return pipeline_config_page.click_save_button()
