import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function", autouse=True)
def browser():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_browser(browser):
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    import time
    time.sleep(3)
    button = browser.find_element(By.XPATH, "//input[@name='username']")
    button.send_keys("Admin")
    button = browser.find_element(By.XPATH, "//input[@name='password']")
    button.send_keys("admin123")
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
    time.sleep(3)
    assert "Dashboard" in browser.page_source