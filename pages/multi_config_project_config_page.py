import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MultiConfigProjectConfigPage(BasePage):
    class Locators:
        DESCRIPTION = (By.NAME, "description")
        SUBMIT = (By.NAME, "Submit")
        SWITCH_BUTTON = (By.ID, "toggle-switch-enable-disable-project")
        SWITCH_INPUT = (By.ID, "enable-disable-project")
        SWITCH_TOOLTIP = (By.CLASS_NAME, "tippy-content")

    def __init__(self, driver, name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{name}/configure"

    def set_description(self, text, name):
        from pages.multi_config_project_page import MultiConfigProjectPage
        self.wait_to_be_visible(self.Locators.DESCRIPTION).send_keys(text)
        self.wait_to_be_clickable(self.Locators.SUBMIT).click()
        return MultiConfigProjectPage(self.driver, name).wait_for_url()

    def edit_description(self, new_text, name):
        from pages.multi_config_project_page import MultiConfigProjectPage
        input_field = self.wait_to_be_visible(self.Locators.DESCRIPTION)
        input_field.clear()
        input_field.send_keys(new_text)
        self.wait_to_be_clickable(self.Locators.SUBMIT).click()
        return MultiConfigProjectPage(self.driver, name).wait_for_url()

    def click_switch_button(self):
        self.click_on(self.Locators.SWITCH_BUTTON)
        return self

    def click_submit_button(self):
        return self.click_on(self.Locators.SUBMIT)

    def is_project_enabled(self) -> bool:
        return self.is_element_selected(self.Locators.SWITCH_INPUT)

    def is_project_disabled(self) -> bool:
        return not self.is_project_enabled()

    @allure.step("Save \"{name}\" project and go to project page")
    def submit_and_open_project_page(self, name):
        from pages.multi_config_project_page import MultiConfigProjectPage
        self.click_submit_button()
        return MultiConfigProjectPage(self.driver, name).wait_for_url()

    @allure.step("Get tooltip text from switch button")
    def get_switch_tooltip_text(self) -> str:
        self.hover_over_element(self.Locators.SWITCH_BUTTON)
        return self.get_visible_text(self.Locators.SWITCH_TOOLTIP)

    def hover_over_description(self):
        return self.hover_over_element(self.Locators.DESCRIPTION)
