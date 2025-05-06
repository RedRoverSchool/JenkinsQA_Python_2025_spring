import pytest
import logging

from tests.freestyle_project.freestyle_data import Freestyle
from pages.freestyle_project_config_page import FreestyleProjectConfigPage
from core.jenkins_utils import remote_build_trigger


logger = logging.getLogger(__name__)


@pytest.fixture
def freestyle(main_page):
    freestyle_config_page = main_page.go_to_new_item_page().create_new_freestyle_project(Freestyle.project_name)
    freestyle_config_page.wait_for_element(FreestyleProjectConfigPage.Locator.H2_LOCATOR, 10)
    return freestyle_config_page

@pytest.fixture
def tooltip(freestyle: FreestyleProjectConfigPage):
    return freestyle.get_tooltip(Freestyle.tooltip_enable)

@pytest.fixture
def disabled_message(freestyle):
    freestyle.switch_to_disable()
    return freestyle.click_save_button().get_warning_message().splitlines()[0]

@pytest.fixture
def enable_automatically(freestyle: FreestyleProjectConfigPage):
    from pages.freestyle_project_page import FreestyleProjectPage
    freestyle.switch_to_disable()
    project_page: FreestyleProjectPage = freestyle.click_save_button()
    project_page.click_enable_button()
    if project_page.get_warning_message() == '':
        is_warning_message_disappear = True
    else:
        is_warning_message_disappear = False
    project_config = project_page.go_to_configure()
    if project_config.is_enable().is_displayed():
        is_project_enable = True
    else:
        is_project_enable = False
    return [is_warning_message_disappear, is_project_enable]

@pytest.fixture()
def can_add_description(freestyle):
    freestyle.add_description(Freestyle.description_text)
    freestyle.click_apply_button()
    return freestyle.get_description()

@pytest.fixture()
def empty_configure(freestyle):
    project_page = freestyle.click_save_button()
    return project_page.get_h1_value()

@pytest.fixture()
def preview_hide(freestyle):
    freestyle.add_description(Freestyle.description_text)
    preview = freestyle.is_preview_visible()
    freestyle.click_preview()
    hide = freestyle.is_hide_preview_visible()
    return [preview, hide]

@pytest.fixture()
def description_appears(freestyle):
    freestyle.add_description(Freestyle.description_text)
    project_page = freestyle.click_save_button()
    return project_page.get_description()


@pytest.fixture(scope="function")
def get_token(main_page, config):
    """
    Fixture that navigates to the user's security settings, revokes any existing
    access tokens associated with the current project (as defined by data.project_name),
    and generates a new token for that project.
    Returns:
        str: The newly generated project-specific token.
    """
    security_page = main_page.go_to_the_user_page().go_to_security_page()
    token = security_page.generate_token(Freestyle.project_name)
    user_page = security_page.save_settings(config.jenkins.USERNAME)
    user_page.go_to_the_main_page()

    return token


@pytest.fixture(scope="function")
def create_freestyle_project_and_build_remotely(get_token, freestyle, config, driver):
    """
    Fixture that configures a Freestyle project to allow remote builds,
    triggers the build using the Jenkins remote API, and waits for the build to complete.
    """
    auth_token = get_token

    freestyle.set_trigger_builds_remotely(auth_token).go_to_the_main_page()

    remote_build_trigger(driver, Freestyle.project_name, auth_token, config)
    logger.info(f"Triggered build at: {driver.current_url}")
    logger.info("Waiting for the build to finish ...")