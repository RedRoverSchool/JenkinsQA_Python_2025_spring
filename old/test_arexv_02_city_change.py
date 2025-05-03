from time import sleep  # noqa: D100
from selenium import webdriver
from selenium.webdriver.common.by import By


# Chrome Ignore SSL Err Settings
options = webdriver.ChromeOptions()
options.add_argument("ignore-certificate-errors")

Expected_City = "Барнаул"


# On-Site Actions
def test_city_change():
    """Helix.ru change city test."""
    driver.get("https://helix.ru")
    sleep(2)  # Prevent 404 page site bug, NOT DEBUG
    # Press NO to 'autodetected' SPB City
    driver.find_element(By.XPATH, "//button[@data-testid='reject-city-button']").click()  # noqa: E501

    # Found City via search field
    input_city_field = driver.find_element(
        By.XPATH, "//app-city//input[@type='search']"
    )  # noqa: E501
    input_city_field.send_keys(Expected_City)
    sleep(3)  # Page Update Time, required, NOT DEBUG
    driver.find_element(
        By.XPATH,
        "//*[@data-testid='important-city-0' and contains(text(), Expected_City)]",
    ).click()  # noqa: E501

    # Set Current City param from Main Page
    sleep(3)  # Page Update Time, required, NOT DEBUG
    Current_City = driver.find_element(
        By.XPATH, "//app-helix-header//span[@data-testid='current-city']"
    ).text  # noqa: E501

    driver.quit()

    # Check Current City set as expected
    assert Current_City == "Expected_City", "Expected City Not Recieved"  # noqa: E501


driver = webdriver.Chrome(options)  # Chrome usage
test_city_change()

driver = webdriver.Firefox()  # FF usage
test_city_change()
