from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FolderConfigPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def save_and_verify(self, folder_name):
        save = self.wait.until(EC.element_to_be_clickable((By.NAME, "Submit")))
        save.click()

        self.wait.until(EC.url_contains(f"/job/{folder_name}/"))
        self.wait.until(EC.presence_of_element_located((By.ID, "main-panel")))
        self.wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), folder_name))

        header_text = self.driver.find_element(By.TAG_NAME, "h1").text.strip()
        assert folder_name in header_text, f"Expected header to contain '{folder_name}', but got: '{header_text}'"
