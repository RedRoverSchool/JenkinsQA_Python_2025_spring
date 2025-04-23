from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewItem:
    def __init__(self, main_page):
        self.main_page = main_page

    def create_freestyle_project(self):
        wait = WebDriverWait(self.main_page, 5)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/view/all/newJob']"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "name"))).send_keys("freestyle1")
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "hudson_model_FreeStyleProject"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()
        wait.until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "jenkins-home-link"))).click()
    def copy_from_option_exist(self):
        wait = WebDriverWait(self.main_page, 5)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href ='/view/all/newJob']"))).click()
        copyFromBtn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.jenkins-input.auto-complete")))
        assert copyFromBtn.is_displayed()

