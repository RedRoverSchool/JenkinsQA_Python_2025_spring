import allure
import pytest

from tests.api.tests_ui.multiconfig_config.data import GitHubConnection, Config, project_name


@allure.title("API: Prepare env > Create multiconfig project")
@pytest.fixture
def create_multiconfig_project_invalid_github_link_api(jenkins_steps):
    invalid_github_link = GitHubConnection.INVALID_GITHUB_LINK
    config_xml = Config.get_multiconfig_github_link_xml(invalid_github_link)
    jenkins_steps.post_create_item(project_name, config_xml)


@allure.title("API: Prepare env > Create base multiconfig project")
@pytest.fixture
def create_multiconfig_project_api(jenkins_steps):
    jenkins_steps.post_create_item(project_name, Config.config_base_xml)


@allure.title("API: Create project with Environment options enabled")
@pytest.fixture
def create_multiconfig_project_with_env_options_delete_api(jenkins_steps):
    jenkins_steps.post_create_item(project_name, Config.config_delete_workspace_xml)


@allure.title("API: Create project with Environment options enabled")
@pytest.fixture
def create_multiconfig_project_with_env_options_use_secrets_api(jenkins_steps):
    jenkins_steps.post_create_item(project_name, Config.config_test_use_secrets_xml)


@allure.title("API: Create project with Environment options enabled")
@pytest.fixture
def create_multiconfig_project_with_env_options_add_timestamps_api(jenkins_steps):
    jenkins_steps.post_create_item(project_name, Config.config_add_timestamps_xml)
