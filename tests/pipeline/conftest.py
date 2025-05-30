import pytest

from tests.pipeline.pipeline_data import pipeline_project_name, BuildTriggers
from pages.pipeline_config_page import PipelineConfigPage


@pytest.fixture(scope="function")
def pipeline_config_page(main_page):
    pipeline_config_page = main_page.go_to_new_item_page().create_new_pipeline_project(pipeline_project_name)
    pipeline_config_page.wait_for_element(PipelineConfigPage.Locators.DESCRIPTION_FIELD, 10)
    return pipeline_config_page


@pytest.fixture(scope="function")
def pipline_project_config_page(new_item_page) -> PipelineConfigPage:
    return new_item_page.create_new_pipeline_project(BuildTriggers.PROJECT_NAME)
