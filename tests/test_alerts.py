import pytest
from core.settings import Config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def config():
    return Config.load()

@pytest.fixture(scope="function")
def driver(config):
    match config.browser.NAME:
        case "chrome":
            from selenium.webdriver.chrome.options import Options
            options = Options()
            options.page_load_strategy="none"
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

@pytest.fixture
def alerts(driver):
    driver.get("https://demoqa.com/alerts")
    return driver

def test_see_alert(alerts):
    waiter5 = WebDriverWait(alerts, 5)
    waiter5.until(EC.visibility_of_element_located((By.ID, "alertButton")))
    alerts.find_element(By.ID, "alertButton").click()

    assert alerts.switch_to.alert.text == "You clicked a button", "Alert isn't present"

def test_timer_alert(alerts):
    waiter10 = WebDriverWait(alerts, 10)
    waiter5 = WebDriverWait(alerts, 5)
    waiter5.until(EC.visibility_of_element_located((By.ID, "timerAlertButton")))
    alerts.find_element(By.ID, "timerAlertButton").click()
    waiter10.until(EC.alert_is_present())

    assert alerts.switch_to.alert.text == "This alert appeared after 5 seconds", "Alert isn't present"

def test_confirm_box_alert(alerts):
    waiter5 = WebDriverWait(alerts, 5)
    waiter5.until(EC.visibility_of_element_located((By.ID, "confirmButton")))
    alerts.find_element(By.ID, "confirmButton").click()
    alert = alerts.switch_to.alert

    assert alert.text == "Do you confirm action?", "Confirm box isn't present"

    alert.accept()
    confirm_text = alerts.find_element(By.ID, "confirmResult").text

    assert confirm_text == "You selected Ok"

def test_prompt_box(alerts):
    waiter5 = WebDriverWait(alerts, 5)
    waiter5.until(EC.visibility_of_element_located((By.ID, "promtButton")))
    test_text = "Testing prompt box..."
    alerts.find_element(By.ID, "promtButton").click()

    assert alerts.switch_to.alert.text == "Please enter your name", "Prompt box isn't present"

    alert = alerts.switch_to.alert
    alert.send_keys(test_text)
    alert.accept()
    confirm_text = alerts.find_element(By.ID, "promptResult").text

    assert confirm_text == f"You entered {test_text}"