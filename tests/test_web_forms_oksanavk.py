import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_fill_out(driver):

    wait = WebDriverWait(driver, 10)

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    driver.find_element(By.ID, "my-text-id").send_keys("faketext")
    driver.find_element(By.NAME, "my-password").send_keys("123OOO")
    driver.find_element(By.NAME, "my-textarea").send_keys("The Performance > Summary tab now shows links")
    dropdown_select = Select(driver.find_element(By.NAME, "my-select"))
    dropdown_select.select_by_visible_text("Two")
    datalist_dropdown = driver.find_element(By.NAME, "my-datalist")
    datalist_dropdown.send_keys("New York")
    datalist_dropdown.send_keys(Keys.TAB)
    checkbox1 = driver.find_element(By.ID, "my-check-1")
    if checkbox1.is_selected():
        checkbox1.click()

    checkbox2 = driver.find_element(By.ID, "my-check-2")
    if not checkbox2.is_selected():
        checkbox2.click()

    radio1 = driver.find_element(By.ID, "my-radio-1")
    radio2 = driver.find_element(By.ID, "my-radio-2")
    if radio1.is_selected() and not radio2.is_selected():
        radio2.click()

    driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]").click()
    conf_message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    assert "Received!" in conf_message.text



