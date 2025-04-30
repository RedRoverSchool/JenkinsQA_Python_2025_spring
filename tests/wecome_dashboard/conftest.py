import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def new_item_page_opens_after_clicking_create_job_block(main_page, config):
    wait5 = WebDriverWait(main_page, 5)
    wait5.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Create a job']"))).click()
    return main_page


@pytest.fixture(scope="function")
def new_item_page_opens_after_clicking_plus_in_create_job_block(main_page, config):
    wait5 = WebDriverWait(main_page, 5)
    wait5.until(EC.presence_of_element_located((By.XPATH, "//*[@class='trailing-icon'][1]"))).click()
    return main_page
