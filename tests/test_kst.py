import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

load_dotenv()

JENKINS_USER = os.getenv("JENKINS_USER")
JENKINS_PASSWORD = os.getenv("JENKINS_PASSWORD")


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


def login(driver):
    driver.get('http://localhost:8080/')
    driver.find_element(By.NAME, "j_username").send_keys(JENKINS_USER)
    driver.find_element(By.NAME, "j_password").send_keys(JENKINS_PASSWORD + Keys.RETURN)


def test_login(driver):
    login(driver)
    assert "Dashboard" in driver.title or "Jenkins" in driver.title, "there is no dashboard and jenkins"


def test_create_job_link_visible(driver):
    login(driver)
    create_link = driver.find_element(By.XPATH, "//a[contains(@href, 'newJob')]")
    assert create_link.is_displayed(), "created job is not displayed"



