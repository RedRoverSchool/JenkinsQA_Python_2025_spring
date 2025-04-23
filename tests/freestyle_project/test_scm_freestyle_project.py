import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from tests.freestyle_project.freestyle_data import Freestyle


def test_scm_to_none(freestyle):
    wait = WebDriverWait(freestyle, 10)
    freestyle.find_element(By.XPATH, '//button[@name="Submit"]').click()
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Build Now'))).click()
    h1_text = freestyle.find_element(By.CSS_SELECTOR, 'h1').text

    assert h1_text == Freestyle.project_name
