from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.freestyle_project.freestyle_data import Freestyle


def test_buttons_available(freestyle):
    wait = WebDriverWait(freestyle, 10)
    save_button = wait.until(
        EC.presence_of_element_located((By.XPATH, '//button[@name="Submit"]'))
    )
    apply_button = freestyle.find_element(By.XPATH, '//button[@name="Apply"]')

    assert save_button.is_displayed() and apply_button.is_displayed()


def test_save_config(freestyle):
    wait = WebDriverWait(freestyle, 10)
    wait.until(
        EC.presence_of_element_located((By.XPATH, '//button[@name="Submit"]'))
    ).click()
    h1_text = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//h1[@class="job-index-headline page-headline"]')
        )
    ).text

    assert h1_text == Freestyle.project_name


def test_applay_config(freestyle):
    wait = WebDriverWait(freestyle, 10, 0.1)
    wait.until(
        EC.presence_of_element_located((By.XPATH, '//button[@name="Apply"]'))
    ).click()
    saved_notification = wait.until(
        EC.presence_of_element_located((By.ID, "notification-bar"))
    )
    h1_text = freestyle.find_element(By.CSS_SELECTOR, "h1").text

    assert saved_notification.is_enabled()
    assert h1_text == "Configure"
