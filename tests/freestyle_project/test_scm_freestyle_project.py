import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from tests.freestyle_project.freestyle_data import Freestyle


# def test_scm_to_none(empty_configure):
#
#     assert empty_configure == True

def test_tooltips(freestyle):
    actions = ActionChains(freestyle)
    wait = WebDriverWait(freestyle, 10)
    freestyle.find_element(By.XPATH, '//label[@for="radio-block-1"]').click()

    el = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="form-container tr"]//div[@class="jenkins-form-item tr"]//button')))
    # el = freestyle.find_elements(By.XPATH, '//div[@class ="advancedLink jenkins-buttons-row"]/button')

    actions.move_to_element(el.find_element(By.XPATH, '//svg[@xmlns="http://www.w3.org/2000/svg"]')).click().perform()
    # time.sleep(3)
    # el.click()
    time.sleep(3)
