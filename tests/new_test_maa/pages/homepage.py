
from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    def count_img_on_homepage(self, cnt: int):
        value = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item_img > a")
        assert len(value) == cnt

    def add_product_to_cart(self, cnt=1):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a").click()
        value = self.driver.find_elements(By.CLASS_NAME, "cart_item_label")
        assert len(value) == cnt

