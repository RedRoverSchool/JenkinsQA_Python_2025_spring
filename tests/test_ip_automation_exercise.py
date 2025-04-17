import pytest
import calendar
import datetime
import uuid
from random import randrange
from faker import Faker
from selenium.webdriver.common.by import By


@pytest.fixture
def automation_exercise(driver):
    driver.get("http://automationexercise.com")
    return driver


@pytest.fixture
def random_string():
    return str(uuid.uuid4())


@pytest.fixture()
def random_dob():
    start_date = datetime.date(1904, 1, 1)
    end_date = datetime.date(2007, 12, 31)
    delta = end_date - start_date
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)

    return start_date + datetime.timedelta(seconds=random_second)


@pytest.fixture
def user_data(random_string, random_dob):
    user_name = random_string
    date_of_birth = random_dob
    fake = Faker()

    return {
        "name": user_name,
        "email": f"{user_name}@test.com",
        "password": random_string,
        "day": date_of_birth.day,
        "month": calendar.month_name[date_of_birth.month],
        "year": date_of_birth.year,
        "first_name": user_name,
        "last_name": random_string,
        "company": random_string,
        "address": fake.street_address(),
        "city": fake.city(),
        "state": fake.state(),
        "country": "United States",
        "zip": fake.zipcode(),
        "phone": f"+1 {Faker().msisdn()[3:]}"
    }


def test_register_user(automation_exercise, user_data):
    automation_exercise.find_element(By.LINK_TEXT, "Signup / Login").click()
    automation_exercise.find_element(By.NAME, "name").send_keys(user_data.get("name"))
    automation_exercise.find_element(By.CSS_SELECTOR, "[data-qa='signup-email']").send_keys(user_data.get("email"))
    automation_exercise.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()
    automation_exercise.find_element(By.NAME, "title").click()
    automation_exercise.find_element(By.ID, "password").send_keys(user_data.get("password"))
    automation_exercise.find_element(By.ID, "days").send_keys(user_data.get("day"))
    automation_exercise.find_element(By.ID, "months").send_keys(user_data.get("month"))
    automation_exercise.find_element(By.ID, "years").send_keys(user_data.get("year"))
    automation_exercise.find_element(By.ID, "first_name").send_keys(user_data.get("first_name"))
    automation_exercise.find_element(By.ID, "last_name").send_keys(user_data.get("last_name"))
    automation_exercise.find_element(By.ID, "company").send_keys(user_data.get("company"))
    automation_exercise.find_element(By.ID, "address1").send_keys(user_data.get("address"))
    automation_exercise.find_element(By.ID, "country").send_keys(user_data.get("country"))
    automation_exercise.find_element(By.ID, "state").send_keys(user_data.get("state"))
    automation_exercise.find_element(By.ID, "city").send_keys(user_data.get("city"))
    automation_exercise.find_element(By.ID, "zipcode").send_keys(user_data.get("zip"))
    automation_exercise.find_element(By.ID, "mobile_number").send_keys(user_data.get("phone"))
    automation_exercise.find_element(By.CSS_SELECTOR, "[data-qa='create-account']").click()

    confirmation_message = ((automation_exercise
                             .find_element(By.CSS_SELECTOR, "h2[data-qa='account-created']>b"))
                            .text)

    assert confirmation_message == "ACCOUNT CREATED!"