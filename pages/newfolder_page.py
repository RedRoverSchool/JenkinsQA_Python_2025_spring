from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewItemPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def create_folder(self, folder_name):
        name_input = self.wait.until(EC.element_to_be_clickable((By.ID, "name")))
        name_input.send_keys(folder_name)

        folder_label = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='label' and normalize-space()='Folder']")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", folder_label)
        folder_label.click()

        ok = self.wait.until(EC.element_to_be_clickable((By.ID, "ok-button")))
        ok.click()
