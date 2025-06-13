import pytest
import allure

from tests.pipeline.pipeline_data import pipeline_project_name, BuildTriggers
from pages.pipeline_config_page import PipelineConfigPage


@pytest.fixture(scope="function")
def pipeline_config_page(main_page):
    pipeline_config_page = main_page.go_to_new_item_page().create_new_pipeline_project(pipeline_project_name)
    pipeline_config_page.wait_for_element(PipelineConfigPage.Locators.DESCRIPTION_FIELD, 10)
    return pipeline_config_page


@pytest.fixture(scope="function")
@allure.title("Create Pipeline project")
def pipeline_project_config_page(new_item_page) -> PipelineConfigPage:
    return new_item_page.create_new_pipeline_project(BuildTriggers.PROJECT_NAME)


@pytest.fixture(scope="function")
@allure.title("Prepare a configuration page with trigger checkboxes enabled")
def pipeline_config_page_enable_trigger_checkboxes(pipeline_project_config_page) -> PipelineConfigPage:
    return pipeline_project_config_page.click_trigger_labels()


@pytest.fixture(scope="function")
@allure.title("Prepare a configuration page with the 'Build after other projects are built' trigger checkbox enabled")
def pipeline_config_page_enable_build_after_checkbox(pipeline_project_config_page) -> PipelineConfigPage:
    return pipeline_project_config_page.click_trigger_build_after_other_projects()
