
from pages.authorizationpage import Authorization
from pages.homepage import Homepage
import time


def test_standard_user(driver):
    authorization_page = Authorization(driver)
    authorization_page.open_authorization_page()
    authorization_page.enter_standard_user_login()
    authorization_page.enter_password_for_authorization()
    authorization_page.click_to_login()

    time.sleep(2)

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    driver.quit()


def test_locked_out_user(driver):
    authorization_page = Authorization(driver)
    authorization_page.open_authorization_page()
    authorization_page.enter_locked_out_user_login()
    authorization_page.enter_password_for_authorization()
    authorization_page.click_to_login()

    time.sleep(2)

    authorization_page.check_title_is_locked_out_user_login("Epic sadface: Sorry, this user has been locked out.")
    driver.quit()


def test_problem_user(driver):
    authorization_page = Authorization(driver)
    authorization_page.open_authorization_page()
    authorization_page.enter_problem_user_login()
    authorization_page.enter_password_for_authorization()
    authorization_page.click_to_login()

    time.sleep(2)

    home_page = Homepage(driver)
    home_page.count_img_on_homepage(6)
    driver.quit()


def test_performance_glitch_user(driver):
    authorization_page = Authorization(driver)
    authorization_page.open_authorization_page()
    authorization_page.enter_performance_glitch_user_login()
    authorization_page.enter_password_for_authorization()
    authorization_page.click_to_login()

    time.sleep(2)

    home_page = Homepage(driver)
    home_page.add_product_to_cart()
    driver.quit()


def test_error_user(driver):
    authorization_page = Authorization(driver)
    authorization_page.open_authorization_page()
    authorization_page.enter_error_user_login()
    authorization_page.enter_password_for_authorization()
    authorization_page.click_to_login()

    time.sleep(2)

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    driver.quit()


def test_visual_user(driver):
    authorization_page = Authorization(driver)
    authorization_page.open_authorization_page()
    authorization_page.enter_visual_user_login()
    authorization_page.enter_password_for_authorization()
    authorization_page.click_to_login()

    time.sleep(2)

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    driver.quit()
