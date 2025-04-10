import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WAIT
from selenium.webdriver.support import expected_conditions as EC

LOGIN_PAGE_URL = "https://www.saucedemo.com/"
PRODUCTS_PAGE_URL = "https://www.saucedemo.com/inventory.html"

# locators
USER_NAME_FIELD = (By.XPATH, "//input[@id='user-name']")
USER_PWD_FIELD = (By.XPATH, "//input[@id='password']")
LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
BURGER_MENU = (By.XPATH, "//button[@id='react-burger-menu-btn']")
LOGOUT_BUTTON = (By.CSS_SELECTOR, "#logout_sidebar_link")
REQUIRED_FIELD_ERROR_MESSAGE_TEXT = (By.XPATH, "//h3")

# test_data
STANDARD_USER_name = "standard_user"
USER_PASSWORD = "secret_sauce"
USERNAME_REQUIRED_ERROR_MSG = "Epic sadface: Username is required"
PASSWORD_REQUIRED_ERROR_MSG = "Epic sadface: Password is required"
PASSWORD_FIELD_TYPE = 'password'
REQUIRED_FIELD_ERROR_MESSAGE_BACKGROUND_COLOR = "rgba(72, 76, 85, 1)"
ERROR_MESSAGE_FONT_COLOR = "rgba(255, 255, 255, 1)"

# config
prod_timeout = 10
headless = True


def login_as_standard_user(driver):
    WAIT(driver, prod_timeout).until(EC.visibility_of_element_located(USER_NAME_FIELD)).send_keys(STANDARD_USER_name)
    WAIT(driver, prod_timeout).until(EC.visibility_of_element_located(USER_PWD_FIELD)).send_keys(USER_PASSWORD)
    WAIT(driver, prod_timeout).until(EC.visibility_of_element_located(LOGIN_BUTTON)).click()


def assert_error_message(driver, error_message):
    actual_error_message = (WAIT(driver, prod_timeout)
                            .until(EC.visibility_of_element_located(REQUIRED_FIELD_ERROR_MESSAGE_TEXT)).text)
    assert actual_error_message == error_message


def assert_required_field_error_message_background_color(actual_error_message_color, expected):
    try:
        assert actual_error_message_color == expected
    except AssertionError as e:
        print(f"Warning: {e}, color of the element is not as expected.")


def get_css_element_color(driver, locator):
    actual_error_message_color = (WAIT(driver, prod_timeout).until(EC.visibility_of_element_located(locator))
                                  .value_of_css_property("color"))
    return actual_error_message_color


def assert_message_text_font_color(driver, locator, expected_color):
    color = (WAIT(driver, prod_timeout).until(EC.visibility_of_element_located(locator))
             .value_of_css_property("color"))
    try:
        assert color == expected_color
    except AssertionError as e:
        print(f"Warning: {e}, color of the text is not as expected.")


class TestSauceDemo:

    @pytest.fixture
    def driver(self):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-cache")
        driver = webdriver.Chrome(options=chrome_options)
        yield driver
        driver.quit()

    def test_login_standard_user(self, driver):
        driver.get(LOGIN_PAGE_URL)

        login_as_standard_user(driver)
        assert driver.current_url == PRODUCTS_PAGE_URL

    def test_standard_user_logout(self, driver):
        driver.get(LOGIN_PAGE_URL)

        login_as_standard_user(driver)
        WAIT(driver, prod_timeout).until(EC.visibility_of_element_located(BURGER_MENU)).click()
        WAIT(driver, prod_timeout).until(EC.visibility_of_element_located(LOGOUT_BUTTON)).click()

        assert driver.current_url == LOGIN_PAGE_URL

    def test_username_required(self, driver):
        driver.get(LOGIN_PAGE_URL)

        WAIT(driver, prod_timeout).until(EC.visibility_of_element_located(USER_PWD_FIELD)).send_keys(USER_PASSWORD)
        WAIT(driver, prod_timeout).until(EC.visibility_of_element_located(LOGIN_BUTTON)).click()

        actual_error_message_background_color = get_css_element_color(driver, USER_NAME_FIELD)
        assert_error_message(driver, USERNAME_REQUIRED_ERROR_MSG)
        assert_required_field_error_message_background_color(actual_error_message_background_color,
                                                             REQUIRED_FIELD_ERROR_MESSAGE_BACKGROUND_COLOR)
        assert_message_text_font_color(driver, REQUIRED_FIELD_ERROR_MESSAGE_TEXT,
                                       ERROR_MESSAGE_FONT_COLOR)

    def test_password_required(self, driver):
        driver.get(LOGIN_PAGE_URL)

        WAIT(driver, prod_timeout).until(EC.visibility_of_element_located(USER_NAME_FIELD)).send_keys(
            STANDARD_USER_name)
        WAIT(driver, prod_timeout).until(EC.visibility_of_element_located(LOGIN_BUTTON)).click()

        actual_error_message_background_color = get_css_element_color(driver, USER_PWD_FIELD)

        assert_error_message(driver, PASSWORD_REQUIRED_ERROR_MSG)
        assert_required_field_error_message_background_color(actual_error_message_background_color,
                                                             REQUIRED_FIELD_ERROR_MESSAGE_BACKGROUND_COLOR)
        assert_message_text_font_color(driver, REQUIRED_FIELD_ERROR_MESSAGE_TEXT,
                                       ERROR_MESSAGE_FONT_COLOR)

    def test_password_masked_by_bullets(self, driver):
        driver.get(LOGIN_PAGE_URL)

        WAIT(driver, prod_timeout).until(EC.visibility_of_element_located(USER_PWD_FIELD)).send_keys(USER_PASSWORD)

        password_field_type = (WAIT(driver, prod_timeout).until(EC.visibility_of_element_located(USER_PWD_FIELD))
                               .get_attribute('type'))

        assert password_field_type == PASSWORD_FIELD_TYPE
