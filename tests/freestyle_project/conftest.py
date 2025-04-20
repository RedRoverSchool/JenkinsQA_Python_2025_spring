import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def freestyle(main_page, config):
    wait5 = WebDriverWait(main_page, 5)
    wait5.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/view/all/newJob"]'))).click()
    # main_page.find_element(By.CSS_SELECTOR, 'a[href="/view/all/newJob"]').click()
    wait5.until(EC.presence_of_element_located((By.ID, 'name'))).send_keys("New Freestyle Project")
    main_page.find_elements(By.CSS_SELECTOR, '.j-item-options>li[tabindex="0"]')[0].click()
    main_page.find_element(By.ID, 'ok-button').click()
    wait5.until(EC.url_changes(config.jenkins.base_url + "/view/all/newJob"))

    return freestyle