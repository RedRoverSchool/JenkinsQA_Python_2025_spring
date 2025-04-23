import time
import pytest
from selenium.webdriver.common.by import By

@pytest.fixture
def prod_page(driver):
     driver.get('http://automationexercise.com')
     elem =  driver.find_element(By.XPATH, "//ul[@class = 'nav navbar-nav']/li[2]/a")
     elem.click()
     time.sleep(5)
     assert driver.current_url == 'https://automationexercise.com/products'
     yield driver
     driver.quit()

def test_search_exist_prod(prod_page):
     search_bar = prod_page.find_element(By.XPATH, "//input[@name='search']")
     search_bar.send_keys("Lace Top For Women")
     prod_page.find_element(By.XPATH, '//*[@id="submit_search"]').click()
     time.sleep(3)
     prod_image = prod_page.find_element(By.XPATH, "//div[@class= 'productinfo text-center']/img")
     assert prod_image.is_displayed()
     assert prod_page.current_url == 'https://automationexercise.com/products?search=Lace%20Top%20For%20Women'

def test_search_non_exist_prod(prod_page):
     search_bar = prod_page.find_element(By.XPATH, "//input[@name='search']")
     search_bar.send_keys("Blue skirt")
     prod_page.find_element(By.XPATH, '//*[@id="submit_search"]').click()
     time.sleep(3)
     products = prod_page.find_elements(By.XPATH, "//div[@class= 'productinfo text-center']/img")
     assert len(products) == 0
