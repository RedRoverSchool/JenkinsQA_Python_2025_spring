import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def login(driver, config, wait):
    driver.get('https://www.saucedemo.com/')
    wait.until(EC.presence_of_element_located((By.ID, 'user-name'))).send_keys('performance_glitch_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

def test_standard_user_login(driver, login, wait):
    wait.until(EC.url_contains("inventory"))
    assert "inventory" in driver.current_url

def test_standard_user_title(driver, login, wait):
    expected_title = "Products"
    title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-test='title']")))
    assert title.text == expected_title, (f'expected result {expected_title} but got {title.text}')

@pytest.mark.skip(reason="Skipping due to Google password popup issue")
def test_product_add(driver, login, wait):
    basket_logo = '1'
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack"))).click()
    basket_lago = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#shopping_cart_container"))).click()
    item_count = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-test='item-quantity']"))).text
    assert item_count == basket_logo,(f"ecpected result {basket_lago}, bot got {item_count}")