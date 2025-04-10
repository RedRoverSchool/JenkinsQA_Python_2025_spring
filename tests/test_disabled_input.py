from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_disabled_input():
    driver = webdriver.Chrome()
    waiter10 = WebDriverWait(driver, 10)

    BASE_URL = "http://uitestingplayground.com/disabledinput"
    my_text = "It is my own text, entered into enabled field!"
    expected_text = f"Value changed to: {my_text}"

    driver.get(BASE_URL)
    driver.find_element(By.ID, "enableButton").click()
    waiter10.until(EC.text_to_be_present_in_element((By.ID, "opstatus"), "Input Enabled..."))
    driver.find_element(By.ID, "inputField").send_keys(my_text)
    driver.find_element(By.ID, "opstatus").click()
    actual_text = driver.find_element(By.ID, "opstatus").text
    driver.quit()

    assert actual_text == expected_text, "Expected text not equal to actual text"