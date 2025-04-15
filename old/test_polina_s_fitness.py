from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_cart_page_url():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://market.fitnesshouse.ru/")
    driver.find_element(By.XPATH, '//a [@class="fh-cart-btn btn btn-outline-light ml-sm-3"]').click()
    WebDriverWait(driver,10)

    expected_url = "https://market.fitnesshouse.ru/cart"
    actual_url = driver.current_url

    assert actual_url == expected_url, f"Ожидался URL: '{expected_url}', получен URL: '{actual_url}'"

    driver.quit()