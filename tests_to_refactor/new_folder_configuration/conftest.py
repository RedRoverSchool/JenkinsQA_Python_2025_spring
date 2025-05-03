import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def create_folder(main_page):
    def create_folder_inner(item_name):
        wait = WebDriverWait(main_page, 10)
        # Create a folder
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='newJob']"))).click()
        main_page.find_element(By.CLASS_NAME, "jenkins-input").send_keys(item_name)
        main_page.find_element(By.CLASS_NAME, "com_cloudbees_hudson_plugins_folder_Folder").click()
        main_page.find_element(By.ID, "ok-button").click()
    return create_folder_inner

