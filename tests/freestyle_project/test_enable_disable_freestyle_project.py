from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_enable_disable_switch(freestyle):
    wait = WebDriverWait(freestyle, 10)
    is_enable = freestyle.find_element(By.CLASS_NAME, 'jenkins-toggle-switch__label__checked-title')

    assert is_enable.is_displayed()

    is_enable.click()
    is_disable = freestyle.find_element(By.CLASS_NAME, 'jenkins-toggle-switch__label__unchecked-title')
    wait.until(EC.visibility_of(is_disable))

    assert is_disable.is_displayed()

def test_tooltip(tooltip):
    title = "Enable or disable the current project"

    assert tooltip == title

def test_disabled_message(disabled_message):
    warning_message = disabled_message.find_element(By.XPATH, '//div[@class="warning"]').text.splitlines()

    assert warning_message[0] == "This project is currently disabled"

def test_enable_after_disabled(enable_automatically):

    assert enable_automatically == [True, True]