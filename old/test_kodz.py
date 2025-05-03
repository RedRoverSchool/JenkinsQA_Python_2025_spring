import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

driver_path = (
    "C:/Users/Natasha/GitProjects/chromedriver/chromedriver-win64/chromedriver.exe"
)


@pytest.fixture
def driver():
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://staging.scrive.com/t/9221714692410699950/7348c782641060a9")
    yield driver
    driver.quit()


def fill_name(driver, id, name):
    name_input = driver.find_element(By.ID, id)
    name_input.send_keys(name)


def click_on_button(driver, xpath):
    button = driver.find_element(By.XPATH, xpath)
    button.click()


def take_screenshot(driver, selector):
    modal = driver.find_element(By.CSS_SELECTOR, selector)
    modal.screenshot("modal.png")


def verify_message(driver, xpath, text):
    message = driver.find_element(By.XPATH, xpath)
    message_text = message.text
    assert text in message_text, f"Expected '{text}', but got '{message_text}'"


def test_document_sign_flow(driver):
    fill_name(driver, "name", "Natallia")
    click_on_button(driver, "/html/body/div/div/div[3]/div[4]/div[1]/a[1]")
    time.sleep(3)
    take_screenshot(
        driver, "body > div > div > div.main > div.section.sign.above-overlay"
    )
    click_on_button(driver, "/html/body/div/div/div[3]/div[4]/div[1]/a[1]")
    time.sleep(3)
    verify_message(
        driver,
        "/html/body/div/div/div[3]/div[2]/div[2]/div/div[1]/h1/span",
        "Document signed!",
    )
