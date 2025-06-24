import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage


class MultiConfigProjectConfigPage(BasePage):
    class Locators:
        DESCRIPTION = (By.NAME, "description")
        SUBMIT = (By.NAME, "Submit")
        SWITCH_BUTTON = (By.ID, "toggle-switch-enable-disable-project")
        SWITCH_INPUT = (By.ID, "enable-disable-project")
        SWITCH_TOOLTIP = (By.CLASS_NAME, "tippy-content")
        HELP_DISCARD_BUILDS = (By.XPATH, "//a[@tooltip='Help for feature: Discard old builds']")
        ENVIRONMENT_SECTION = (By.CSS_SELECTOR, ".jenkins-section:has(#environment)")
        DELETE_WORKSPACE_CHECKBOX = (By.CSS_SELECTOR, "input[name*='PreBuildCleanup']~label")
        USE_SECRET_TEXT = (By.CSS_SELECTOR, "input[name*='SecretBuildWrapper'] ~ label")
        ADD_TIMESTAMP_CHECKBOX = (By.CSS_SELECTOR, "input[name*='Timestamp'] ~ label")
        BUILD_SCANS_CHECKBOX = (By.CSS_SELECTOR, "input[name *= 'BuildScan'] ~ label")

    def __init__(self, driver, name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{name}/configure"
        self.name = name

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

    @allure.step("Click the switch button 'Enabled/Disabled' to change project state")
    def click_switch_button(self):
        self.click_on(self.Locators.SWITCH_BUTTON)
        return self

    def is_project_enabled(self) -> bool:
        return self.is_element_selected(self.Locators.SWITCH_INPUT)

    def is_project_disabled(self) -> bool:
        return not self.is_project_enabled()

    def submit_and_open_project_page(self):
        with allure.step(f"Click the button 'Save' to save \"{self.name}\" project and go to project page"):
            from pages.multi_config_project_page import MultiConfigProjectPage
            self.click_on(self.Locators.SUBMIT)
            return MultiConfigProjectPage(self.driver, self.name).wait_for_url()

    def get_switch_tooltip_text(self) -> str:
        self.hover_over_element(self.Locators.SWITCH_BUTTON)
        return self.get_visible_text(self.Locators.SWITCH_TOOLTIP)

    @allure.step("Hover over help for feature: 'Discard old builds'")
    def hover_over_help_discard_builds(self):
        return self.hover_over_element(self.Locators.HELP_DISCARD_BUILDS)

    @allure.step("Get environment section")
    def get_environment_section(self) -> WebElement:
        environment_section = self.wait_to_be_visible(self.Locators.ENVIRONMENT_SECTION)
        self.scroll_into_view(environment_section)
        return self.wait_to_be_visible_element(environment_section)

    @allure.step("Click 'Delete workspace' checkbox in Environment section")
    def click_delete_workspace_checkbox(self):
        environment_section = self.wait_to_be_visible(self.Locators.ENVIRONMENT_SECTION)
        self.scroll_into_view(environment_section)
        self.click_on(self.Locators.DELETE_WORKSPACE_CHECKBOX)
        return self

    @allure.step("Click 'Use secret text' checkbox in Environment section")
    def click_use_secret_text_checkbox(self):
        environment_section = self.wait_to_be_visible(self.Locators.ENVIRONMENT_SECTION)
        self.scroll_into_view(environment_section)
        self.click_on(self.Locators.USE_SECRET_TEXT)
        return self

    @allure.step("Click 'Add timestamps to the Console Output' checkbox in Environment section")
    def click_add_timestamps_to_console_output_checkbox(self):
        environment_section = self.wait_to_be_visible(self.Locators.ENVIRONMENT_SECTION)
        self.scroll_into_view(environment_section)
        self.click_on(self.Locators.ADD_TIMESTAMP_CHECKBOX)
        return self

    @allure.step("Click 'Inspect build log for published build scans' checkbox in Environment section")
    def click_build_scans_checkbox(self):
        environment_section = self.wait_to_be_visible(self.Locators.ENVIRONMENT_SECTION)
        self.scroll_into_view(environment_section)
        self.click_on(self.Locators.BUILD_SCANS_CHECKBOX)
        return self
