import time


def test_pipeline_builds_history_pagination(create_pipeline_with_script):
    pipeline_page = create_pipeline_with_script
    pipeline_page.create_multiple_builds(31)
    # pipeline_page.click_builds_next_page_button()
    time.sleep(60)
