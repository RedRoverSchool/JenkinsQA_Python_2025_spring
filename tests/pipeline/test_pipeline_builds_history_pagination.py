import time


def test_pipeline_builds_history_pagination(create_pipeline_with_script):
    pipeline_page = create_pipeline_with_script
    pipeline_page.click_build_now_button()
    time.sleep(60)

