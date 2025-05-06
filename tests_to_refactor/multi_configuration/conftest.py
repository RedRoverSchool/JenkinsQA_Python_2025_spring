import pytest
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.multi_config.multi_config_project_page import MultiConfigProjectConfigPage


@pytest.fixture
def multi_config_project_page(main_page):
    wait = WebDriverWait(main_page, 10)
    project_name = f"MultiConfig_{datetime.now().strftime('%H%M%S')}"

    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "New Item"))).click()
    wait.until(EC.presence_of_element_located((By.ID, "name"))).send_keys(project_name)
    wait.until(EC.presence_of_element_located((By.ID, "j-add-item-type-standalone-projects")))
    project_type = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "hudson_matrix_MatrixProject")))
    main_page.driver.execute_script("arguments[0].scrollIntoView(true);", project_type)
    time.sleep(0.5)
    project_type.click()
    wait.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()
    wait.until(EC.presence_of_element_located((By.NAME, "description")))

    return MultiConfigProjectConfigPage(main_page.driver)
