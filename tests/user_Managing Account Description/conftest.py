import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os


load_dotenv()


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login(browser):

    username = os.getenv("JENKINS_USERNAME")
    password = os.getenv("JENKINS_PASSWORD")
    url = f"http://{os.getenv('JENKINS_HOST')}:{os.getenv('JENKINS_PORT')}"

    browser.get(url + "/login")
    browser.find_element(By.CSS_SELECTOR, "input[name='j_username'][id='j_username']").send_keys(username)
    browser.find_element(By.CSS_SELECTOR, "input[type='password'][name='j_password']").send_keys(password)
    browser.find_element(By.CLASS_NAME, "jenkins-button").click()


    WebDriverWait(browser, 10).until(
        EC.url_contains("/dashboard")
    )