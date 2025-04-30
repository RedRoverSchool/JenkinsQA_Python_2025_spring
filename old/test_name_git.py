import time

from selenium import webdriver
from selenium.webdriver.common.by import By

name = "Bond"


def test_name():
    driver = webdriver.Chrome()
    base_url = 'https://gh-users-search.netlify.app/'
    driver.get(base_url)

    user_name = driver.find_element(By.CSS_SELECTOR, "[data-testid='search-bar']")
    user_name.send_keys(name)
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    time.sleep(2)
    temp = driver.find_element(By.XPATH, '//section[3]/div/article[1]/header/div/h4')
    search_result = temp.text
    print(search_result, "was found.")
    assert name in search_result, "Name not found"

    driver.quit()
