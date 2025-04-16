import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="function")
def wait(driver):
    return WebDriverWait(driver, 10)


@pytest.fixture(scope="function")
def faker_data():
    fake = Faker()
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.ascii_free_email(),
        "password": fake.password(length=8)
    }


@pytest.fixture
def custom_base_url():
    return "https://magento.softwaretestingboard.com"


def test_auth_positive(driver, custom_base_url, wait, faker_data):
    driver.get(f"{custom_base_url}/customer/account/create")
    driver.find_element(By.XPATH, "//input[@id='firstname']").send_keys(faker_data['first_name'])
    driver.find_element(By.XPATH, "//input[@id='lastname']").send_keys(faker_data['last_name'])
    email_field = wait.until(EC.presence_of_element_located((By.ID, "email_address")))
    email_field.send_keys(faker_data['email'])
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys(faker_data['password'])
    driver.find_element(By.XPATH, "//*[@id='password-confirmation']").send_keys(faker_data['password'])
    driver.find_element(By.XPATH, "//button[@title='Create an Account']").click()
    expected_url_part = "/customer/account"
    assert expected_url_part in driver.current_url, f"Expected URL to contain '{expected_url_part}', but got: {driver.current_url}"
