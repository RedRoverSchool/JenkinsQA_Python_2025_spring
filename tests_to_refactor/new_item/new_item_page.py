from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class NewItemPage:
    NEW_ITEM_LINK = (By.XPATH, "//a[@href='/view/all/newJob']")
    ITEM_LIST = (By.ID, "items")
    TITLE_ITEMS = (By.XPATH, "//label/span")
    PIPELINE_ITEM = (By.CLASS_NAME, "org_jenkinsci_plugins_workflow_job_WorkflowJob")
    PIPELINE_ITEM_ACTIVE = (By.CSS_SELECTOR, ".org_jenkinsci_plugins_workflow_job_WorkflowJob.active")
    FREESTYLE_ITEM = (By.CLASS_NAME, "hudson_model_FreeStyleProject")
    FREESTYLE_ITEM_ACTIVE = (By.CSS_SELECTOR, ".hudson_model_FreeStyleProject.active")
    SELECTED_ITEM = (By.XPATH, "//li[@aria-checked='true']")
    ACTIVE_ITEM = (By.CLASS_NAME, "active")
    ACTIVE_ITEM_TITLE = (By.XPATH, "//li[contains(@class, 'active')]//label/span")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.driver.find_element(*self.NEW_ITEM_LINK).click()
        self.wait.until(EC.visibility_of_element_located(self.ITEM_LIST))

    def select_pipeline_project(self):
        self.driver.find_element(*self.PIPELINE_ITEM).click()
        self.wait.until(EC.visibility_of_element_located(self.PIPELINE_ITEM_ACTIVE))

    def select_freestyle_project(self):
        self.driver.find_element(*self.FREESTYLE_ITEM).click()
        self.wait.until(EC.visibility_of_element_located(self.FREESTYLE_ITEM_ACTIVE))

    def get_title_items(self):
        return self.driver.find_elements(*self.TITLE_ITEMS)

    def get_selected_items(self):
        return self.driver.find_elements(*self.SELECTED_ITEM)

    def get_highlighted_items(self):
        return self.driver.find_elements(*self.ACTIVE_ITEM)

    def get_highlighted_item_title(self):
        return self.driver.find_element(*self.ACTIVE_ITEM_TITLE).text.strip()
