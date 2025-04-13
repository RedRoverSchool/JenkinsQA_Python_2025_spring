import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_fill_text_box(driver):

    input_first_name = 'Yuliya'
    input_last_name = 'Tester'
    input_phone_number = '7042223344'
    input_email = 'ytest@gmail.com'

    driver.get('https://demoqa.com/automation-practice-form')

    #driver.find_element(By.CLASS_NAME, 'btn btn-light active').click()
    driver.find_element(By.ID, 'firstName').send_keys(input_first_name)
    driver.find_element(By.ID, 'lastName').send_keys(input_last_name)
    driver.find_element(By.ID, 'userEmail').send_keys(input_email)
    driver.find_element(By.XPATH, "//label[text()='Female']").click()
    #driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-2']").click()
    driver.find_element(By.ID, 'userNumber').send_keys(input_phone_number)
    submit_btn = driver.find_element(By.ID, 'submit')
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    submit_btn.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
    output_full_name = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//td[text()='Student Name']/following-sibling::td")
    )).text
    output_email = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//td[text()='Student Email']/following-sibling::td")
    )).text
    output_phone_number = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//td[text()='Mobile']/following-sibling::td")
    )).text

    assert f"{input_first_name} {input_last_name}" in output_full_name
    assert f"{input_email}" in output_email
    assert f"{input_phone_number}" in output_phone_number



