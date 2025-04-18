import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def demo(driver):
    driver.get("https://www.demoblaze.com/")
    return driver

def test_incorrect_password(demo):
    element_login = demo.find_element(By.ID, "login2")
    demo.execute_script("arguments[0].click();", element_login)

    element_modal = WebDriverWait(demo, 10).until(
        expected_conditions.visibility_of_element_located((By.ID, "logInModal")))
    assert element_modal.is_displayed(), "Element is not displayed"

    demo.find_element(By.ID, "loginusername").send_keys("test")
    demo.find_element(By.ID, "loginpassword").send_keys("password")
    demo.find_element(By.XPATH, "//button[text()='Log in']").click()

    WebDriverWait(demo, 10).until(expected_conditions.alert_is_present())
    assert Alert(demo).text == "Wrong password.", "Incorrect alert message, expected 'Wrong password.'"
