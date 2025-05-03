from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from tests.display_system_information.base_methods import BaseMethods
from tests.display_system_information.locators import SystemInformationPage as SI


class SystemInformationPage(BaseMethods):
    ENDPOINT_URL = '/manage/systemInfo'
    TAB_TITLE = 'System Information [Jenkins]'
    TABS = ['System Properties', 'Environment Variables', 'Plugins', 'Memory Usage', 'Thread Dumps']
    SYS_ENV_TABS = TABS[:2]
    TIMESPAN_OPTIONS = {'Short': 'sec10&width', 'Medium': 'min&width', 'Long': 'hour&width'}

    def __init__(self, sys_info_page: WebDriver):
        super().__init__(sys_info_page)

    def get_data_table_id(self, anchor_locator) -> str:
        return self.get_attribute('data-table-id', anchor_locator)

    def get_table_td_values(self, table_id: str) -> list[str]:
        table = self.driver.find_element(By.ID, table_id)
        rows = table.find_elements(By.TAG_NAME, "tr")
        first_td_values = []
        for row in rows:
            tds = row.find_elements(By.TAG_NAME, "td")
            if tds:
                first_td_text = tds[0].text.strip()
                if first_td_text:
                    first_td_values.append(first_td_text)
        return first_td_values

    def get_all_element_names(self, anchor_locator):
        # for System Properties and Environment Variables tabs only
        data_table_id = self.get_data_table_id(anchor_locator)
        return self.get_table_td_values(data_table_id)

    def define_show_single_value_button_locator(self, element_name: str) -> tuple[str, str]:
        return By.XPATH, f"//tr[td[normalize-space(text())='{element_name}']]//button[contains(normalize-space(.), 'Hidden value, click to show this value')]"

    def define_hide_single_value_button_locator(self, element_name: str) -> tuple[str, str]:
        return By.XPATH, f"//tr[td[normalize-space(text())='{element_name}']]//div[contains(@class, 'app-hidden-info-hide')]//button"

    def is_value_displayed(self, element_name: str) -> bool:
        locator = self.define_hide_single_value_button_locator(element_name)
        button_element = self.find_element(locator)
        if not button_element:
            return False
        button_text = button_element.text.strip()
        return button_text != "Hidden value, click to show this value"

    def find_table_element(self, table_id: str) -> WebElement:
        return self.find_element((By.ID, table_id))

    def number_of_plugins_in_table(self, table_body_locator: tuple[str, str]) -> int:
        table = self.find_element(table_body_locator)
        return len(table.find_elements(By.TAG_NAME, "tr"))

    def get_plugin_info(self, number: int) -> tuple[tuple[str, str], tuple[str, str], tuple[str, str], str]:
        name_locator = (By.XPATH, f"(//table[@class='jenkins-table sortable'])[3]/tbody/tr[{number}]/td[1]//a")
        version_locator = (By.XPATH, f"(//table[@class='jenkins-table sortable'])[3]/tbody/tr[{number}]/td[2]")
        enabled_locator = (By.XPATH, f"(//table[@class='jenkins-table sortable'])[3]/tbody/tr[{number}]/td[3]")
        plugin_name = self.get_element_text(name_locator)
        return name_locator, version_locator, enabled_locator, plugin_name

    def select_timespan(self, text: str):
        element = self.get_element(SI.TIMESPAN_DROPDOWN)
        Select(element).select_by_visible_text(text)

    def get_graph_locator(self, flag_value: str):
        return By.XPATH, f"//img[@alt='Memory usage graph' and contains(@src, '{flag_value}')]"
