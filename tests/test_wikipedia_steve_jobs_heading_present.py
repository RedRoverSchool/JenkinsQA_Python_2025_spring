from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
# @pytest.fixture
# def driver():
#     # driver settings
#     options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(options=options)
#     driver.set_window_size(1920, 1080)
#     driver.implicitly_wait(5)  # we wait up to 5 seconds to find the elements
#     yield driver
#     driver.quit()  # Closing the browser after completing the test


def test_wikipedia_steve_jobs_heading_present(driver):
    # Open the main Wikipedia page
    driver.get("https://www.wikipedia.org/")

    # Choosing English
    driver.find_element(By.ID, "js-link-box-en").click()
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
