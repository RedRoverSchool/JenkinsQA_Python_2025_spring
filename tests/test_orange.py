import pytest
from selenium.webdriver.common.by import By

@pytest.fixture
def orange(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    return driver

def test_browser(orange):
    import time
    time.sleep(3)
    button = orange.find_element(By.XPATH, "//input[@name='username']")
    button.send_keys("Admin")
    button = orange.find_element(By.XPATH, "//input[@name='password']")
    button.send_keys("admin123")
    button = orange.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
    time.sleep(3)
    assert "Dashboard" in orange.page_source