import pytest
from selenium.webdriver.support.wait import WebDriverWait

from core.settings import Config
from selenium import webdriver


@pytest.fixture(scope="session")
def config():
    return Config.load()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=15)
    return wait


@pytest.fixture(scope="function")
def driver(config):

    match config.browser.NAME:
        case "chrome":
            from selenium.webdriver.chrome.options import Options
            options = Options()
            for argument in config.browser.OPTIONS_CHROME.split(';'):
                options.add_argument(argument)
            driver = webdriver.Chrome(options=options)
        case "edge":
            from selenium.webdriver.edge.options import Options
            options = Options()
            for argument in config.browser.OPTIONS_EDGE.split(';'):
                options.add_argument(argument)
            driver = webdriver.Edge(options=options)
        case _:
            raise RuntimeError(f"Browser {config.browser.NAME} is not supported.")
    driver.implicitly_wait(3)

    yield driver

    driver.quit()

