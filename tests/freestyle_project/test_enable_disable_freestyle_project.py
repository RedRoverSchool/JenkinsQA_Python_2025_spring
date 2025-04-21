from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_enabled_disable_freestyle_project(freestyle, main_page):
    wait5 = WebDriverWait(main_page, 5)
    is_enable = main_page.find_element(By.CLASS_NAME, 'jenkins-toggle-switch__label__checked-title')

    assert is_enable.is_displayed()

    is_enable.click()
    is_disable = main_page.find_element(By.CLASS_NAME, 'jenkins-toggle-switch__label__unchecked-title')
    wait5.until(EC.visibility_of(is_disable))

    assert is_disable.is_displayed()

    main_page.find_element(By.XPATH, '//button[@name="Submit"]').click()
    wait5.until(EC.presence_of_element_located((By.XPATH, '//button[@name="Submit"]')))
    status_text = main_page.find_element(By.XPATH, '//div[@class="warning"]').text.splitlines()

    assert status_text[0] == "This project is currently disabled"

    main_page.find_element(By.XPATH, '//button[@name="Submit"]').click()
    wait5.until(EC.presence_of_element_located((By.LINK_TEXT, 'Build Now')))
    menu = main_page.find_elements(By.XPATH, '//span[@class="task-icon-link"]')
    menu[4].click()
    wait5.until(EC.presence_of_element_located((By.XPATH, '//label[@class="jenkins-toggle-switch__label "]')))
    is_enable_text = main_page.find_element(By.XPATH, '//label[@class="jenkins-toggle-switch__label "]').text

    assert is_enable_text == "Enabled"
