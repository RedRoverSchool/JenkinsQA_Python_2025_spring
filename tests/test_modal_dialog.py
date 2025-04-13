from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def modal(driver):
    driver.get("https://demoqa.com/modal-dialogs")
    return driver

@pytest.mark.parametrize(
    "body_text, id_show, id_button, title",
    [
        ("This is a small modal", "showSmallModal", "closeSmallModal", "Small Modal"),
        ("Lorem Ipsum is simply dummy text of the printing and typesetting industry", "showLargeModal",
         "closeLargeModal", "Large Modal")
    ]
)
def test_modal_dialog(modal, body_text, id_show, id_button, title):
    waiter5 = WebDriverWait(modal, 5)
    modal.find_element(By.ID, id_show).click()
    waiter5.until(EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]')))
    modal.switch_to.active_element.find_element(By.XPATH, '//div[@role="dialog"]')
    m_title = modal.find_element(By.CLASS_NAME, "modal-title").text
    m_body = modal.find_element(By.CLASS_NAME, "modal-body").text.split(".")
    m_button = modal.find_element(By.ID, id_button)
    m_button_text = m_button.text
    m_button.click()

    assert m_title == title
    assert m_body[0] == body_text
    assert m_button_text == "Close"

# def test_large_modal_dialog(modal):
#     lm_text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
#     waiter5 = WebDriverWait(modal, 5)
#     modal.find_element(By.ID, "showLargeModal").click()
#     waiter5.until(EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]')))
#     modal.switch_to.active_element.find_element(By.XPATH, '//div[@role="dialog"]')
#     lm_title = modal.find_element(By.CLASS_NAME, "modal-title").text
#     lm_body = modal.find_element(By.CLASS_NAME, "modal-body").text
#     lm_button = modal.find_element(By.ID, "closeLargeModal")
#     lm_button_text = lm_button.text
#     lm_button.click()
#
#     assert lm_title == "Large Modal"
#     assert lm_body == lm_text
#     assert lm_button_text == "Close"