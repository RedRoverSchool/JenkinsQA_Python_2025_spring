from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .data_structs import NewItem, FreestyleItem


def create_freestyle_item(new_item_page, config):
    wait = WebDriverWait(new_item_page, 15)
    new_item_page.find_element(*NewItem.name_field_selector).send_keys(NewItem.positive_name)
    new_item_page.find_element(*FreestyleItem.freestyle_selector).click()
    wait.until(EC.element_to_be_clickable(NewItem.ok_button_selector)).click()
    wait.until(EC.url_to_be(config.jenkins.base_url + FreestyleItem.configuration_page))
    new_item_page.find_element(*FreestyleItem.save_button_selector).click()
    wait.until(EC.url_to_be(config.jenkins.base_url + FreestyleItem.item_page))
    new_item_page.get(config.jenkins.base_url + NewItem.url)
    wait.until(EC.url_to_be(config.jenkins.base_url + NewItem.url))

    return new_item_page
