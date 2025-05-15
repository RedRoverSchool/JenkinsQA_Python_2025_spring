from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_new_item(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/newJob')]")))
        btn.click()

    def go_to_dashboard(self):
        link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/' and text()='Dashboard']")))
        link.click()

    def verify_folder_exists(self, folder_name):
        xpath = f"//*[@id='job_{folder_name}']/td[3]/a/span"
        folder_element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        assert folder_element.text.strip() == folder_name, f"Expected to find '{folder_name}' on Dashboard, but found '{folder_element.text.strip()}'"
