from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_successful_login():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    try:
        # Поиск элементов и действия
        username = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username.send_keys("standard_user")

        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Проверка успешного входа
        WebDriverWait(driver, 15).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "title"), "Products")
        )

    finally:
        # Закрытие браузера
        driver.quit()
