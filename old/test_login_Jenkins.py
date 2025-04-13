from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080/login?from=%2F")
    driver.find_element(By.NAME, "j_username").send_keys("admin")
    driver.find_element(By.NAME, "j_password").send_keys("admin")
    driver.find_element(By.XPATH, "//*[@id='main-panel']/div/form/button").click()

    assert driver.find_element(By.ID,"jenkins-name-icon")
    driver.quit()