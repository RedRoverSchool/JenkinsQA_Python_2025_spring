from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_set_description_for_multi_config_project(multi_config_project_page):
    wait = WebDriverWait(multi_config_project_page, 10)
    description_text = "This is my overview"
    wait.until(EC.presence_of_element_located((By.NAME, "description"))).send_keys(description_text)
    multi_config_project_page.find_element(By.NAME, "Submit").click()
    desc_element = wait.until(EC.visibility_of_element_located((By.ID, "description")))

    assert desc_element.is_displayed(), "Project description is not displayed"
    assert description_text in desc_element.text, f"Expected '{description_text}', but got '{desc_element.text}'"