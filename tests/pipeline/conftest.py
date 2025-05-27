import pytest

from pages.pipeline_page import PipelinePage
from pages.pipeline_config_page import PipelineConfigPage

from tests.pipeline.pipeline_data import pipeline_project_name, Script


@pytest.fixture(scope="function")
def pipeline_config_page(new_item_page) -> PipelineConfigPage:
    return new_item_page.create_new_pipeline_project(pipeline_project_name)


@pytest.fixture(scope="function")
def create_pipeline_with_script(pipeline_config_page) -> PipelinePage:
    return pipeline_config_page.type_script(Script.script).click_save_button(pipeline_project_name)


@pytest.fixture
def create_builds(create_pipeline_with_script):
    pipeline_page = create_pipeline_with_script

    def _create_builds_per_amount(total: int, start: int = 1, amount_to_wait: int = 5) -> PipelinePage:
        for i in range(start, start + total):
            pipeline_page.click_build_now_button()

            build_index = i - start + 1
            if build_index % amount_to_wait == 0 or i == total:
                pipeline_page.wait_for_build_execution(i)

        return pipeline_page

    return _create_builds_per_amount
