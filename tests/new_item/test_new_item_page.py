from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.new_item_page import NewItemPage


def test_new_item_page_accessibility(driver, config, main_page, new_item_page):
    login_page = LoginPage(driver)
    login_page.open()
    main_page = login_page.login(config.jenkins.USERNAME, config.jenkins.PASSWORD)

    new_item_page = main_page.go_to_new_item_page()
    assert new_item_page.is_name_input_displayed()
