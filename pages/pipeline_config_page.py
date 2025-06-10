import allure
from urllib.parse import quote
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PipelineConfigPage(BasePage):
    class Locators:
        GENERAL_BUTTON = (By.ID, "general")
        DESCRIPTION_FIELD = (By.NAME, 'description')
        SAVE_BUTTON = (By.NAME, "Submit")
        TRIGGERS_TITLE = (By.ID, "triggers")
        TRIGGERS_DESCRIPTION = (By.CSS_SELECTOR, "#triggers + .jenkins-section__description")
        TRIGGERS_SIDEBAR = (By.CSS_SELECTOR, "button[data-section-id='triggers']")
        TRIGGER_LABELS = (By.XPATH, "//span[input[contains(@name, 'Trigger')]]")
        TRIGGER_CHECKBOXES = (By.XPATH, "//*[contains(@name, 'Trigger') and @type='checkbox']")
        TRIGGER_HELPER_ICONS = (By.CSS_SELECTOR, "div[class*='checkbox'] a[helpurl*='rigger'] > span")
        TRIGGER_HELPER_TOOLTIPS = (By.CLASS_NAME, "tippy-box")

    def __init__(self, driver, pipeline_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.pipeline_name = pipeline_name
        self.url = self.base_url + f"/job/{quote(pipeline_name)}/configure"

    def click_save_button_and_open_project_page(self):
        with allure.step(f"Click the button 'Save' to save \"{self.pipeline_name}\" project and go to project page"):
            from pages.pipeline_page import PipelinePage
            self.click_on(self.Locators.SAVE_BUTTON)
            return PipelinePage(self.driver, self.pipeline_name).wait_for_url()

    def wait_for_page(self):
        return self.wait_for_element(self.Locators.GENERAL_BUTTON)

    def add_description(self, text_for_description):
        self.wait_for_element(self.Locators.DESCRIPTION_FIELD).send_keys(text_for_description)
        return self

    def click_save_button(self, pipeline_project_name):
        from pages.pipeline_page import PipelinePage
        self.wait_to_be_clickable(self.Locators.SAVE_BUTTON).click()
        return PipelinePage(self.driver, pipeline_project_name).wait_for_url()

    @allure.step("Scroll to the \"Build Triggers\" section title")
    def scroll_to_triggers_section(self) -> None:
        element = self.wait_to_be_visible(self.Locators.TRIGGERS_TITLE)
        self.scroll_into_view(element)

    @allure.step("Get the title text for the \"Build Triggers\" section")
    def get_text_title_triggers(self) -> str:
        self.scroll_to_triggers_section()
        return self.get_visible_text(self.Locators.TRIGGERS_TITLE)

    @allure.step("Get the description text for the \"Build Triggers\" section")
    def get_text_description_triggers(self) -> str:
        self.scroll_to_triggers_section()
        return self.get_visible_text(self.Locators.TRIGGERS_DESCRIPTION)

    @allure.step("Get the sidebar label text for the \"Build Triggers\" section")
    def get_text_sidebar_triggers(self) -> str:
        return self.get_visible_text(self.Locators.TRIGGERS_SIDEBAR)

    @allure.step("Get text from all trigger checkbox labels")
    def get_text_trigger_labels(self) -> list[str]:
        self.scroll_to_triggers_section()
        labels = self.wait_to_be_visible_all(self.Locators.TRIGGER_LABELS)
        return [label.text.strip() for label in labels]

    @allure.step("Get visible of all trigger checkboxes ids")
    def get_visible_trigger_checkboxes_ids(self) -> list[str]:
        self.scroll_to_triggers_section()
        checkboxes = self.wait_to_be_visible_all(self.Locators.TRIGGER_CHECKBOXES)
        return [cb.get_attribute("id") for cb in checkboxes]

    @allure.step("Get trigger checkboxes checked states")
    def is_trigger_checkboxes_checked(self) -> list[bool]:
        return self.is_elements_selected(self.Locators.TRIGGER_CHECKBOXES)

    @allure.step("Get trigger checkboxes unchecked states")
    def is_trigger_checkboxes_unchecked(self) -> list[bool]:
        return self.is_elements_unselected(self.Locators.TRIGGER_CHECKBOXES)

    @allure.step("Clik all trigger checkbox labels")
    def click_trigger_labels(self):
        self.click_elements(self.Locators.TRIGGER_LABELS)
        return self

    @allure.step("Get display status of helper icons for trigger checkboxes")
    def is_helper_icons_displayed(self) -> list[bool]:
        return self.is_elements_displayed(self.Locators.TRIGGER_HELPER_ICONS)

    @allure.step("Get visible tooltip text for helper icons for trigger checkboxes")
    def get_trigger_helper_tooltips(self) -> list[str]:
        return self.get_tooltip_texts(self.Locators.TRIGGER_HELPER_ICONS, self.Locators.TRIGGER_HELPER_TOOLTIPS)

    @allure.step("Wait for all tooltips to disappear after hover out")
    def trigger_tooltips_disappeared(self) -> list[bool]:
        return self.wait_all_tooltips_to_disappear(self.Locators.TRIGGER_HELPER_ICONS,
                                                   self.Locators.TRIGGER_HELPER_TOOLTIPS, self.Locators.TRIGGER_LABELS)
