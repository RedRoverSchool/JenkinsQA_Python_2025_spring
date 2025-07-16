import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from tests.multibranch_pipeline_configuration.mbp_data import Toggle
class MultibranchPipelineConfigPage(BasePage):

    class Projects_name:
        MBP_TITLE = "Multibranch_Pipeline_Project"
        LIBRARY_NAME = 'Test_1'
    class Locators:
        PROPERTIES_SECTION = (By.ID, "properties")
        BRANCH_SOURCES_SECTION = (By.ID, "branch-sources")
        ADD_SOURCE_BUTTON = (By.XPATH, '//*[@id="main-panel"]/form/div[1]/section[1]/div[2]/div/div/div[2]/button')
        ADD_SOURCE_ITEM =  (By.CLASS_NAME, 'jenkins-dropdown__item ')
        BUTTON_ADD = (By.CSS_SELECTOR, ".jenkins-button.repeatable-add")
        TITLE_ADDED_PROPERTY = (By.CLASS_NAME, "repeated-chunk__header")
        INPUT_ADDED_PROPERTY = (By.NAME, "_.name")
        BUTTON_SAVE = (By.NAME, "Submit")
        CONFIGURE_OPTION = (By.CSS_SELECTOR, "a.task-link[href$='/configure']")

    def __init__(self, driver, job_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{job_name}/configure"

    def get_state_of_the_toggle(self):
        return self.find_element(*Toggle.TOGGLE).text

    @allure.step("Get Properties section element")
    def get_properties_section(self):
        properties_section = self.wait_to_be_visible(self.Locators.PROPERTIES_SECTION)
        self.scroll_into_view(properties_section)
        return properties_section

    @allure.step("Get Branch Sources section element")
    def get_branch_sources_section(self):
        branch_sources_section = self.wait_to_be_visible(self.Locators.BRANCH_SOURCES_SECTION)
        self.scroll_into_view(branch_sources_section)
        return branch_sources_section

    @allure.step("Scroll to Branch Sources section")
    def scroll_to_branch_sources_section(self):
        branch_sources_section = self.wait_to_be_visible(self.Locators.BRANCH_SOURCES_SECTION)
        self.scroll_into_view(branch_sources_section)
        return self

    @allure.step('Click on "Add source" button')
    def click_add_source_button(self):
        from selenium.webdriver import ActionChains
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(*self.Locators.ADD_SOURCE_BUTTON)).click().perform()
        return self

    def get_add_source_items(self) -> list:
        list_add_source_items = self.wait_to_be_visible_all(self.Locators.ADD_SOURCE_ITEM)
        add_source_items = []
        for item in list_add_source_items:
            add_source_items.append(item.text)
        return add_source_items
    
    @allure.step("In the Properties section, click “Add Property”")
    def add_properties(self):
        self.wait_to_be_clickable(self.Locators.BUTTON_ADD).click()
        new_property = self.wait_to_be_visible(self.Locators.TITLE_ADDED_PROPERTY).text
        return new_property
    
    @allure.step("Enter the name of property")
    def enter_item_name(self):
        self.enter_text(self.Locators.INPUT_ADDED_PROPERTY, self.Projects_name.LIBRARY_NAME)
        return self.Projects_name.LIBRARY_NAME
    
    @allure.step("Click the “Save” button at the bottom of the page")
    def click_save_property(self):
        self.wait_to_be_clickable(self.Locators.BUTTON_SAVE).click()
        return self
    
    @allure.step("Redirect to the project\n's main page")
    def main_page_availability(self):
        return self.find_element(By.XPATH, f"//h1[contains(normalize-space(.), '{self.Projects_name.MBP_TITLE}')]")
        
    @allure.step("Re-enter the Configure page")
    def click_on_configure(self):
        return self.wait_to_be_clickable(self.Locators.CONFIGURE_OPTION).click()
    
    @allure.step("Verify that the added and edited property values are correctly saved and displayed")
    def find_added_property(self):
        values = []
        target = self.Projects_name.LIBRARY_NAME
        inputs = self.find_elements(By.CSS_SELECTOR, "input.jenkins-input.validated")
        # inputs = self.find_elements(self.Locators.INPUT_ADDED_PROPERTY)
        for inp in inputs:
            values.append(inp.get_attribute("value"))
        if target in values:
            return target
