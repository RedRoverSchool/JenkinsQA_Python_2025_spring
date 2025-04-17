from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.yahoo.com")

import time
time.sleep(2)  # Подожди 2 секунды
print(driver.title)

assert "Google" in driver.title

driver.quit()