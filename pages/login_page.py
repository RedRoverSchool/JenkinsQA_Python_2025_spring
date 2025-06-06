import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from core.jenkins_utils import update_crumb

class LoginPage(BasePage):
    class Locators:
        SIGN_IN_FORM_HEADER = (By.XPATH, "//main//h1")
        LOGIN_FIELD = (By.ID, "j_username")
        PASSWORD_FIELD = (By.ID, "j_password")
        SUBMIT_BUTTON = (By.NAME, "Submit")
        KEEP_ME_SIGNED_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = self.base_url + "/login?from=%2F"

    @allure.step("Login with credentials")
    def login(self, login, password):
        from pages.main_page import MainPage
        self.find_element(*self.Locators.LOGIN_FIELD).send_keys(login)
        self.find_element(*self.Locators.PASSWORD_FIELD).send_keys(password)
        self.find_element(*self.Locators.SUBMIT_BUTTON).click()
        main_page = MainPage(self.driver).wait_for_url()
        time.sleep(0.1)
        self.config.jenkins.current_username = login
        crumb = update_crumb(self.driver, self.config)
        self.logger.debug(f"login crumb: {crumb}")
        return main_page

    def get_sign_in_form_header(self):
        return self.find_element(*self.Locators.SIGN_IN_FORM_HEADER).text

    def is_login_field_displayed(self):
        return self.find_element(*self.Locators.LOGIN_FIELD).is_displayed()

    def is_password_field_displayed(self):
        return self.find_element(*self.Locators.PASSWORD_FIELD).is_displayed()

    def is_keep_me_signed_checkbox_displayed(self):
        return self.find_element(*self.Locators.KEEP_ME_SIGNED_CHECKBOX).is_displayed()

    def is_login_page(self):
        return self.wait_text_to_be_present(self.Locators.SIGN_IN_FORM_HEADER, "Sign in to Jenkins")
