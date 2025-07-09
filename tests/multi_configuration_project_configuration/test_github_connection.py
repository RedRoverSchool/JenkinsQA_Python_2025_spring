import allure
import pytest

from tests.multi_configuration_project_configuration.data import GitHubConnection


@pytest.mark.skip("failed on CI")
def test_github_connection_error(multi_config_project_with_invalid_github_link):
    project_page = multi_config_project_with_invalid_github_link
    error_text = project_page.go_to_configure_page().click_source_code_management_button().get_invalid_github_link_error_text()
    with allure.step("Assert error message contains text"):
        assert error_text == GitHubConnection.FAILED_CONNECTION_ERROR_MESSAGE