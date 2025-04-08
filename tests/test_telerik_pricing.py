from selenium import webdriver
from selenium.webdriver.common.by import By


def test_see_plans_and_pricing ():
    driver = webdriver.Chrome()
    driver.get('https://www.telerik.com/support/demos')
    driver.find_element(By.XPATH, "//a[normalize-space(text())='See Plans & Pricing']").click()

    assert driver.find_element(By.XPATH, "//h1[text()='Pricing']").is_displayed()

    driver.quit()
