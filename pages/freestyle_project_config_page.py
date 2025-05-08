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
        BUILDS_PERIODICALLY_CHECKBOX = (By.CSS_SELECTOR, "input[name='hudson-triggers-TimerTrigger']~label")
        AUTH_TOKEN = (By.NAME, "authToken")
        SCHEDULE = (By.NAME, "_.spec")
        BUILD_STEPS = (By.CSS_SELECTOR, '#build-steps')
        POST_BUILD_ACTIONS = (By.ID, 'post-build-actions')
        ENVIRONMENT = (By.ID, 'environment')
        GIT = (By.XPATH, '//label[@for="radio-block-1"]')
        GIT_ADVANCED = (By.XPATH, '//div[@class="form-container tr"]//div[@class="jenkins-form-item tr"]//button')
        TRIGGER = (By.ID, 'triggers')

    def __init__(self, driver, project_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + self.get_part_url(project_name)
        self.name = project_name

    def add_description(self, description_text):
        self.wait_for_element(self.Locator.DESCRIPTION_FIELD).send_keys(description_text)
        return self

    def click_save_button(self):
        from pages.freestyle_project_page import FreestyleProjectPage
        self.wait_to_be_clickable(self.Locator.SAVE_BUTTON).click()
        return FreestyleProjectPage(self.driver, project_name=self.name).wait_for_url()

    def click_apply_button(self):
        self.wait_to_be_clickable(self.Locator.APPLY_BUTTON).click()
        return self

    def click_git(self):
        self.wait_for_element(self.Locator.GIT).click()

    def click_git_advanced(self):
        self.wait_for_element(self.Locator.GIT_ADVANCED).click()

    def click_preview(self):
        if self.is_preview_visible():
            self.find_element(*self.Locator.PREVIEW).click()
        return self

    def click_on_checkbox_environment_options(self, item_name):
        locator = (
            By.XPATH, f'//label[text()="{item_name}"]/ancestor::span[@class="jenkins-checkbox"]')
        self.find_element(*locator).click()

    def get_part_url(self, name: str):
        if len(name.split(' ')) > 1:
            new_name = name.replace(" ", "%20")
        else:
            new_name = name
        return f"/job/{new_name}/configure"

    def get_tooltip(self, tooltip_link):
        from selenium.webdriver import ActionChains
        actions = ActionChains(self.driver)
        tooltip = self.find_element(*tooltip_link)
        actions.move_to_element(tooltip).perform()
        return self.wait_for_element(self.Locator.TOOLTIP_CONTENT).text

    def get_description(self):
        return self.find_element(*self.Locator.DESCRIPTION_FIELD).get_attribute("value")

    def get_environment_element(self):
        return self.wait_for_element(self.Locator.ENVIRONMENT)

    def get_h1_text(self):
        return self.wait_for_element(self.Locator.H1).text

    def is_checkbox_environment_options_selected(self, id_check):
        return self.wait_for_element((By.XPATH, f'//input[@id="{id_check}"]')).is_selected()

    def is_save_button_available(self):
        return self.wait_to_be_clickable(self.Locator.SAVE_BUTTON)

    def is_apply_button_available(self):
        return self.wait_to_be_clickable(self.Locator.APPLY_BUTTON)

    def is_enable(self):
        return self.wait_to_be_visible(self.Locator.ENABLE, 10)

    def is_disable(self):
        return self.wait_to_be_visible(self.Locator.DISABLE, 10)

    def is_enable_text(self):
        return self.wait_for_element(self.Locator.ENABLE_TEXT).text

    def is_preview_visible(self):
        if self.wait_to_be_clickable(self.Locator.PREVIEW):
            return True
        else:
            return False

    def is_hide_preview_visible(self):
        if self.wait_to_be_clickable(self.Locator.HIDE_PREVIEW, 2):
            return True
        else:
            return False

    def is_notification_was_visible(self):
        return self.wait_to_be_visible(self.Locator.NOTIFICATION)

    def scroll_to_post_build_actions(self):
        self.scroll_to_element(*self.Locator.POST_BUILD_ACTIONS)
        self.wait_for_element(self.Locator.BUILD_STEPS)
        return self

    def scroll_to_trigger(self):
        self.wait_text_to_be_present(self.Locator.H2_LOCATOR, 'General')
        self.scroll_to_element(*self.Locator.TRIGGER)
        self.wait_for_element(self.Locator.GIT)
        return self

    def scroll_down(self, count):
        from selenium.webdriver import ActionChains
        actions = ActionChains(self.driver)
        window_size = self.driver.get_window_size("current")
        to_half = window_size.get('height')//2
        to_dec = window_size.get('height')//10
        actions.pause(1).scroll_by_amount(0, to_half + to_dec * count).perform()

    def check_builds_trigger(self, trigger_checkbox):
        self.scroll_into_view(trigger_checkbox)
        self.wait_to_be_clickable(trigger_checkbox).click()

    def set_trigger_builds_remotely(self, token):
        self.check_builds_trigger(self.wait_for_element(self.Locator.BUILDS_REMOTELY_CHECKBOX))
        self.wait_to_be_visible(self.Locator.AUTH_TOKEN).send_keys(token)
        return self.click_save_button()

    def set_trigger_builds_periodically(self, schedule):
        self.check_builds_trigger(self.wait_for_element(self.Locator.BUILDS_PERIODICALLY_CHECKBOX))
        self.wait_to_be_visible(self.Locator.SCHEDULE).send_keys(schedule)
        return self.click_save_button()

    def switch_to_disable(self):
        self.wait_to_be_clickable(self.Locator.ENABLE, 10).click()
        return self.is_disable()
