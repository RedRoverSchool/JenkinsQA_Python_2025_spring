from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_enabled_disable_freestyle_project(freestyle, main_page):
    is_enable = main_page.find_element(By.CLASS_NAME, 'jenkins-toggle-switch__label__checked-title')

    assert is_enable.is_displayed()

    is_enable.click()
    is_disable = main_page.find_element(By.CLASS_NAME, 'jenkins-toggle-switch__label__unchecked-title')
    WebDriverWait(main_page, 5).until(EC.visibility_of(is_disable))

    assert is_disable.is_displayed()
