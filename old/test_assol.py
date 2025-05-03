from selenium import webdriver
from selenium.webdriver.common.by import By


def test_simple_button_work():
    browser = webdriver.Chrome()
    browser.get("https://www.qa-practice.com/elements/button/simple")
    button = browser.find_element(By.ID, "submit-id-submit")
    button.click()
    result = browser.find_element(By.ID, "result-text").text
    assert result == "Submitted", "Надпись 'Submitted' не появилась"

    browser.quit()
