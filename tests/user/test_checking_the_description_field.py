from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_account_description_field(main_page):
    wait = WebDriverWait(main_page, timeout=5)

    test_description_name = "test description"


    wait.until(EC.element_to_be_clickable((By.XPATH, '//header//a[contains(@href, "user")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "account")]'))).click()
    description_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@name="_.description"]')))
    description_field.clear()
    description_field.send_keys(test_description_name)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@name="Submit"]'))).click()

    assert description_field.get_attribute('value') == test_description_name