import pytest
from selenium.webdriver.common.by import By
from tests.freestyle_project.data import project_name
from tests.freestyle_project.data import crumb_api


@pytest.fixture(scope="function")
def generate_token(main_page):
    """
    Fixture that navigates to the user's security settings, revokes any existing
    access tokens associated with the current project (as defined by data.project_name),
    and generates a new token for that project.

    Returns:
        str: The newly generated project-specific token.
    """
    security_page = main_page.go_to_the_user_page().go_to_security_page()
    existing_tokens = security_page.get_existing_token_list()
    if existing_tokens:
        security_page.revoke_project_tokens(project_name, existing_tokens)

    token = security_page.generate_project_token(project_name)

    user_page = security_page.save_token(security_page.get_username())
    user_page.go_to_the_main_page()

    return token


@pytest.fixture(scope="function")
def get_crumb(main_page):
    """
    Fixture that opens a new browser window, navigates to the crumb API endpoint,
    and extracts the crumb value from the response body.

    Returns:
            str: The extracted crumb value.
    """
    base_url = main_page.base_url
    main_page_window = main_page.get_current_window_handle()
    new_window = main_page.switch_to_new_window()
    new_window.get(base_url + crumb_api)

    crumb = new_window.find_element(By.CSS_SELECTOR, "body").text.split('"')[7]

    new_window.switch_to.window(main_page_window)

    return crumb
