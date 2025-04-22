import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


# def test_enabled_disable_freestyle_project(freestyle):
#     wait = WebDriverWait(freestyle, 10)
#     is_enable = freestyle.find_element(By.CLASS_NAME, 'jenkins-toggle-switch__label__checked-title')
#
#     assert is_enable.is_displayed()
#
#     is_enable.click()
#     is_disable = freestyle.find_element(By.CLASS_NAME, 'jenkins-toggle-switch__label__unchecked-title')
#     wait.until(EC.visibility_of(is_disable))
#
#     assert is_disable.is_displayed()

def test_tooltip(freestyle):
    title = "Enable or disable the current project"
    wait = WebDriverWait(freestyle, 10)
    actions = ActionChains(freestyle)

    tooltip_link = freestyle.find_element(By.XPATH, '//span[@tooltip="Enable or disable the current project"]')
    actions.move_to_element(tooltip_link).perform()
    wait.until(EC.visibility_of(tooltip_link))
    tooltip = freestyle.find_element(By.XPATH, '//span[@aria-describedby="tippy-15"]').text
    time.sleep(5)
    print(tooltip)









# def test_disabled_message(freestyle):
#     wait = WebDriverWait(freestyle, 10)
#     wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'jenkins-toggle-switch__label__checked-title')))
#     freestyle.find_element(By.CLASS_NAME, 'jenkins-toggle-switch__label__checked-title').click()
#     wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@name="Submit"]')))
#     freestyle.find_element(By.XPATH, '//button[@name="Submit"]').click()
#     wait.until(EC.presence_of_element_located((By.XPATH, '//button[@formnovalidate="formNoValidate"]')))
#     status_text = freestyle.find_element(By.XPATH, '//div[@class="warning"]').text.splitlines()
#
#     assert status_text[0] == "This project is currently disabled"


    # freestyle.find_element(By.XPATH, '//button[@name="Submit"]').click()
    # wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Build Now')))
    # freestyle.find_element(By.LINK_TEXT, 'Configure').click()
    # wait.until(EC.presence_of_element_located((By.XPATH, '//label[@class="jenkins-toggle-switch__label "]')))
    # is_enable_text = freestyle.find_element(By.XPATH, '//label[@class="jenkins-toggle-switch__label "]').text
    #
    # assert is_enable_text == "Enabled"
