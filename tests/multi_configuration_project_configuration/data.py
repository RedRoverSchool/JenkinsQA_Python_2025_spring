description_text = "This is my overview"
project_name = "MyProject"
updated_description_text = "Updated project summary"


class ProjectToggle:
    PROJECT_NAME = "Multi-configuration project"
    WARNING_MESSAGE = "This project is currently disabled"
    STATUS_ENABLE_PROJECT = "Not built"
    STATUS_DISABLE_PROJECT = "Disabled"
    TOOLTIP = "Enable or disable the current project"


class GitHubConnection:
    INVALID_GITHUB_LINK = "https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring.git"+"1"
    FAILED_CONNECTION_ERROR_MESSAGE = f"Failed to connect to repository : Command \"git.exe ls-remote -h -- {INVALID_GITHUB_LINK} HEAD\" returned status code 128:"

