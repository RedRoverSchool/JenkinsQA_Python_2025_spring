from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class UserPage(BasePage):
    class Locators:
        SECURITY_BUTTON = (By.LINK_TEXT, 'Security')

    def __init__(self, driver, username,  timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/user/{username}/"

    def go_to_security_page(self):
        from pages.security_page import SecurityPage
        self.wait_to_be_clickable(self.Locators.SECURITY_BUTTON).click()
        return SecurityPage(self.driver, self.config.jenkins.USERNAME).wait_for_url()
