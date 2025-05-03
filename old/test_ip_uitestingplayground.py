import pytest
from selenium.webdriver.common.by import By


@pytest.fixture
def sampleapp(driver):
    driver.get("http://uitestingplayground.com/sampleapp")
    return driver


def test_default_login_form_view(sampleapp):
    message_element = sampleapp.find_element(By.ID, "loginstatus")
    message_text = message_element.text
    message_color = message_element.value_of_css_property("color")
    user_name_placeholder_text = sampleapp.find_element(
        By.NAME, "UserName"
    ).get_attribute("placeholder")
    user_password_placeholder_text = sampleapp.find_element(
        By.NAME, "Password"
    ).get_attribute("placeholder")
    submit_button_text = sampleapp.find_element(By.CSS_SELECTOR, ".row button").text

    assert message_element.is_displayed(), "Login status message is not displayed."
    assert message_text == "User logged out."
    assert message_color == "rgba(23, 162, 184, 1)"
    assert user_name_placeholder_text == "User Name"
    assert user_password_placeholder_text == "********"
    assert submit_button_text == "Log In"


def test_success_login_message(sampleapp):
    user_name = "user"
    user_password = "pwd"

    sampleapp.find_element(By.NAME, "UserName").send_keys(user_name)
    sampleapp.find_element(By.NAME, "Password").send_keys(user_password)
    sampleapp.find_element(By.ID, "login").click()

    success_message_element = sampleapp.find_element(By.ID, "loginstatus")
    success_message_text = success_message_element.text
    success_message_color = success_message_element.value_of_css_property("color")

    assert success_message_element.is_displayed(), (
        "Login status message is not displayed."
    )
    assert success_message_text == "Welcome, user!"
    assert success_message_color == "rgba(40, 167, 69, 1)"
