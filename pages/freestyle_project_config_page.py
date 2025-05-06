from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FreestyleProjectConfigPage(BasePage):
    class Locator:
        H1 = (By.CSS_SELECTOR, '.jenkins-app-bar__content>h1')
        H2_LOCATOR = (By.ID, "general")
        ENABLE = (By.CLASS_NAME, 'jenkins-toggle-switch__label__checked-title')
        DISABLE = (By.CLASS_NAME, 'jenkins-toggle-switch__label__unchecked-title')
        ENABLE_TEXT = (By.XPATH, '//label[@class="jenkins-toggle-switch__label "]')
        TOOLTIP_CONTENT = (By.XPATH, '//div[@class="tippy-content"]')
        DESCRIPTION_FIELD = (By.XPATH, '//textarea[@name="description"]')
        SAVE_BUTTON = (By.XPATH, '//button[@name="Submit"]')
        APPLY_BUTTON = (By.XPATH, '//button[@name="Apply"]')
        PREVIEW = (By.LINK_TEXT, 'Preview')
        HIDE_PREVIEW = (By.LINK_TEXT, 'Hide preview')
        NOTIFICATION = (By.ID, 'notification-bar')
        BUILDS_REMOTELY_CHECKBOX = (By.CSS_SELECTOR, "input[name='pseudoRemoteTrigger']~label")
        AUTH_TOKEN = (By.NAME, "authToken")

    def __init__(self, driver, project_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + self.get_part_url(project_name)
        self.name = project_name

    def get_part_url(self, name: str):
        if len(name.split(' ')) > 1:
            new_name = name.replace(" ", "%20")
        else:
            new_name = name
        return f"/job/{new_name}/configure"

    def get_h1_text(self):
        return self.wait_for_element(self.Locator.H1).text

    def is_enable(self):
        return self.wait_to_be_visible(self.Locator.ENABLE, 10)

    def is_disable(self):
        return self.wait_to_be_visible(self.Locator.DISABLE, 10)

    def switch_to_disable(self):
        self.wait_to_be_clickable(self.Locator.ENABLE, 10).click()
        return self.is_disable()

    def is_save_button_available(self):
        return self.wait_to_be_clickable(self.Locator.SAVE_BUTTON)

    def click_save_button(self):
        from pages.freestyle_project_page import FreestyleProjectPage
        self.wait_to_be_clickable(self.Locator.SAVE_BUTTON).click()
        return FreestyleProjectPage(self.driver, project_name=self.name).wait_for_url()

    def is_apply_button_available(self):
        return self.wait_to_be_clickable(self.Locator.APPLY_BUTTON)

    def click_apply_button(self):
        self.wait_to_be_clickable(self.Locator.APPLY_BUTTON).click()
        return self

    def is_enable_text(self):
        return self.wait_for_element(self.Locator.ENABLE_TEXT).text

    def get_tooltip(self, tooltip_link, tooltip_wait):
        from selenium.webdriver import ActionChains
        actions = ActionChains(self.driver)
        tooltip = self.find_element(*tooltip_link)
        actions.move_to_element(tooltip).perform()
        self.wait_for_element(tooltip_wait)
        return self.wait_for_element(self.Locator.TOOLTIP_CONTENT).text

    def add_description(self, description_text):
        self.wait_for_element(self.Locator.DESCRIPTION_FIELD).send_keys(description_text)
        return self

    def get_description(self):
        return self.find_element(*self.Locator.DESCRIPTION_FIELD).get_attribute("value")

    def is_preview_visible(self):
        if self.wait_to_be_clickable(self.Locator.PREVIEW):
            return True
        else:
            return False

    def click_preview(self):
        if self.is_preview_visible():
            self.find_element(*self.Locator.PREVIEW).click()
        return self

    def is_hide_preview_visible(self):
        if self.wait_to_be_clickable(self.Locator.HIDE_PREVIEW, 2):
            return True
        else:
            return False

    def is_notification_was_visible(self):
        return self.wait_to_be_visible(self.Locator.NOTIFICATION)

    def set_trigger_builds_remotely(self, token):
        checkbox = self.wait_for_element(self.Locator.BUILDS_REMOTELY_CHECKBOX)
        self.scroll_into_view(checkbox)
        self.wait_to_be_clickable(checkbox).click()
        self.wait_to_be_visible(self.Locator.AUTH_TOKEN).send_keys(token)
        return self.click_save_button()
