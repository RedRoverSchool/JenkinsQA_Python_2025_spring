from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestSauceDemo:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

    def teardown_method(self):
        self.driver.quit()

    def test_login_success(self):
        assert "inventory" in self.driver.current_url

    def test_add_to_cart(self):

        self.driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        time.sleep(1)

        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "1"