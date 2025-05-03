import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.settings import Config


LOGIN_PAGE_URL = "https://www.saucedemo.com/"
PRODUCTS_PAGE_URL = "https://www.saucedemo.com/inventory.html"


@pytest.fixture(scope="session")
def config():
    return Config.load()


@pytest.fixture(scope="function")
def driver(config):
    match config.browser.NAME:
        case "chrome":
            from selenium.webdriver.chrome.options import Options

            options = Options()
            options.add_argument("--incognito")
            for argument in config.browser.OPTIONS_CHROME.split(";"):
                options.add_argument(argument)
            driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.get(LOGIN_PAGE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()


def test_login(login, driver):
    assert driver.current_url == PRODUCTS_PAGE_URL


# @pytest.mark.xfail(reason="Expected failure due to Google password change popup")
def test_open_sidebar_menu(driver, login):
    driver.find_element(By.XPATH, "//button[text()='Open Menu']").click()
    assert driver.find_element(By.XPATH, "// a[text() = 'About']")


# @pytest.mark.xfail(reason="Expected failure due to Google password change popup")
def test_add_item_to_cart(driver, login):
    driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]").click()
    driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    WebDriverWait(driver, 5).until(EC.url_to_be("https://www.saucedemo.com/cart.html"))
    assert driver.current_url == "https://www.saucedemo.com/cart.html"


# @pytest.mark.xfail(reason="Expected failure due to Google password change popup")
def test_check_item_in_cart(driver, login):
    driver.find_element(
        By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']"
    ).click()
    driver.find_element(By.XPATH, "//a[@class = 'shopping_cart_link']").click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[text()='Sauce Labs Backpack']/ancestor::div[@class='cart_item']",
            )
        )
    )

    items = driver.find_elements(
        By.XPATH,
        "//div[text()='Sauce Labs Backpack']/ancestor::div[@class='cart_item']",
    )
    assert len(items) > 0, "Item not found in cart"


# @pytest.mark.xfail(reason="Expected failure due to Google password change popup")
def test_open_item(driver, login):
    driver.find_element(
        By.XPATH, "//div[contains(text(),'Sauce Labs Fleece Jacket')]"
    ).click()

    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=5"


def test_locked_out_user(driver):
    driver.get(LOGIN_PAGE_URL)
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()

    error_message = driver.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert error_message.text == "Epic sadface: Sorry, this user has been locked out."


def test_invalid_password(driver):
    driver.get(LOGIN_PAGE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret")
    driver.find_element(By.NAME, "login-button").click()

    error_message = driver.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert (
        error_message.text
        == "Epic sadface: Username and password do not match any user in this service"
    )


def test_empty_username_field(driver):
    driver.get(LOGIN_PAGE_URL)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()

    error_message = driver.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert error_message.text == "Epic sadface: Username is required"


def test_empty_password_field(driver):
    driver.get(LOGIN_PAGE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.NAME, "login-button").click()

    error_message = driver.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert error_message.text == "Epic sadface: Password is required"


def test_empty_username_password_fields(driver):
    driver.get(LOGIN_PAGE_URL)
    driver.find_element(By.NAME, "login-button").click()

    error_message = driver.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert error_message.text == "Epic sadface: Username is required"


def test_logout(driver, login):
    driver.find_element(By.XPATH, "//button[text()='Open Menu']").click()

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))
    ).click()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    ).click()

    assert driver.current_url == LOGIN_PAGE_URL
