import pytest
from random import choice as rand_choice
from selenium.webdriver.common.by import By
from time import sleep

hcities = ["Архангельск", "Барнаул", "Выборг", "Грозный", "Дигора"]
expected_city = rand_choice(hcities)


@pytest.fixture(autouse=True)
def helix_loader(driver):
    driver.get("https://helix.ru")
    sleep(2)  # Prevent 404 page site bug, NOT DEBUG
    # Press NO to 'autodetected' SPB City
    driver.find_element(By.XPATH, "//button[@data-testid='reject-city-button']").click()  # noqa: E501


@pytest.fixture
def city_changer(driver):
    input_city_field = driver.find_element(
        By.XPATH, "//app-city//input[@type='search']"
    )  # noqa: E501
    input_city_field.send_keys(expected_city)
    driver.find_element(
        By.XPATH,
        "//*[@data-testid='important-city-0' and contains(text(), expected_city)]",
    ).click()  # noqa: E501
    sleep(3)  # Page load delay, required


@pytest.fixture
def LKK_Login(driver):
    driver.find_element(
        By.XPATH, '//app-helix-header//a[@data-testid="header-nav-personal-account"]'
    ).click()  # noqa: E501
    driver.find_element(By.ID, "email").send_keys("testmi-1@ya.ru")
    driver.find_element(By.ID, "pass").send_keys("asdASD11!!")
    driver.find_element(
        By.XPATH, "//button[contains(text(), 'Перейти в мой Личный кабинет')]"
    ).click()  # noqa: E501
    sleep(3)  # Page load delay, required
    driver.find_element(By.XPATH, "//header/a").click()


def test_city_change(driver, city_changer):
    current_city = driver.find_element(
        By.XPATH, "//app-helix-header//span[@data-testid='current-city']"
    ).text  # noqa: E501
    assert current_city == expected_city, "Expected City Not Recieved"  # noqa: E501


def test_login_sequence_with_city_change(driver, city_changer, LKK_Login):
    """Helix.ru login with change city test."""
    Uname = driver.find_element(By.XPATH, "//app-user-info-button").text
    assert Uname == "For Showing Cutout behavior at long S.", (
        "Expected Username Not Recieved"
    )  # noqa: E501
