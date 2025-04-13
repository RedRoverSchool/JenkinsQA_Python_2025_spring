from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def modal(driver):
    driver.get("https://demoqa.com/modal-dialogs")
    return driver

def test_small_modal_dialog(modal):
    sm_text = "This is a small modal. It has very less content"
    waiter5 = WebDriverWait(modal, 5)
    modal.find_element(By.ID, "showSmallModal").click()
    waiter5.until(EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]')))
    modal.switch_to.active_element.find_element(By.XPATH, '//div[@role="dialog"]')
    sm_title = modal.find_element(By.CLASS_NAME, "modal-title").text
    sm_body = modal.find_element(By.CLASS_NAME, "modal-body").text
    sm_button = modal.find_element(By.ID, "closeSmallModal")
    sm_button_text = sm_button.text
    sm_button.click()

    assert sm_title == "Small Modal"
    assert sm_body == sm_text
    assert sm_button_text == "Close"

def test_large_modal_dialog(modal):
    lm_text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    waiter5 = WebDriverWait(modal, 5)
    modal.find_element(By.ID, "showLargeModal").click()
    waiter5.until(EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]')))
    modal.switch_to.active_element.find_element(By.XPATH, '//div[@role="dialog"]')
    lm_title = modal.find_element(By.CLASS_NAME, "modal-title").text
    lm_body = modal.find_element(By.CLASS_NAME, "modal-body").text
    lm_button = modal.find_element(By.ID, "closeLargeModal")
    lm_button_text = lm_button.text
    lm_button.click()

    assert lm_title == "Large Modal"
    assert lm_body == lm_text
    assert lm_button_text == "Close"