from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webelement import WebElement
from pages.manage_jenkins.manage_jenkins_page import ManageJenkinsPage
from tests.manage_jenkins.status_information.data import SystemInformationData as SI


class SystemInformationPage(ManageJenkinsPage):
    class Locator:
        TABS_BAR = (By.CSS_SELECTOR, ".tabBar .tab a")
        ACTIVE_TAB = (By.XPATH, "//div[@class='jenkins-tab-pane'][@style='display: block;']/h2")
        TABLE_ROWS = (By.TAG_NAME, "tr")
        TABLE_CELLS = (By.TAG_NAME, "td")
        TIMESPAN_DROPDOWN = (By.ID, "timespan-select")

        @staticmethod
        def tab_table(tab_number: int) -> tuple[str, str]:
            return By.XPATH, f"//div[@class='jenkins-tab-pane'][{tab_number}]/table/tbody"

        @staticmethod
        def show_all_button(tab_number: int) -> tuple[str, str]:
            return By.XPATH, f"(//button[contains(normalize-space(text()), 'Show values')])[{tab_number}]"

        @staticmethod
        def hide_all_button(tab_number: int) -> tuple[str, str]:
            return By.XPATH, f"(//button[contains(normalize-space(text()), 'Hide values')])[{tab_number}]"

        @staticmethod
        def show_single_value_button(element_name: str) -> tuple[str, str]:
            return By.XPATH, f"//tr[td[normalize-space(text())='{element_name}']]//button[contains(normalize-space(.), '{SI.SHOW_SINGLE_VALUE_BUTTON_TEXT}')]"

        @staticmethod
        def hide_single_value_button(element_name: str) -> tuple[str, str]:
            return By.XPATH, f"//tr[td[normalize-space(text())='{element_name}']]//div[contains(@class, 'app-hidden-info-hide')]//button"

        @staticmethod
        def tab_by_name(tab_name: str) -> tuple[str, str]:
            return By.XPATH, f"//a[@href='#'][text()='{tab_name}']/.."

        @staticmethod
        def memory_usage_graph(flag_value: str) -> tuple[str, str]:
            return By.XPATH, f"//img[@alt='Memory usage graph' and contains(@src, '{flag_value}')]"

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/manage/systemInfo"

    def get_tabs_bar_headers(self) -> list[str]:
        self.wait_to_be_clickable(self.Locator.TABS_BAR)
        return [tab.text.strip() for tab in self.find_elements(*self.Locator.TABS_BAR)]

    def get_active_tab_number(self) -> int:
        tab = self.find_element(*self.Locator.ACTIVE_TAB)
        tab_name = tab.get_attribute("textContent")
        return SI.TABS_BAR_HEADERS.index(tab_name) + 1

    def get_table_content(self) -> list[list[str]]:
        tab_number = self.get_active_tab_number()
        table = self.find_element(*self.Locator.tab_table(tab_number))
        raw_rows = table.find_elements(*self.Locator.TABLE_ROWS)
        processed_rows = []
        for row in raw_rows:
            cells = row.find_elements(*self.Locator.TABLE_CELLS)
            row_text = [cell.text for cell in cells]
            processed_rows.append(row_text)
        return processed_rows

    def click_show_all_values_button(self) -> None:
        tab_number = self.get_active_tab_number()
        self.click_on(self.Locator.show_all_button(tab_number))

    def click_hide_all_values_button(self) -> None:
        tab_number = self.get_active_tab_number()
        self.click_on(self.Locator.hide_all_button(tab_number))

    def click_show_single_value_button(self, system_property: str) -> str:
        locator = self.Locator.show_single_value_button(system_property)
        self.click_on(locator)
        locator = self.Locator.hide_single_value_button(system_property)
        return self.find_element(*locator).get_attribute("textContent").strip().replace('\n', '').replace('\r', '')

    def click_hide_single_value_button(self, system_property: str) -> str:
        locator = self.Locator.hide_single_value_button(system_property)
        self.click_on(locator)
        locator = self.Locator.show_single_value_button(system_property)
        return self.find_element(*locator).get_attribute("textContent").strip().replace('\n', '').replace('\r', '')

    def click_on_tab(self, tab_name: str) -> None:
        self.click_on(self.Locator.tab_by_name(tab_name))

    def click_on_environment_variables_tab(self) -> None:
        self.click_on_tab(SI.TABS_BAR_HEADERS[1])

    def click_on_plugins_tab(self) -> None:
        self.click_on_tab(SI.TABS_BAR_HEADERS[2])

    def click_on_memory_usage_tab(self) -> None:
        self.click_on_tab(SI.TABS_BAR_HEADERS[3])

    def select_timespan(self, option: str) -> None:
        element = self.wait_to_be_visible(self.Locator.TIMESPAN_DROPDOWN, timeout=5)
        Select(element).select_by_visible_text(option)

    def get_graph_for_selected_timespan_option(self, option: str) -> WebElement | bool:
        self.select_timespan(option)
        graph_locator = self.Locator.memory_usage_graph(SI.TIMESPAN_OPTIONS.get(option))
        try:
            return self.wait_to_be_visible(graph_locator, timeout=5)
        except TimeoutException:
            return False
