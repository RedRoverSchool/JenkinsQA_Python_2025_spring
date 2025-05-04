from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FreestyleProjectPage(BasePage):
    class Locator:
        h1 = (By.CSS_SELECTOR, '.job-index-headline.page-headline')
        warning_message = (By.XPATH, '//form[@action="enable"]')
        form = (By.XPATH, '//form[@action="enable"]')
        build_now = (By.LINK_TEXT, 'Build Now')
        enable_button = (By.XPATH, '//button[@name="Submit"]')
        configure_menu = (By.LINK_TEXT, 'Configure')


    def __init__(self, driver, project_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{project_name}"
        self.name = project_name


    def get_warning_message(self):
        self.wait_text_to_be_present(self.Locator.h1, f"{self.name}")
        if len(self.find_elements(*self.Locator.form)) > 0:
            return self.wait_to_be_visible(self.Locator.warning_message).text
        else:
            return ''

    def click_enable_button(self):
        self.wait_for_element(self.Locator.enable_button).click()
        return self

    def go_to_configure(self):
        from pages.freestyle_project_config_page import FreestyleProjectConfigPage
        self.wait_for_element(self.Locator.build_now)
        self.wait_to_be_clickable(self.Locator.configure_menu).click()
        return FreestyleProjectConfigPage(self.driver, self.name)