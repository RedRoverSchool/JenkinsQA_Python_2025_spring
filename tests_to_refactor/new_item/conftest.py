import pytest
from tests.new_item.data_structs import NewItem
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#@pytest.fixture()
#def new_item_page(main_page, config):
#    new_item_button = main_page.find_element(*NewItem.new_item_button_selector)
#    new_item_button.click()
#    wait = WebDriverWait(main_page, 5)
#    wait.until(EC.url_matches(config.jenkins.base_url + NewItem.url))
#
#    return main_page


@pytest.fixture()
def wait5(new_item_page):
    return WebDriverWait(new_item_page, 5)


def create_freestyle_item(new_item_page, config, wait5):
    new_item_page.find_element(*NewItem.name_field_selector).send_keys(NewItem.positive_name)
    new_item_page.find_element(*NewItem.freestyle_selector).click()
    wait5.until(EC.element_to_be_clickable(NewItem.ok_button_selector)).click()
    wait5.until(EC.url_to_be(config.jenkins.base_url + NewItem.configuration_page))
    new_item_page.find_element(*NewItem.save_button_selector).click()
    wait5.until(EC.url_to_be(config.jenkins.base_url + NewItem.item_page))


@pytest.fixture()
def prepare_new_item(new_item_page, config, wait5):
    create_freestyle_item(new_item_page, config, wait5)
    new_item_page.get(config.jenkins.base_url + NewItem.url)
    wait5.until(EC.url_to_be(config.jenkins.base_url + NewItem.url))

    return new_item_page
