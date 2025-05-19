# import pytest
# from tests.new_item.data_structs import NewItem
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


#@pytest.fixture()
#def new_item_page(main_page, config):
#    new_item_button = main_page.find_element(*NewItem.new_item_button_selector)
#    new_item_button.click()
#    wait = WebDriverWait(main_page, 5)
#    wait.until(EC.url_matches(config.jenkins.base_url + NewItem.url))
#
#    return main_page
