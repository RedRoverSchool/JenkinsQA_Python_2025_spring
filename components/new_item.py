from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewItem:
    def __init__(self, main_page):
        self.main_page = main_page
        self.wait = WebDriverWait(self.main_page, 100)

    def click_element(self, by, value):
       return self.wait.until(EC.element_to_be_clickable((by, value))).click()

    def enter_text(self, by, value, text):
        return self.wait.until(EC.element_to_be_clickable((by, value))).send_keys(text)

    def wait_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def create_freestyle_project(self):
        self.click_element(By.XPATH, "//a[@href='/view/all/newJob']")
        self.enter_text(By.ID, "name", "freestyle1")
        self.click_element(By.CLASS_NAME, "hudson_model_FreeStyleProject")
        self.click_element(By.ID, "ok-button")
        self.click_element(By.NAME, "Submit")
        self.click_element(By.ID, "jenkins-home-link")

    def copy_from_option_exist(self):
        self.click_element(By.XPATH, "//a[@href='/view/all/newJob']")
        self.wait_element(By.CSS_SELECTOR, "input.jenkins-input.auto-complete")
        copy = self.main_page.find_element(By.CSS_SELECTOR, "input.jenkins-input.auto-complete")
        assert copy.is_displayed(), "Autocomplete input field is not visible!"

    def copy_from_option_is_working(self):
        self.click_element(By.XPATH, "//a[@href='/view/all/newJob']")
        self.enter_text(By.CSS_SELECTOR, "input.jenkins-input.auto-complete", "f")
        assert self.wait.until(
            EC.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, "input.jenkins-input.auto-complete"), "aria-expanded", "true"))
