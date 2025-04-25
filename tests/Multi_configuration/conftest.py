import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def multi_config_project_page(main_page):
    wait = WebDriverWait(main_page, 10)
    project_name = "MultiConfigProject01"

    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "New Item"))).click()
    wait.until(EC.presence_of_element_located((By.ID, "name"))).send_keys(project_name)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="j-add-item-type-standalone-projects"]/ul/li[3]/div[2]/div'))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()
    wait.until(EC.presence_of_element_located((By.NAME, "description")))
    return main_page
