from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1440,900")
    options.add_argument("--window-position=0,0")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def sauce_site(driver):
    driver.get("https://www.saucedemo.com/")
    return driver

def test_locked_out_user_error_message(sauce_site):

    sauce_site.find_element(By.ID,'user-name').send_keys("locked_out_user")
    sauce_site.find_element(By.ID, 'password').send_keys("secret_sauce")
    sauce_site.find_element(By.NAME, 'login-button').click()
    error_message = sauce_site.find_element(By.XPATH,"//h3[@data-test='error']")
    assert error_message.text == "Epic sadface: Sorry, this user has been locked out.", "Ожидалось сообщение об ошибки о блокировки юзера"

def test_locked_out_user_url_check(sauce_site):

    sauce_site.find_element(By.ID,'user-name').send_keys("locked_out_user")
    sauce_site.find_element(By.ID, 'password').send_keys("secret_sauce")
    sauce_site.find_element(By.NAME, 'login-button').click()

    assert sauce_site.current_url == "https://www.saucedemo.com/", "wrong url"

def test_def_problem_user(sauce_site):

    sauce_site.find_element(By.ID,'user-name').send_keys("problem_user")
    sauce_site.find_element(By.ID, 'password').send_keys("secret_sauce")
    sauce_site.find_element(By.NAME, 'login-button').click()

    assert sauce_site.current_url == "https://www.saucedemo.com/inventory.html", "wrong url"

def test_added_to_cart(sauce_site):

    sauce_site.find_element(By.ID, 'user-name').send_keys("standard_user")
    sauce_site.find_element(By.ID, 'password').send_keys("secret_sauce")
    sauce_site.find_element(By.NAME, 'login-button').click()

    try:
        WebDriverWait(driver,10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
    except:
        print("Нет модального окна")

    sauce_site.find_element(By.ID,'item_4_title_link').click()
    assert sauce_site.current_url == "https://www.saucedemo.com/inventory-item.html?id=4", "wrong url"
