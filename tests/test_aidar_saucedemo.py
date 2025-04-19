import time, pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def sauce_site(driver):
    driver.get("https://www.saucedemo.com/")
    return driver


def test_locked_out_user_error_message(sauce_site):

    sauce_site.find_element(By.ID, "user-name").send_keys("locked_out_user")
    time.sleep(1)
    sauce_site.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    sauce_site.find_element(By.ID, "login-button").click()

    error_message = sauce_site.find_element(By.XPATH, "//h3[@data-test='error']")
    assert error_message.text == "Epic sadface: Sorry, this user has been locked out."

def test_locked_out_user_url_check(sauce_site):

    sauce_site.find_element(By.ID, "user-name").send_keys("locked_out_user")
    time.sleep(1)
    sauce_site.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    sauce_site.find_element(By.ID, "login-button").click()

    assert sauce_site.current_url == "https://www.saucedemo.com/", "wrong url"

@pytest.mark.new
def test_problem_user(sauce_site):

    sauce_site.find_element(By.ID, "user-name").send_keys("problem_user")
    time.sleep(1)
    sauce_site.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    sauce_site.find_element(By.ID, "login-button").click()

@pytest.mark.new
def test_problem_user_image(sauce_site):

    sauce_site.find_element(By.ID, "user-name").send_keys("problem_user")
    time.sleep(1)
    sauce_site.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    sauce_site.find_element(By.ID, "login-button").click()

    img_item = sauce_site.find_element(By.CLASS_NAME, "inventory_item_img")

    assert img_item.get_attribute("src") != "/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg", "wrong image"

