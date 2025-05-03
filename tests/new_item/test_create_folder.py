import os
import time
from dotenv import load_dotenv
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path)

def click_new_item_button(driver):
    try:
        btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/newJob')]"))
        )
        btn.click()
    except (NoSuchElementException, TimeoutException):
        raise AssertionError("The 'New Item' button was not found.")

@pytest.mark.usefixtures("driver")
class TestCreateFolder:

    def test_create_folder_from_dashboard(self, login_page, main_page, driver):

        assert login_page.title == "Sign in [Jenkins]" or main_page.title == "Dashboard [Jenkins]"

        click_new_item_button(driver)
        wait = WebDriverWait(driver, 10)

        folder_name = f"TestFolder_{int(time.time())}"
        name_input = wait.until(EC.presence_of_element_located((By.ID, "name")))
        name_input.send_keys(folder_name)

        folder_label = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//span[@class='label' and normalize-space()='Folder']"
        )))
        driver.execute_script("arguments[0].scrollIntoView(true);", folder_label)
        folder_label.click()

        ok = wait.until(EC.element_to_be_clickable((By.ID, "ok-button")))
        ok.click()

        save = wait.until(EC.element_to_be_clickable((By.NAME, "Submit")))
        save.click()

        wait.until(EC.url_contains(f"/job/{folder_name}/"))
        wait.until(EC.presence_of_element_located((By.ID, "main-panel")))

        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), folder_name))
        header_text = driver.find_element(By.TAG_NAME, "h1").text.strip()
        assert folder_name in header_text, f"Expected header to contain '{folder_name}', but got: '{header_text}'"

        dashboard_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/' and text()='Dashboard']")))
        dashboard_link.click()

        folder_xpath = f"//*[@id='job_{folder_name}']/td[3]/a/span"
        folder_element = wait.until(EC.presence_of_element_located((By.XPATH, folder_xpath)))

        assert folder_element.text.strip() == folder_name, f"Expected to find '{folder_name}' on Dashboard, but found '{folder_element.text.strip()}'"