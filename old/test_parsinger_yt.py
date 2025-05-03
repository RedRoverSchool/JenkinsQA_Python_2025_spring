from selenium.webdriver.common.by import By


def test_result_text(driver):
    driver.get("https://parsinger.ru/selenium/3/3.2.3/index.html")

    driver.find_element(By.ID, "showTextBtn").click()
    password_field = driver.find_element(By.ID, "userInput")
    password_field.send_keys(driver.find_element(By.ID, "text1").text)
    driver.find_element(By.ID, "checkBtn").click()
    result = driver.find_element(By.ID, "text2")

    assert result.text == "G00D-J0B-T0M-P0W3R"


def test_password_text(driver):
    driver.get("https://parsinger.ru/selenium/3/3.3.1/index.html")

    button = driver.find_element(By.ID, "parent_id").find_element(
        By.CLASS_NAME, "child_class"
    )
    button.click()

    assert button.get_attribute("password") == "GET-TH1S-C0D3"
