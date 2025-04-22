from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_enabled_disable_freestyle_project(freestyle):
    wait = WebDriverWait(freestyle, 10)
    is_enable = freestyle.find_element(By.CLASS_NAME, 'jenkins-toggle-switch__label__checked-title')

    assert is_enable.is_displayed()

    is_enable.click()
    is_disable = freestyle.find_element(By.CLASS_NAME, 'jenkins-toggle-switch__label__unchecked-title')
    wait.until(EC.visibility_of(is_disable))

    assert is_disable.is_displayed()

    freestyle.find_element(By.XPATH, '//button[@name="Submit"]').click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//button[@formnovalidate="formNoValidate"]')))
    status_text = freestyle.find_element(By.XPATH, '//div[@class="warning"]').text.splitlines()

    assert status_text[0] == "This project is currently disabled"

    freestyle.find_element(By.XPATH, '//button[@name="Submit"]').click()
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Build Now')))
    freestyle.find_element(By.LINK_TEXT, 'Configure').click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//label[@class="jenkins-toggle-switch__label "]')))
    is_enable_text = freestyle.find_element(By.XPATH, '//label[@class="jenkins-toggle-switch__label "]').text

    assert is_enable_text == "Enabled"
