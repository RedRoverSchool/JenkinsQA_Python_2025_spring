import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def authorization_jenkins():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en")

    driver = webdriver.Chrome()
    driver.get("http://localhost:8080/login?from=%2F")
    driver.find_element(By.NAME, "j_username").send_keys("admin")
    driver.find_element(By.NAME, "j_password").send_keys("admin")
    return driver


def test_login(authorization_jenkins):
    driver = authorization_jenkins
    driver.find_element(By.XPATH, "//button[@name='Submit']").click()

    assert driver.find_element(By.ID,"jenkins-name-icon")
    driver.quit()