import time

from core.jenkins_utils import remote_build_trigger
from tests.pipeline.pipeline_data import BuildCounter, pipeline_project_name


def test_pipeline_builds_history_pagination(create_multiple_builds, driver):
    count = BuildCounter.build_history_limit_31
    pipeline_page = create_multiple_builds
    assert len(pipeline_page.get_builds_list(count)) == 30

    # assert pipeline_page.get_next_page_button().

    # pipeline_page.click_builds_next_page_button()
    time.sleep(120)
