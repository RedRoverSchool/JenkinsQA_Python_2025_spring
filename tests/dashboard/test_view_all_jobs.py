import allure

from tests.dashboard.data import DashboardTable
from tests.new_item.data import new_folder_name, new_pipeline_name, new_multi_config_project_name


@allure.epic("Dashboard with the items")
@allure.story("View All Jobs")
@allure.title("Display list of jobs and folders")
@allure.description("Verify that all jobs and folders are listed on the Dashboard page.")
@allure.testcase("TC_12.001.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/688", name="Github issue")
def test_all_jobs_and_folders_visible_in_dashboard(create_job_and_folders_env, main_page):
    items = main_page.get_item_list()
    assert new_multi_config_project_name in items, "Multi-conf project should be visible on Dashboard"
    assert new_folder_name in items, "Folder should be visible on Dashboard"
    assert new_pipeline_name not in items, "Pipeline job should only be visible inside its folder"

    folder_contents = main_page.go_to_the_folder_page(new_folder_name).get_item_list()
    assert new_pipeline_name in folder_contents, "Pipeline job should be visible when opening its folder"


@allure.epic("Dashboard with the items")
@allure.story("View All Jobs")
@allure.title("Verification of column headers in dashboard table")
@allure.description("Verify the dashboard table displays correct abbreviated column headers.")
@allure.testcase("TC_12.001.02")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/742", name="Github issue")
def test_verify_table_column_headers(create_job_pipeline_env, main_page):
    actual_headers = main_page.get_table_headers_list()
    with allure.step("Load expected headers configuration"):
        expected_headers = list(DashboardTable.HEADERS_MAP.values())
    with allure.step("Verify headers presence"):
        assert actual_headers, "No headers found in the table (empty list)"
    with allure.step("Validate headers format and order"):
        assert actual_headers == expected_headers, \
            f"Headers mismatch. Expected:{expected_headers}, actual:{actual_headers}"


@allure.epic("Dashboard with the items")
@allure.story("View All Jobs")
@allure.title("Verification of default state for job without configuration")
@allure.description("Verify that a newly created job without any build history or configuration displays the correct"
                    " default state in the dashboard jobs table.")
@allure.testcase("TC_12.001.03")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/757", name="Github issue")
def test_verify_default_state_for_all_projects(main_page, created_projects):
    allure.attach(
        main_page.driver.get_screenshot_as_png(),
        name="Dashboard view with all created projects",
        attachment_type=allure.attachment_type.PNG
    )
    for project_type, project_name in created_projects:
        actual_info = main_page.get_project_row_data(project_name)
        with allure.step(f"Load expected data for '{project_type}'"):
            expected_data = DashboardTable.DEFAULT_PROJECT_DATA_MAP[project_type].copy()
            expected_data["name"] = project_name
        with allure.step(f"Verify default state for project '{project_name}'"):
            assert actual_info == list(expected_data.values()), \
                f"Mismatch for project '{project_type}'. Expected: {list(expected_data.values())}, Actual: {actual_info}"
            assert actual_info == list(expected_data.values()), \
                f"Mismatch for project '{project_type}'. Expected: {list(expected_data.values())}, Actual: {actual_info}"
