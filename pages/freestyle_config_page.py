from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FreestyleConfigPage(BasePage):
    class Locator:
        BUILDS_REMOTELY_CHECKBOX = (By.CSS_SELECTOR, "input[name='pseudoRemoteTrigger']~label")
        AUTH_TOKEN = (By.NAME, "authToken")
        SAVE_BUTTON = (By.NAME, "Submit")


    def __init__(self, driver, project_name,  timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{project_name}/configure"

    def set_trigger_builds_remotely(self, token, name):
        from pages.freestyle_project_page import FreestyleProjectPage
        self.wait_for_url()
        checkbox = self.wait_for_element(self.Locator.BUILDS_REMOTELY_CHECKBOX)
        self.scroll_into_view(checkbox)
        self.wait_to_be_clickable(checkbox).click()
        self.wait_to_be_visible(self.Locator.AUTH_TOKEN).send_keys(token)
        self.wait_to_be_clickable(self.Locator.SAVE_BUTTON).click()
        return FreestyleProjectPage(self.driver, name)
