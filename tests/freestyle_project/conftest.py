import allure
import uuid
import pytest
import logging

from core.jenkins_utils import remote_build_trigger
from pages.main_page import MainPage
from pages.new_item_page import NewItemPage
from pages.freestyle_project_config_page import FreestyleProjectConfigPage
from pages.freestyle_project_page import FreestyleProjectPage
from pages.freestyle_project_config_options_page import FreestylePJConfOptPage

from tests.freestyle_project.freestyle_data import Freestyle, CronTimer

logger = logging.getLogger(__name__)


@pytest.fixture
@allure.title("Prepare: Create Freestyle Project")
def freestyle(main_page) -> FreestyleProjectConfigPage:
    with allure.step("Create Freestyle Project"):
        freestyle_config_page = main_page.go_to_new_item_page().create_new_freestyle_project(Freestyle.project_name)
    with allure.step("Wait for title FreestyleProjectConfigPage"):
        freestyle_config_page.wait_for_element(FreestyleProjectConfigPage.Locators.H2_LOCATOR, 10)
    with allure.step("Return FreestyleProjectConfigPage"):
        return freestyle_config_page


@pytest.fixture
@allure.title("Create Freestyle Project")
def freestyle_config_page(new_item_page: NewItemPage) -> FreestyleProjectConfigPage:
    return new_item_page.create_new_freestyle_project(Freestyle.project_name)


@pytest.fixture(scope="function")
@allure.title("Create unique project name")
def generate_unique_project_name() -> str:
    return f"freestyle-{uuid.uuid4().hex[:8]}"


@pytest.fixture
@allure.title("Prepare: Get tooltip")
def tooltip(freestyle: FreestyleProjectConfigPage):
    with allure.step("Get tooltip"):
        return freestyle.get_tooltip(Freestyle.tooltip_enable)


@pytest.fixture
@allure.title("Prepare: make Freestyle Project Disabled")
def disabled_message(freestyle):
    with allure.step("Click Disable button"):
        freestyle.switch_to_disable()
    with allure.step("Return warning message"):
        return freestyle.click_save_button().get_warning_message().splitlines()[0]


@pytest.fixture
@allure.title("Prepare: make Freestyle Project Enabled automatically")
def enable_automatically(freestyle: FreestyleProjectConfigPage):
    from pages.freestyle_project_page import FreestyleProjectPage
    with allure.step("Make Freestyle project is disable"):
        freestyle.switch_to_disable()
    with allure.step("Save Freestyle Project as disabled"):
        project_page: FreestyleProjectPage = freestyle.click_save_button()
    with allure.step("On Freestyle Project Page click Enable button"):
        project_page.click_enable_button()
    with allure.step("Return is visible warning_message: True or False"):
        if project_page.get_warning_message() == '':
            is_warning_message_disappear = True
        else:
            is_warning_message_disappear = False
    with allure.step("Go to Freestyle Project Config Page"):
        project_config = project_page.go_to_configure()
    with allure.step("Return is Freestyle Project is enable: True or False"):
        if project_config.is_enable().is_displayed():
            is_project_enable = True
        else:
            is_project_enable = False
    return [is_warning_message_disappear, is_project_enable]


@pytest.fixture()
@allure.title("Prepare: add description")
def can_add_description(freestyle):
    with allure.step("Add description to Freestyle Projet"):
        freestyle.add_description(Freestyle.description_text)
        freestyle.click_apply_button()
    return freestyle.get_description()


@pytest.fixture()
@allure.title("Prepare: save Freestyle Project without description")
def empty_configure(freestyle):
    with allure.step("Saving Freestyle Project without description and/or scm"):
        project_page = freestyle.click_save_button()
    return project_page.get_h1_value()


@pytest.fixture()
@allure.title("Prepare for testing \"preview\" and \"hide\"")
def preview_hide(freestyle):
    with allure.step("Type text to the description field"):
        freestyle.add_description(Freestyle.description_text)
    with allure.step("Is \"preview\" button is visible"):
        preview = freestyle.is_preview_visible()
    with allure.step("Click \"preview\" button"):
        freestyle.click_preview()
    with allure.step("Is \"hide\" button is visible"):
        hide = freestyle.is_hide_preview_visible()
    with allure.step("Return list [preview, hide]"):
        return [preview, hide]


@pytest.fixture()
@allure.title("Prepare to testing is Description text appears on the Project General page")
def description_appears(freestyle):
    with allure.step("Add description to the Freestyle Project"):
        freestyle.add_description(Freestyle.description_text)
        project_page = freestyle.click_save_button()
    return project_page.get_description()


@pytest.fixture(scope="function")
@allure.title("Precondition: Generate and temporary save a new token in the User's Security Settings.")
def get_token(main_page: MainPage, config):
    security_page = main_page.header.go_to_the_user_page().go_to_security_page()
    token = security_page.generate_token(Freestyle.project_name)
    user_page = security_page.save_settings(config.jenkins.USERNAME)
    user_page.header.go_to_the_main_page()
    with allure.step(f"Generated token: \"{token}\"."):
        return token


@pytest.fixture(scope="function")
@allure.title("Precondition: Configure Freestyle project for remote builds and trigger execution via API.")
def create_freestyle_project_and_build_remotely(get_token, freestyle_config_page: FreestyleProjectConfigPage, config,
                                                driver) -> MainPage:
    auth_token = get_token
    logger.info(f"Getting auth token: {auth_token}")
    main_page: MainPage = freestyle_config_page.set_trigger_builds_remotely(auth_token).header.go_to_the_main_page()
    with allure.step("Trigger the build via API and wait for it to finish."):
        remote_build_trigger(driver, Freestyle.project_name, auth_token, config)
        logger.info(f"Triggering build for the project '{Freestyle.project_name}' via API.")
        logger.info("Waiting for the build to finish ...")
    main_page.wait_for_build_queue_executed()

    return main_page


@pytest.fixture(scope="function")
@allure.title("Configure Freestyle project with cron schedule and wait for periodic build to complete.")
def create_freestyle_project_and_build_periodically(freestyle_config_page: FreestyleProjectConfigPage):
    """
    Fixture that configures a Freestyle project to trigger builds periodically using a cron schedule.
    It waits for the scheduled build to complete.
    Returns:
        project_name
    """
    cron_schedule = CronTimer.cron_schedule_every_minute
    timeout = CronTimer.timeout[cron_schedule]

    logger.info(f"Getting cron schedule: {cron_schedule}")
    logger.info(f"Getting timeout for the cron schedule: {timeout}")

    freestyle_project_page: FreestyleProjectPage = freestyle_config_page.set_trigger_builds_periodically(cron_schedule)

    logger.info(f"Triggering build for the project '{Freestyle.project_name}' by schedule '{cron_schedule}'.")
    logger.info(f"Waiting for the build to finish (up to {timeout} sec)...")
    main_page: MainPage = freestyle_project_page.wait_for_build_execution(timeout).header.go_to_the_main_page()

    return main_page


@pytest.fixture
def freestyle_pj_conf_page(freestyle):
    return FreestylePJConfOptPage(freestyle)


@pytest.fixture
def access(freestyle) -> MainPage:
    return freestyle.navigate_to(MainPage, FreestyleProjectConfigPage.Locators.HEADER_LOGO)
