import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def sauce(driver):
    """Фикстура для открытия сайта"""
    driver.get("https://www.saucedemo.com/")
    return driver


@pytest.fixture
def authorized_user(sauce):
    """Фикстура для авторизованного пользователя"""
    sauce.find_element(By.ID, "user-name").send_keys("standard_user")
    sauce.find_element(By.ID, "password").send_keys("secret_sauce" + Keys.RETURN)
    WebDriverWait(sauce, 10).until(
        EC.url_to_be("https://www.saucedemo.com/inventory.html")
    )
    expected_url = "https://www.saucedemo.com/inventory.html"
    assert sauce.current_url == expected_url, (
        f"Ожидался URL c 'inventory', но получен: {sauce.current_url}"
    )
    yield sauce


def test_get_title(sauce):
    actual_title = sauce.title
    expected_title = "Swag Labs"
    assert actual_title == expected_title, f"wrong title. expected '{expected_title}'"


@pytest.mark.xfail(reason="Expected failure due to Google password change popup")
def test_add_to_cart(authorized_user):
    authorized_user.find_element(
        By.XPATH, "//button[contains(text(),'Add to cart')]"
    ).click()
    authorized_user.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(authorized_user, 10).until(EC.url_contains("cart"))
    assert "cart" in authorized_user.current_url


def test_sort_price(authorized_user):
    authorized_user.find_element(By.CLASS_NAME, "product_sort_container").click()
    authorized_user.find_element(
        By.XPATH, "//option[contains(text(), 'Price (low to high)')]"
    ).click()
    text = authorized_user.find_element(
        By.XPATH, "//*[contains(text(), 'Sauce Labs Onesie')]"
    ).text
    assert text == "Sauce Labs Onesie"
