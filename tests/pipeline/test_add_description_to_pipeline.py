import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

load_dotenv()


def test_account_profile():
    driver = webdriver.Chrome()
    try:
        driver.get(f"http://{os.getenv('JENKINS_HOST', 'localhost')}:{os.getenv('JENKINS_PORT', '8080')}/login")

        driver.find_element(By.NAME, "j_username").send_keys(os.getenv("JENKINS_USERNAME"))
        driver.find_element(By.NAME, "j_password").send_keys(os.getenv("JENKINS_PASSWORD"))
        driver.find_element(By.NAME, "Submit").click()

        time.sleep(3)
        if "login" in driver.current_url:
            driver.save_screenshot("login_error.png")
            pytest.fail("Login failed")

        driver.find_element(By.XPATH, "//a[contains(@href, '/user/')]").click()
        driver.find_element(By.XPATH, "//a[contains(., 'Account')]").click()

        assert driver.find_element(By.NAME, "_.fullName").is_displayed()
        assert driver.find_element(By.NAME, "_.description").is_displayed()

    finally:
        driver.quit()


