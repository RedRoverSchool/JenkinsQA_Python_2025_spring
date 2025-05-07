from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from core.jenkins_utils import update_crumb

class LoginPage(BasePage):
    class Locator:
        SIGN_IN_FORM_HEADER = (By.XPATH, "//main//h1")
        LOGIN_FIELD = (By.ID, "j_username")
        PASSWORD_FIELD = (By.ID, "j_password")
        SUBMIT_BUTTON = (By.NAME, "Submit")
        KEEP_ME_SIGNED_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = self.base_url + "/login?from=%2F"


    def login(self, login, password):
        from pages.main_page import MainPage
        self.find_element(*self.Locator.LOGIN_FIELD).send_keys(login)
        self.find_element(*self.Locator.PASSWORD_FIELD).send_keys(password)
        self.find_element(*self.Locator.SUBMIT_BUTTON).click()
        main_page = MainPage(self.driver).wait_for_url()
        crumb = update_crumb(self.driver, self.config)
        self.logger.info(f"login crumb: {crumb}")
        return main_page

    def get_sign_in_form_header(self):
        return self.find_element(*self.Locator.SIGN_IN_FORM_HEADER).text

    def login_field_is_displayed(self):
        return self.find_element(*self.Locator.LOGIN_FIELD).is_displayed()

    def password_field_is_displayed(self):
        return self.find_element(*self.Locator.PASSWORD_FIELD).is_displayed()

    def keep_me_signed_checkbox_is_displayed(self):
        return self.find_element(*self.Locator.KEEP_ME_SIGNED_CHECKBOX).is_displayed()
