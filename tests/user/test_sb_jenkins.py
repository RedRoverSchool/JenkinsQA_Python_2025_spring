import style
from selenium.webdriver.common.by import By
import time
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger(__name__)

def test_login(login_page):
    assert login_page.title == "Sign in [Jenkins]"


def test_main_page(main_page):
    assert main_page.title == "Dashboard [Jenkins]"

def test_create_job(main_page):
    main_page.find_element(By.CLASS_NAME, 'content-block__link').click()
    search_input = (main_page.find_element(By.CLASS_NAME, 'jenkins-input'))
    search_input.send_keys("TEST")
    time.sleep(10)
    value = search_input.get_attribute("value")
    assert value is not None and value.strip() != ""
    logger.info(style)

def test_description_account(main_page):
    wait = WebDriverWait(main_page, 5)
    test_description_name = "test description"
    main_page.find_element(By.XPATH, '//header//span[contains(@class, "hidden-xs")]').click()
    main_page.find_element(By.XPATH, '//a[contains(@href, "account")]').click()
    description_field = main_page.find_element(By.XPATH, '//textarea[@name="_.description"]')
    description_field.clear()
    description_field.send_keys(test_description_name)
    main_page.find_element(By.XPATH, '//button[@name="Submit"]').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "account")]')))
    main_page.find_element(By.XPATH, '//a[contains(@href, "account")]').click()
    description_field = main_page.find_element(By.XPATH, '//textarea[@name="_.description"]')
    description_field_value = description_field.get_attribute("value")

    assert description_field_value == test_description_name


def test_error_message_create_user(main_page):
    main_page.find_element(By.XPATH, '//a[contains(@href, "manage")]').click()
    main_page.find_element(By.XPATH, '//a[contains(@href, "securityRealm")]').click()
    main_page.find_element(By.XPATH, '//a[contains(@href, "addUse")]').click()
    main_page.find_element(By.ID, 'username').send_keys("Vika")
    main_page.find_element(By.CSS_SELECTOR, "input[name='password1']").send_keys("1234567")
    main_page.find_element(By.NAME, 'password2').send_keys("123456")
    main_page.find_element(By.NAME, 'email').send_keys("astra@gmail.com")
    main_page.find_element(By.NAME, 'Submit').click()
    wait = WebDriverWait(main_page, 5)

    error_message = main_page.find_element(By.XPATH, "//div[@class='error jenkins-!-margin-bottom-2']")
    assert error_message.text == "Password didn't match"