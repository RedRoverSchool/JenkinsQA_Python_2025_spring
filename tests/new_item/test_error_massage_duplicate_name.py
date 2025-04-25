from tests.new_item.data_structs import NewItem
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import time

def test_check_error_message(new_item_page):
    wait = WebDriverWait(new_item_page, timeout=5)
    testjob = "job" + str(random.randint(1,100))
    name_field = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#name")))
    name_field.send_keys(testjob)
    new_item_page.find_element(By.CLASS_NAME, "hudson_model_FreeStyleProject").click()
    new_item_page.find_element(By.CSS_SELECTOR, "#ok-button").click()
    dashboard = WebDriverWait(new_item_page, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#breadcrumbBar  a[href="/"]')))
    dashboard.click()
    new_item_page.find_element(By.CSS_SELECTOR, "a[href='/view/all/newJob']").click()
    name_field = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#name")))
    name_field.send_keys(testjob)
    assert new_item_page.find_element(By.CSS_SELECTOR, "#itemname-invalid").text == f"» A job already exists with the name ‘{testjob}’"




