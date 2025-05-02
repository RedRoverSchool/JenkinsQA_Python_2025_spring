from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_signin_fields(login_page):
    wait5 = WebDriverWait(login_page, 5)
    wait5.until(EC.visibility_of_element_located((By.ID, "main-panel")))
    signin_form = login_page.find_element(By.XPATH, "//main//h1")
    username_field = login_page.find_element(By.ID, "j_username")
    password_field = login_page.find_element(By.ID, "j_password")
    keep_me_signed_checkbox = login_page.find_element(By.XPATH, "//input[@type='checkbox']")

    assert signin_form.text == "Sign in to Jenkins"
    assert username_field.is_displayed(), "Username field is not displayed"
    assert password_field.is_displayed(), "Password field is not displayed"
    assert keep_me_signed_checkbox.is_displayed(), "Keep me signed checkbox is not displayed"
