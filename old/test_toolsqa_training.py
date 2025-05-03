import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

DEMO_URL = "https://demoqa.com"
TRAINING_URL = "https://www.toolsqa.com/selenium-training/"
DEMO_TITLE = "DEMOQA"
TRAINING_TITLE = "Tools QA - Selenium Training"
JOIN_NOW_BUTTON = (By.XPATH, "//img[@alt='Selenium Online Training']")


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestToolsQATraining:
    def test_demoqa_main_page(self, driver):
        """
        Open https://demoqa.com and check page title
        """
        driver.get(DEMO_URL)
        assert driver.title == DEMO_TITLE

    def test_toolsqa_training_page(self, driver):
        """
        Open https://demoqa.com, click "JOIN NOW" button, switch driver to new opened tab and check page title
        """
        driver.get(DEMO_URL)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(JOIN_NOW_BUTTON)
        ).click()
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(lambda d: d.title != "")
        assert driver.title == TRAINING_TITLE
