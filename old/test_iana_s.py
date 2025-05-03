from selenium import webdriver
from selenium.webdriver.common.by import By


def test_log_in_url_check():
    driver = webdriver.Chrome()
    driver.get("https://demo.applitools.com/")
    driver.find_element(By.ID, "username").send_keys("Iana")
    driver.find_element(By.ID, "password").send_keys("qwaszx")
    driver.find_element(By.ID, "log-in").click()
    assert driver.current_url == "https://demo.applitools.com/app.html"
    driver.quit()
