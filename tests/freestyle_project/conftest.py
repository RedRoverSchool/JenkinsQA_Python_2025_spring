import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

@pytest.fixture(scope="function")
def freestyle(main_page, config):
    wait5 = WebDriverWait(main_page, 5)
    wait5.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/view/all/newJob"]'))).click()
    wait5.until(EC.presence_of_element_located((By.ID, 'name'))).send_keys("New Freestyle Project")
    main_page.find_elements(By.CSS_SELECTOR, '.j-item-options>li[tabindex="0"]')[0].click()
    main_page.find_element(By.ID, 'ok-button').click()
    wait5.until(EC.url_changes(config.jenkins.base_url + "/view/all/newJob"))

    return main_page

@pytest.fixture(scope="function")
def tooltip(freestyle):
    wait = WebDriverWait(freestyle, 10)
    actions = ActionChains(freestyle)
    tooltip_link = freestyle.find_element(By.XPATH, '//span[@tooltip="Enable or disable the current project"]')
    actions.move_to_element(tooltip_link).perform()
    wait.until(EC.presence_of_element_located((By.XPATH, '//span[@aria-describedby="tippy-15"]')))

    return freestyle.find_element(By.XPATH, '//div[@class="tippy-content"]').text

@pytest.fixture(scope="function")
def disabled_message(freestyle):
    wait = WebDriverWait(freestyle, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'jenkins-toggle-switch__label__checked-title')))
    freestyle.find_element(By.XPATH, '//label[@data-title="Disabled"]').click()
    freestyle.find_element(By.XPATH, '//button[@name="Submit"]').click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//form[@action="enable"]')))

    return freestyle

@pytest.fixture(scope="function")
def enable_automatically(disabled_message):
    is_warning_message_disappear = False
    is_project_enable = False
    wait = WebDriverWait(disabled_message, 2)
    disabled_message.find_element(By.XPATH, '//button[@name="Submit"]').click()
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Build Now')))
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, '//form[@action="enable"]')))
    except:
        is_warning_message_disappear = True
    disabled_message.find_element(By.LINK_TEXT, 'Configure').click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//label[@class="jenkins-toggle-switch__label "]')))
    is_enable_text = disabled_message.find_element(By.XPATH, '//label[@class="jenkins-toggle-switch__label "]').text
    if is_enable_text == "Enabled":
        is_project_enable = True

    return [is_warning_message_disappear, is_project_enable]