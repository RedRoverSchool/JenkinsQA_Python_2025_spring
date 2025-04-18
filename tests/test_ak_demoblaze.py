import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def demoblaze_page(driver):
    driver.get("https://www.demoblaze.com/")
    return driver


def test_incorrect_password(demoblaze_page):
    wait = WebDriverWait(demoblaze_page, 10)

    element_login = demoblaze_page.find_element(By.ID, "login2")
    element_login.click()
    element_modal = wait.until(
        expected_conditions.visibility_of_element_located((By.ID, "logInModal")))

    assert element_modal.is_displayed(), "Element is not displayed"

    demoblaze_page.find_element(By.ID, "loginusername").send_keys("test")
    demoblaze_page.find_element(By.ID, "loginpassword").send_keys("password")
    demoblaze_page.find_element(By.XPATH, "//button[text()='Log in']").click()
    wait.until(expected_conditions.alert_is_present())

    assert Alert(demoblaze_page).text == "Wrong password.", "Incorrect alert message, expected 'Wrong password.'"
