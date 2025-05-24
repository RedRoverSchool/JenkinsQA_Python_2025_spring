import allure

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

    @allure.step("Generate and copy new Token with name \"{name}\"")
    def generate_token(self, name):
        with allure.step("Click Add new token button"):
            self.wait_to_be_clickable(self.Locators.ADD_NEW_TOKEN_BUTTON).click()
        with allure.step("Input token name \"{name\"}"):
            self.wait_to_be_visible(self.Locators.TOKEN_NAME).send_keys(name)
        with allure.step("Click Generate button"):
            self.wait_to_be_clickable(self.Locators.GENERATE_BUTTON).click()
        with allure.step("Copy token"):
            return self.wait_to_be_clickable(self.Locators.COPY_TOKEN_BUTTON).get_attribute("text")

    @allure.step("Save settings")
    def save_settings(self, username):
        from pages.user_page import UserPage
        with allure.step("Click Save button"):
            self.wait_to_be_clickable(self.Locators.SAVE_BUTTON).click()
        return UserPage(self.driver, username).wait_for_url()
