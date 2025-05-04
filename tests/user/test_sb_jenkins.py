from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger(__name__)

def test_login(login_page):
    assert login_page.title == "Sign in [Jenkins]"

def test_main_page(main_page):
    assert main_page.title == "Dashboard [Jenkins]"

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