import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.saucedemo.com/'
username_standard = 'standard_user'
password = 'secret_sauce'

# ✅ fixture setup/teardown
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# ✅ Login with wait
def login_standard_user(driver):
    driver.get(url)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'user-name'))).send_keys(username_standard)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-button').click()

# ✅ Test URL
def test_standard_user_login(driver):
    url_text = "inventory"
    login_standard_user(driver)
    WebDriverWait(driver, 5).until(EC.url_contains("inventory"))
    assert url_text in driver.current_url

# ✅ Test title
def test_standard_user_title(driver):
    titel = "Products"
    login_standard_user(driver)
    title = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-test='title']"))
    )
    assert title.text == titel, (f'expected result {titel} but got {title.text}')

def test_product_add(driver):
    expext_result = '1'
    login_standard_user(driver)
    add_to_cart_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack"))).click()
    basket_lago = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#shopping_cart_container"))).click()
    item_count = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-test='item-quantity']"))).text
    assert item_count == expext_result,(f"ecpected result {expext_result}, bot got {item_count}")

