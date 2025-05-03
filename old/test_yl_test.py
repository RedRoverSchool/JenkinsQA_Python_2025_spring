from selenium import webdriver
from selenium.webdriver.common.by import By


def test_register_user():
    driver = webdriver.Chrome()
    driver.get("https://www.automationexercise.com/")
    new_user_signup = driver.find_element(
        By.CSS_SELECTOR, "a[href='/'][style='color: orange;']"
    )
    assert new_user_signup.is_displayed(), "User signup display is not visible"

    driver.quit()
