import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def alerts(driver):
    driver.get("https://demoqa.com/alerts")
    return driver

def test_see_alert(alerts):
    alerts.find_element(By.ID, "alertButton").click()

    assert alerts.switch_to.alert.text == "You clicked a button", "Alert isn't present"

def test_timer_alert(alerts):
    waiter6 = WebDriverWait(alerts, 10)
    alerts.find_element(By.ID, "timerAlertButton").click()
    waiter6.until(EC.alert_is_present())

    assert alerts.switch_to.alert.text == "This alert appeared after 5 seconds", "Alert isn't present"

def test_confirm_box_alert(alerts):
    alerts.find_element(By.ID, "confirmButton").click()
    alert = alerts.switch_to.alert

    assert alert.text == "Do you confirm action?", "Confirm box isn't present"

    alert.accept()
    confirm_text = alerts.find_element(By.ID, "confirmResult").text

    assert confirm_text == "You selected Ok"

def test_prompt_box(alerts):
    test_text = "Testing prompt box..."
    alerts.find_element(By.ID, "promtButton").click()

    assert alerts.switch_to.alert.text == "Please enter your name", "Prompt box isn't present"

    alert = alerts.switch_to.alert
    alert.send_keys(test_text)
    alert.accept()
    confirm_text = alerts.find_element(By.ID, "promptResult").text

    assert confirm_text == f"You entered {test_text}"