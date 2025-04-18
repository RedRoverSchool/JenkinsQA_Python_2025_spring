from time import sleep
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_wikipedia_steve_jobs_heading_present(driver):
    # Open the main Wikipedia page
    driver.get("https://www.wikipedia.org/")

    # Choosing English
    driver.find_element(By.ID, "js-link-box-en").click()

    wait = WebDriverWait(driver, 10)
    search_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//input[@class='cdx-text-input__input'])[1]")))

    # looking for "Steve Jobs"
    search_input = driver.find_element(By.XPATH, "(//input[@class='cdx-text-input__input'])[1]")
    search_input.send_keys("Steve Jobs")
    search_input.send_keys(Keys.RETURN)

    # waiting for the heading to appear on the page
    heading = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "firstHeading"))
    )

    # Checking that the heading is on the page — "Steve Jobs"
    assert heading.text == "Steve Jobs"
