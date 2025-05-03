import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSearch(unittest.TestCase):
    def test_search(self):
        driver = webdriver.Chrome()

        driver.get("https://www.vpl.ca/")

        text_box = driver.find_element(By.NAME, "keyword")
        search_button = driver.find_element(By.CSS_SELECTOR, "#edit-submit")

        text_box.send_keys("Python")
        search_button.click()

        text = driver.find_element(By.CLASS_NAME, "search-query")
        value = text.text

        self.assertEqual(value, "Keyword search: Python")

        driver.quit()
