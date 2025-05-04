import time

import pytest
from selenium.webdriver.support.expected_conditions import url_to_be
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_create_new_user(main_page):
    wait7 = WebDriverWait(main_page, 7)
    wait7.until(EC.element_to_be_clickable((By.LINK_TEXT, "Manage Jenkins"))).click()
    wait7.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Users"))).click()
    wait7.until(EC.element_to_be_clickable((By.CLASS_NAME, "jenkins-button--primary"))).click()
    username = "testProfile"
    wait7.until(EC.element_to_be_clickable((By.ID, "username"))).send_keys(username)
    wait7.until(EC.element_to_be_clickable((By.NAME, "password1"))).send_keys("1234")
    wait7.until(EC.element_to_be_clickable((By.NAME, "password2"))).send_keys("1234")
    wait7.until(EC.element_to_be_clickable((By.NAME, "fullname"))).send_keys("John Doe")
    wait7.until(EC.element_to_be_clickable((By.NAME, "email"))).send_keys("John.Doe@example.com")
    wait7.until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()

    assert url_to_be("http://localhost:8080/manage/securityRealm/")
    assert main_page.find_element(
        By.CSS_SELECTOR, "#people > tbody > tr:nth-child(2) > td:nth-child(2) > a"
    ).text == username

