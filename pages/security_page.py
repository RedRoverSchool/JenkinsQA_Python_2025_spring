from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SecurityPage(BasePage):
    class Locators:
        ADD_NEW_TOKEN_BUTTON = (By.CSS_SELECTOR, "button.repeatable-add")
        TOKEN_NAME = (By.CSS_SELECTOR, "input[placeholder='Default name']")
        GENERATE_BUTTON = (By.ID, "api-token-property-token-save")
        COPY_TOKEN_BUTTON = (By.CSS_SELECTOR, "button[title='Copy this token'")
        SAVE_BUTTON = (By.NAME, "Submit")

    def __init__(self, driver, username,  timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/user/{username}/security/"

    def generate_token(self, name):
        self.wait_to_be_clickable(self.Locators.ADD_NEW_TOKEN_BUTTON).click()
        self.wait_to_be_visible(self.Locators.TOKEN_NAME).send_keys(name)
        self.wait_to_be_clickable(self.Locators.GENERATE_BUTTON).click()
        return self.wait_to_be_clickable(self.Locators.COPY_TOKEN_BUTTON).get_attribute("text")

    def save_settings(self, username):
        from pages.user_page import UserPage
        self.wait_to_be_clickable(self.Locators.SAVE_BUTTON).click()
        return UserPage(self.driver, username).wait_for_url()
