from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_edit_description_from_project_page(multi_config_project_with_description_page):
    wait = WebDriverWait(multi_config_project_with_description_page, 10)
    updated_text = "Updated project summary"

    wait.until(EC.element_to_be_clickable((By.ID,"description-link"))).click()
    desc_input = wait.until(EC.visibility_of_element_located((By.NAME, "description")))
    desc_input.clear()
    desc_input.send_keys(updated_text)
    multi_config_project_with_description_page.find_element(By.NAME, "Submit").click()
    text_actual = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#description>div:first-child"))).text

    assert text_actual == updated_text
