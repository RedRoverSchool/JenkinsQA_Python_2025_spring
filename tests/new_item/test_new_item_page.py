from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_new_item_page_accessibility(main_page):
    wait = WebDriverWait(main_page, 10)
    expected_input_field_name = "Enter an item name"
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tasks"]/div[1]/span/a/span[1]'))).click()
    field_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="createItem"]/div[1]/div/label')))
    assert field_name.text == expected_input_field_name, f"field name is {field_name}, expected {expected_input_field_name}"