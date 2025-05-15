from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FreestyleProjectConfigPage(BasePage):
    class Locators:
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
        ADD_POST_BUILD_ACTIONS = (By.XPATH, '//button[@class="jenkins-button hetero-list-add" and @suffix="publisher"]')
        LIST_POST_BUILD_ACTIONS = (By.CLASS_NAME, 'jenkins-dropdown__item ')
        GITHUB_PROJECT_OPTION = (By.CSS_SELECTOR, 'input[name="githubProject"]')
        PROJECT_URL_FIELD = (By.XPATH, '//*[contains(text(),"Project url")]//following-sibling::div/input')

    def __init__(self, driver, project_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + self.get_part_url(project_name)
        self.name = project_name

    def add_description(self, description_text):
        self.wait_for_element(self.Locators.DESCRIPTION_FIELD).send_keys(description_text)
        return self

    def click_save_button(self):
        from pages.freestyle_project_page import FreestyleProjectPage
        self.wait_to_be_clickable(self.Locators.SAVE_BUTTON).click()
        return FreestyleProjectPage(self.driver, project_name=self.name).wait_for_url()

    def click_apply_button(self):
        self.wait_to_be_clickable(self.Locators.APPLY_BUTTON).click()
        return self

    def click_git(self):
        self.wait_for_element(self.Locators.GIT).click()

    def click_git_advanced(self):
        self.wait_for_element(self.Locators.GIT_ADVANCED).click()

    def click_preview(self):
        if self.is_preview_visible():
            self.find_element(*self.Locators.PREVIEW).click()
        return self

    def click_on_checkbox_environment_options(self, item_name):
        locator = (
            By.XPATH, f'//label[text()="{item_name}"]/ancestor::span[@class="jenkins-checkbox"]')
        self.find_element(*locator).click()

    def click_add_post_build_actions(self):
        from selenium.webdriver import ActionChains
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(*self.Locators.ADD_POST_BUILD_ACTIONS)).click().perform()
        return self

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
        return self.wait_for_element(self.Locators.TOOLTIP_CONTENT).text

    def get_description(self):
        return self.find_element(*self.Locators.DESCRIPTION_FIELD).get_attribute("value")

    def get_environment_element(self):
        return self.wait_for_element(self.Locators.ENVIRONMENT)

    def get_h1_text(self):
        return self.wait_for_element(self.Locators.H1).text

    def get_items_post_build_actions(self):
        list_post_build_actions = self.wait_to_be_visible_all(self.Locators.LIST_POST_BUILD_ACTIONS)
        items_post_build_action = []
        for item in list_post_build_actions:
            items_post_build_action.append(item.text)
        return items_post_build_action

    def get_port_build_actions_element(self):
        return self.wait_for_element(self.Locators.POST_BUILD_ACTIONS)

    def get_windows_size(self, handle):
        return self.driver.get_window_size(handle)

    def is_checkbox_environment_options_selected(self, id_check):
        return self.wait_for_element((By.XPATH, f'//input[@id="{id_check}"]')).is_selected()

    def is_save_button_available(self):
        return self.wait_to_be_clickable(self.Locators.SAVE_BUTTON)

    def is_apply_button_available(self):
        return self.wait_to_be_clickable(self.Locators.APPLY_BUTTON)

    def is_enable(self):
        return self.wait_to_be_visible(self.Locators.ENABLE, 10)

    def is_disable(self):
        return self.wait_to_be_visible(self.Locators.DISABLE, 10)

    def is_enable_text(self):
        return self.wait_for_element(self.Locators.ENABLE_TEXT).text

    def is_preview_visible(self):
        if self.wait_to_be_clickable(self.Locators.PREVIEW):
            return True
        else:
            return False

    def is_hide_preview_visible(self):
        if self.wait_to_be_clickable(self.Locators.HIDE_PREVIEW, 2):
            return True
        else:
            return False

    def is_notification_was_visible(self):
        return self.wait_to_be_visible(self.Locators.NOTIFICATION)

    def scroll_to_post_build_actions(self):
        self.scroll_to_element(*self.Locators.POST_BUILD_ACTIONS)
        self.wait_for_element(self.Locators.BUILD_STEPS)
        return self

    def scroll_to_trigger(self):
        self.wait_text_to_be_present(self.Locators.H2_LOCATOR, 'General')
        self.scroll_to_element(*self.Locators.TRIGGER)
        self.wait_for_element(self.Locators.GIT)
        return self

    def scroll_down(self, count):
        from selenium.webdriver import ActionChains
        actions = ActionChains(self.driver)
        window_size = self.get_windows_size("current")
        to_half = window_size.get('height') // 2
        to_dec = window_size.get('height') // 10
        actions.pause(1).scroll_by_amount(0, to_half + to_dec * count).perform()

    def scroll_to_bottom_screen(self):
        from selenium.webdriver import ActionChains
        actions = ActionChains(self.driver)
        window_size = self.get_windows_size("current")
        actions.pause(1).scroll_by_amount(0, window_size.get('height')).perform()
        self.wait_to_be_clickable(self.Locators.ADD_POST_BUILD_ACTIONS)
        return self

    def set_trigger_builds_remotely(self, token):
        checkbox = self.wait_for_element(self.Locators.BUILDS_REMOTELY_CHECKBOX)
        self.scroll_into_view(checkbox)
        self.wait_to_be_clickable(checkbox).click()
        self.wait_to_be_visible(self.Locators.AUTH_TOKEN).send_keys(token)
        return self.click_save_button()

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
        self.wait_to_be_clickable(self.Locators.ENABLE, 10).click()
        return self.is_disable()

    def check_github_project_option(self):
        checkbox = self.wait_to_be_visible(self.Locators.GITHUB_PROJECT_OPTION)
        self.driver.execute_script("arguments[0].click();", checkbox)

    def is_github_project_option_enabled(self):
        checkbox = self.wait_to_be_visible(self.Locators.GITHUB_PROJECT_OPTION)
        return self.driver.execute_script("return arguments[0].checked;", checkbox)

    def add_project_url(self, github_project_url):
        self.wait_to_be_visible(self.Locators.PROJECT_URL_FIELD).send_keys(github_project_url)
        return self
