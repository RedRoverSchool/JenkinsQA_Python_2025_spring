from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def test_start():

 browser = webdriver.Chrome()
 browser.get("https://www.qa-practice.com/elements/button/simple")
 browser.find_element(By.ID, 'submit-id-submit').click()

 sleep(1)
 browser.quit()