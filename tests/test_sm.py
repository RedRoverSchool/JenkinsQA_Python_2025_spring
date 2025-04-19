import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common import NoSuchElementException
from selenium.webdriver.ie.webdriver import WebDriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://quotes.toscrape.com/")
    yield driver
    driver.quit()

def test_login(driver: WebDriver):
    driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()
    driver.find_element(By.ID, "username").send_keys("aaa")
    driver.find_element(By.ID, "password").send_keys("123")
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    time.sleep(3)
    logout = driver.find_element(By.CSS_SELECTOR, "a[href='/logout']")
    assert logout.text == "Logout"