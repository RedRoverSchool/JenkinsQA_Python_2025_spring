from _ast import Assert

import pytest
from selenium.webdriver.common.by import By



@pytest.fixture
def auto_login(driver):
    driver.get("http://automationexercise.com")
    yield driver
    driver.quit()

def test_register_user(auto_login):


    auto_login.get("https://www.automationexercise.com/")
    home = auto_login.find_element(By.CSS_SELECTOR,  '.nav a[href="/"]')
    assert home.is_displayed()
    current_url = auto_login.current_url
    expected_url ="https://www.automationexercise.com/"
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"
    print("The page is correct. Current URL:", current_url)

