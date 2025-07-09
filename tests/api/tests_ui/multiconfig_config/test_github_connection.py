import allure

from tests.api.tests_ui.multiconfig_config.data import GitHubConnection, project_name


def test_github_connection_error(create_multiconfig_project_invalid_github_link_api, main_page):
    project_page = main_page.go_to_multiconfig_project_page(project_name)
    error_text = project_page.go_to_configure_page().click_source_code_management_button().get_invalid_github_link_error_text()
    with allure.step("Assert error message contains text"):
        assert error_text == GitHubConnection.FAILED_CONNECTION_ERROR_MESSAGE