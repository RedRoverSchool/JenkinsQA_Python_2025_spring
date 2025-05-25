import allure
from selenium.webdriver.common.by import By

from pages.ui_element import UIElementMixin

class Header(UIElementMixin):
    class Locators:
        HEADER_LOGO = (By.ID, "jenkins-home-link")
        USER_PAGE_LINK = (By.CSS_SELECTOR, "a[href*='/user/']")
        LOG_OUT = (By.XPATH, '//a[@href="/logout"]')
        BREADCRUMB_BAR = (By.XPATH, "// div[ @ id = 'breadcrumbBar'] // a[ @ href = '/']")
        LOG_OUT_LINK = (By.XPATH, "// a[ @ href = '/logout']")

    @allure.step("Go to the main page by clicking logo.")
    def go_to_the_main_page(self):
        from pages.main_page import MainPage
        return self.navigate_to(MainPage, self.Locators.HEADER_LOGO)

    @allure.step("Go to the User page by clicking the Username in the header.")
    def go_to_the_user_page(self):
        from pages.user_page import UserPage
        return self.navigate_to(UserPage, self.Locators.USER_PAGE_LINK, self.config.jenkins.USERNAME)

    def sign_out(self):
        from pages.login_page import LoginPage
        self.click_on(self.Locators.LOG_OUT)
        return LoginPage(self.driver)

    def get_breadcrumb_bar_text(self):
        return self.wait_to_be_visible(self.Locators.BREADCRUMB_BAR).text

    def get_logout_link_text(self):
        return self.wait_to_be_visible(self.Locators.LOG_OUT_LINK).text

