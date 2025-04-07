from _ast import Assert

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement



def test_register_user():

    driver = webdriver.Chrome()
    driver.get("https://www.automationexercise.com/")
    newUserSignup = driver.find_element(By.CSS_SELECTOR, "a[href='/'][style='color: orange;']")
    assert newUserSignup.is_displayed() , "User signup display is not visible"

    driver.quit()
