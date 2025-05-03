import time
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_new_freestyle_with_description(main_page):
    main_page.find_element(By.LINK_TEXT, "Create a job").click()
    wait3 = WebDriverWait(main_page, 3)
    wait3.until(EC.element_to_be_clickable((By.CLASS_NAME, "jenkins-input"))).send_keys("New Project")
    wait3.until(EC.element_to_be_clickable((By.CLASS_NAME, "hudson_model_FreeStyleProject"))).click()
    wait3.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()
    wait3.until(EC.presence_of_element_located((By.NAME, "description"))).send_keys("Description")
    wait3.until(EC.element_to_be_clickable((By.CLASS_NAME, "textarea-show-preview"))).click()
    wait3.until(EC.element_to_be_clickable((By.CLASS_NAME, "textarea-hide-preview"))).click()
    wait3.until(EC.element_to_be_clickable((By.CLASS_NAME, "jenkins-submit-button"))).click()

    assert main_page.find_element(By.ID, "description").text == "Description"
    assert main_page.find_element(By.ID, "description").is_displayed()


