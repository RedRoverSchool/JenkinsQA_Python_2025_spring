from tests.new_item.data import new_folder_name, new_pipeline_name, new_multi_config_project_name


def test_all_jobs_and_folders_visible_in_dashboard(create_job_and_folders_env, main_page):
    items = main_page.get_item_list()
    assert new_multi_config_project_name in items, "Multi-conf project should be visible on Dashboard"
    assert new_folder_name in items, "Folder should be visible on Dashboard"
    assert new_pipeline_name not in items, "Pipeline job should only be visible inside its folder"

    folder_contents = main_page.go_to_the_folder_page(new_folder_name).get_item_list()
    assert new_pipeline_name in folder_contents, "Pipeline job should be visible when opening its folder"
