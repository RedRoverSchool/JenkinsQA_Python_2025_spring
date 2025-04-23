import time
from selenium.webdriver.common.by import By

class NewItem:
    def __init__(self, main_page):
        self.main_page = main_page

    def create_freestyle_project(self):
        self.main_page.find_element(By.XPATH, "//a[@href ='/view/all/newJob']").click()
        time.sleep(2)
        self.main_page.find_element(By.ID, "name").send_keys("freestyle1")
        self.main_page.find_element(By.CLASS_NAME, "hudson_model_FreeStyleProject").click()
        self.main_page.find_element(By.ID, "ok-button").click()
        time.sleep(2)
        self.main_page.find_element(By.NAME, "Submit").click()
        time.sleep(2)
        self.main_page.find_element(By.ID, "jenkins-home-link").click()

    def copy_from_option_exist(self):
        self.main_page.find_element(By.XPATH, "//a[@href ='/view/all/newJob']").click()
        time.sleep(2)
        copyFromBtn = self.main_page.find_element(By.CSS_SELECTOR, "input.jenkins-input.auto-complete")
        assert copyFromBtn.is_displayed()

