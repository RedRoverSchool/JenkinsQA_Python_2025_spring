from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class FreestylePJConfOptPage(BasePage):
    def __init__(self, freestyle):
        super().__init__(freestyle)

    def check_trigger_title(self):
        title_triggers = self.find_element(By.ID, 'triggers')
        return title_triggers.is_displayed

    def check_box_enable(self, option_name: str):
        el = self.find_element(By.NAME, option_name)
        el.send_keys(Keys.SPACE)
        return el.is_selected()
    
    def check_box_disable(self, option_name: str):
        el = self.find_element(By.NAME, option_name)
        el.send_keys(Keys.SPACE)
        el.send_keys(Keys.SPACE)
        return el.is_selected()