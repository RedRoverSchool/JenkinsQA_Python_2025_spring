import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

LOGIN_PAGE = "https://www.saucedemo.com/"
PRODUCT_PAGE = "https://www.saucedemo.com/inventory.html"

STANDARD_USER_NAME = "standard_user"
LOCKED_OUT_USER_NAME = "locked_out_user"
VALID_PASSWORD = "secret_sauce"
INVALID_PASSWORD = "secret"

USER_NAME_FIELD = (By.ID, "user-name")
PASSWORD_FIELD = (By.ID, "password")
LOGIN_BUTTON = (By.NAME, "login-button")
OPEN_MENU_BUTTON = (By.XPATH, "//button[text()='Open Menu']")


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.delete_all_cookies()
    driver.implicitly_wait(10)
    yield driver


def test_login(driver):
    driver.get(LOGIN_PAGE)
    driver.find_element(*USER_NAME_FIELD).send_keys(STANDARD_USER_NAME)
    driver.find_element(*PASSWORD_FIELD).send_keys(VALID_PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()

    assert driver.current_url == PRODUCT_PAGE


def test_locked_out_user(driver):
    driver.get(LOGIN_PAGE)
    driver.find_element(*USER_NAME_FIELD).send_keys(LOCKED_OUT_USER_NAME)
    driver.find_element(*PASSWORD_FIELD).send_keys(VALID_PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()

    error_message = driver.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert error_message.text == "Epic sadface: Sorry, this user has been locked out."


def test_invalid_password(driver):
    driver.get(LOGIN_PAGE)

    driver.find_element(*USER_NAME_FIELD).send_keys(STANDARD_USER_NAME)
    driver.find_element(*PASSWORD_FIELD).send_keys(INVALID_PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()

    error_message = driver.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert (
            error_message.text
            == "Epic sadface: Username and password do not match any user in this service"
    )


def test_empty_username_field(driver):
    driver.get(LOGIN_PAGE)
    driver.find_element(*PASSWORD_FIELD).send_keys(VALID_PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()

    error_message = driver.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert error_message.text == "Epic sadface: Username is required"


def test_empty_password_field(driver):
    driver.get(LOGIN_PAGE)
    driver.find_element(*USER_NAME_FIELD).send_keys(STANDARD_USER_NAME)
    driver.find_element(*LOGIN_BUTTON).click()

    error_message = driver.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert error_message.text == "Epic sadface: Password is required"


def test_empty_username_password_fields(driver):
    driver.get(LOGIN_PAGE)
    driver.find_element(*LOGIN_BUTTON).click()

    error_message = driver.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert error_message.text == "Epic sadface: Username is required"


def test_open_sidebar_menu(driver):
    driver.get(LOGIN_PAGE)
    driver.find_element(*USER_NAME_FIELD).send_keys(STANDARD_USER_NAME)
    driver.find_element(*PASSWORD_FIELD).send_keys(VALID_PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()
    driver.find_element(*OPEN_MENU_BUTTON).click()

    assert driver.find_element(By.XPATH, "// a[text() = 'About']")


def test_logout(driver):
    wait = WebDriverWait(driver, 5)

    driver.get(LOGIN_PAGE)
    wait.until(EC.visibility_of_element_located(USER_NAME_FIELD)).send_keys(
        STANDARD_USER_NAME
    )

    wait.until(EC.visibility_of_element_located(PASSWORD_FIELD)).send_keys(
        VALID_PASSWORD
    )
    wait.until(EC.visibility_of_element_located(LOGIN_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(OPEN_MENU_BUTTON)).click()

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='Logout']"))
    ).click()

    assert driver.current_url == LOGIN_PAGE


def test_add_item_to_cart(driver):
    driver.get(LOGIN_PAGE)

    driver.find_element(*USER_NAME_FIELD).send_keys(STANDARD_USER_NAME)
    driver.find_element(*PASSWORD_FIELD).send_keys(VALID_PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]").click()
    driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()

    assert driver.current_url == "https://www.saucedemo.com/cart.html"


def test_check_item_in_cart(driver):
    driver.get(LOGIN_PAGE)

    driver.find_element(*USER_NAME_FIELD).send_keys(STANDARD_USER_NAME)
    driver.find_element(*PASSWORD_FIELD).send_keys(VALID_PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()
    driver.find_element(
        By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']"
    ).click()
    driver.find_element(By.XPATH, "//a[@class = 'shopping_cart_link']").click()

    assert driver.find_element(
        By.XPATH,
        "//div[text()='Sauce Labs Backpack']/ancestor::div[@class='cart_item']",
    )


def test_open_item(driver):
    driver.get(LOGIN_PAGE)

    driver.find_element(*USER_NAME_FIELD).send_keys(STANDARD_USER_NAME)
    driver.find_element(*PASSWORD_FIELD).send_keys(VALID_PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()
    driver.find_element(
        By.XPATH, "//div[contains(text(),'Sauce Labs Fleece Jacket')]"
    ).click()

    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=5"
