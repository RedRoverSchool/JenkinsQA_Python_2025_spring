import logging
import os
import subprocess
import sys

import allure
import pytest
from selenium import webdriver

from core.jenkins_utils import clear_data
from core.settings import Config
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.manage_jenkins.manage_jenkins_page import ManageJenkinsPage
from pages.manage_jenkins.status_information.load_statistics_page import LoadStatisticsPage
from pages.manage_jenkins.status_information.system_information_page import SystemInformationPage
from pages.new_item_page import NewItemPage

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

logging.getLogger('selenium.webdriver.remote.remote_connection').setLevel(logging.INFO)
logging.getLogger('faker.factory').setLevel(logging.INFO)
logger = logging.getLogger(__name__)


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     setattr(item, "rep_" + report.when, report)


@pytest.fixture(scope="session")
@allure.title("Set up config from context for test session.")
def config():
    parent_branch = f"origin/{os.getenv('github.base_ref', 'main')}"
    output = subprocess.run(["git", "-c", "core.fileMode=false", "diff", "--name-status", parent_branch],
                            stdout=subprocess.PIPE)
    for line in output.stdout.decode("utf-8").expandtabs().splitlines():
        logger.warning(line)
    return Config.load()


@pytest.fixture(scope="function", autouse=True)
@allure.title("Clear Jenkins data before each test run.")
def jenkins_reset(config):
    clear_data(config)


@pytest.fixture(scope="function")
@allure.title("Configure WebDriver with options.")
def driver(request, config):
    match config.browser.NAME:
        case "chrome":
            from selenium.webdriver.chrome.options import Options
            options = Options()
            for argument in config.browser.OPTIONS_CHROME.split(';'):
                options.add_argument(argument)
                logger.debug(f"Argument {argument} added to the chrome")
            driver = webdriver.Chrome(options=options)
        case "edge":
            from selenium.webdriver.edge.options import Options
            options = Options()
            for argument in config.browser.OPTIONS_EDGE.split(';'):
                options.add_argument(argument)
                logger.debug(f"Argument {argument} added to the edge")
            driver = webdriver.Edge(options=options)
        case _:
            raise RuntimeError(f"Browser {config.browser.NAME} is not supported.")

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
@allure.title("Get result and screenshot.")
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)

    is_failed = report.when == "call" and report.failed
    is_expected_xfail = (
        report.when == "call"
        and report.outcome == "skipped"
        and hasattr(report, "wasxfail")
        and report.wasxfail
    )

    if is_failed or is_expected_xfail:
        driver = item.funcargs.get("driver")
        if driver:
            try:
                test_name = "".join(ch for ch in item.name if ch not in r'\/:*?<>|"')
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"screenshot_{test_name}",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Failed to attach screenshot: {e}")



# @pytest.fixture(scope="function")
# @allure.title("Configure WebDriver with options and save failure screenshot.")
# def driver(request, config):
#     match config.browser.NAME:
#         case "chrome":
#             from selenium.webdriver.chrome.options import Options
#             options = Options()
#             for argument in config.browser.OPTIONS_CHROME.split(';'):
#                 options.add_argument(argument)
#                 logger.debug(f"Argument {argument} added to the chrome")
#             driver = webdriver.Chrome(options=options)
#         case "edge":
#             from selenium.webdriver.edge.options import Options
#             options = Options()
#             for argument in config.browser.OPTIONS_EDGE.split(';'):
#                 options.add_argument(argument)
#                 logger.debug(f"Argument {argument} added to the edge")
#
#             driver = webdriver.Edge(options=options)
#         case _:
#             raise RuntimeError(f"Browser {config.browser.NAME} is not supported.")
#
#     yield driver
#
#     if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
#         logger.info(f"Test {request.node.name} failed, taking screenshot...")
#         try:
#             test_name = "".join(ch for ch in request.node.name if ch not in r'\/:*?<>|"')
#             allure.attach(
#                 driver.get_screenshot_as_png(),
#                 name=test_name,
#                 attachment_type=allure.attachment_type.PNG,
#             )
#         except Exception as e:
#             logger.error(f"Failed to take screenshot: {e}")
#
#     driver.quit()


@pytest.fixture(scope="function")
@allure.title("Launch browser and open the Login Page.")
def login_page(driver) -> LoginPage:
    return LoginPage(driver).open()


@pytest.fixture(scope="function")
@allure.title("Log in with valid credentials and open the Jenkins Main Page.")
def main_page(login_page, config) -> MainPage:
    main_page = login_page.login(config.jenkins.USERNAME, config.jenkins.PASSWORD)
    return main_page


@pytest.fixture(scope="function")
@allure.title("Navigate to the New Item Page.")
def new_item_page(main_page) -> NewItemPage:
    return main_page.go_to_new_item_page()


@pytest.fixture(scope="function")
def manage_jenkins_page(main_page) -> ManageJenkinsPage:
    return main_page.go_to_manage_jenkins_page()


@pytest.fixture(scope="function")
def system_information_page(manage_jenkins_page) -> SystemInformationPage:
    return manage_jenkins_page.go_to_system_information_page()


@pytest.fixture(scope="function")
def environment_variables_tab(system_information_page) -> SystemInformationPage:
    system_information_page.click_on_environment_variables_tab()
    return system_information_page


@pytest.fixture(scope="function")
def plugins_tab(system_information_page) -> SystemInformationPage:
    system_information_page.click_on_plugins_tab()
    return system_information_page


@pytest.fixture(scope="function")
def memory_usage_tab(system_information_page) -> SystemInformationPage:
    system_information_page.click_on_memory_usage_tab()
    return system_information_page


@pytest.fixture(scope="function")
def thread_dumps_tab(system_information_page) -> SystemInformationPage:
    system_information_page.click_on_thread_dumps_tab()
    return system_information_page


@pytest.fixture(scope="function")
def load_statistics_page(manage_jenkins_page) -> LoadStatisticsPage:
    return manage_jenkins_page.go_to_load_statistics_page()
