from time import sleep  # noqa: D100
from selenium import webdriver
from selenium.webdriver.common.by import By


# Chrome Ignore SSL Err Settings
options = webdriver.ChromeOptions()
options.add_argument("ignore-certificate-errors")

Expected_City = "Барнаул"


# On-Site Actions
def test_login_sequence_with_city_change():
    """Helix.ru login with change city test."""
    driver.get("https://helix.ru")
    sleep(2)  # Prevent 404 page site bug, NOT DEBUG
    # Press NO to 'autodetected' SPB City
    driver.find_element(By.XPATH, "//button[@data-testid='reject-city-button']").click()  # noqa: E501

    # Found City via search field
    input_city_field = driver.find_element(
        By.XPATH, "//app-city//input[@type='search']"
    )  # noqa: E501
    input_city_field.send_keys(Expected_City)
    sleep(1)  # Page Update Time, required, NOT DEBUG
    driver.find_element(
        By.XPATH,
        "//*[@data-testid='important-city-0' and contains(text(), Expected_City)]",
    ).click()  # noqa: E501
    sleep(3)  # Page Update Time, required, NOT DEBUG
    # Go to login page
    driver.find_element(
        By.XPATH, '//app-helix-header//a[@data-testid="header-nav-personal-account"]'
    ).click()  # noqa: E501
    # Fill input fields
    driver.find_element(By.ID, "email").send_keys("testmi-1@ya.ru")
    driver.find_element(By.ID, "pass").send_keys("asdASD11!!")
    # Press button
    driver.find_element(
        By.XPATH, "//button[contains(text(), 'Перейти в мой Личный кабинет')]"
    ).click()  # noqa: E501
    sleep(5)  # Page load delay, NOT DEBUG
    # Return to main page
    driver.find_element(By.XPATH, "//header/a").click()
    sleep(3)  # Page load delay, NOT DEBUG
    Uname = driver.find_element(By.XPATH, "//app-user-info-button").text

    driver.quit()

    # Check Username on Helix.ru main page
    assert Uname == "For Showing Cutout behavior at long S.", (
        "Expected Username Not Recieved"
    )  # noqa: E501


driver = webdriver.Chrome(options)  # Chrome usage
test_login_sequence_with_city_change()

driver = webdriver.Firefox()  # FF usage
test_login_sequence_with_city_change()
