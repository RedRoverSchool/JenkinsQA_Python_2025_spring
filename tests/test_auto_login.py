from _ast import Assert

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from faker import Faker


@pytest.fixture
def auto_login(driver):
    driver.get("http://automationexercise.com")
    return driver


def test_register_user(auto_login):


    auto_login.get("https://www.automationexercise.com/")
    newUserSignup = auto_login.find_element(By.CSS_SELECTOR,  '.nav a[href="/"]')
    assert newUserSignup.is_displayed() , "User signup display is not visible"

    auto_login.quit()