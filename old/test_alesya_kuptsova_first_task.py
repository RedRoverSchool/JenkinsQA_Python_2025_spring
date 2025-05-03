from selenium import webdriver
from selenium.webdriver.common.by import By


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=profile")
    driver = webdriver.Chrome(options)
    return driver


url = "https://www.saucedemo.com/"
username_correct = "problem_user"
password_correct = "secret_sauce"


def test_log_in_with_correct_data():
    with setup_driver() as page_login:
        # 1. Open https://www.saucedemo.com/ site
        page_login.get(url)
        # 2. Enter "problem_user" in "Username" field
        page_login.find_element(By.ID, "user-name").send_keys(username_correct)
        # 3. Enter "pecret_sauce" in "Password" field
        page_login.find_element(By.ID, "password").send_keys(password_correct)
        # 4. Click "Login" button
        page_login.find_element(By.NAME, "login-button").click()

        # Expected result:User can see a "...inventory.html" website page, 'Swag Labs' logo and burger menu button.
        assert page_login.current_url == "https://www.saucedemo.com/inventory.html", (
            "wrong url"
        )
        assert page_login.find_element(By.CLASS_NAME, "app_logo").text == "Swag Labs"
        assert (
            page_login.find_element(By.ID, "react-burger-menu-btn").tag_name == "button"
        )


def test_log_in_with_unfilled_fields():
    with setup_driver() as page_login:
        # 1. Open https://www.saucedemo.com/ site
        page_login.get(url)
        # 2. Click "Login" button
        page_login.find_element(By.NAME, "login-button").click()

        error_message = page_login.find_element(By.XPATH, "//h3[@data-test='error']")
        # Expected result:User can see a message:'Epic sadface: Username is required'. User stays on login page.
        assert error_message.text == "Epic sadface: Username is required"
        assert page_login.current_url == url, "wrong url"


def test_log_in_with_unfilled_username_field():
    with setup_driver() as page_login:
        # 1. Open https://www.saucedemo.com/ site
        page_login.get(url)
        # 2. Enter "problem_user" in "Password" field
        page_login.find_element(By.ID, "password").send_keys(password_correct)
        # 3. Click "Login" button
        page_login.find_element(By.NAME, "login-button").click()

        error_message = page_login.find_element(By.XPATH, "//h3[@data-test='error']")
        # Expected result:User can see a message:'Epic sadface: Password is required'. User stays on login page.
        assert error_message.text == "Epic sadface: Username is required"
        assert page_login.current_url == url, "wrong url"


def test_log_in_with_unfilled_password_field():
    with setup_driver() as page_login:
        # 1. Open https://www.saucedemo.com/ site
        page_login.get(url)
        # 2. Enter "problem_user" in "Username" field
        page_login.find_element(By.ID, "user-name").send_keys(username_correct)
        # 3. Click "Login" button
        page_login.find_element(By.NAME, "login-button").click()

        error_message = page_login.find_element(By.XPATH, "//h3[@data-test='error']")
        # Expected result:User can see a message:'Epic sadface: Password is required'. User stays on login page.
        assert error_message.text == "Epic sadface: Password is required"
        assert page_login.current_url == url, "wrong url"


def test_log_in_with_incorrect_data():
    with setup_driver() as page_login:
        # 1. Open https://www.saucedemo.com/ site
        page_login.get(url)
        # 2. Enter "username" in "Username" field
        page_login.find_element(By.ID, "user-name").send_keys("username")
        # 3. Enter "password" in "Password" field
        page_login.find_element(By.ID, "password").send_keys("password")
        # 4. Click "Login" button
        page_login.find_element(By.NAME, "login-button").click()

        error_message = page_login.find_element(By.XPATH, "//h3[@data-test='error']")
        # Expected result:User can see a message:'Epic sadface: Username and password do not match any user in this service'. User stays on login page.
        assert (
            error_message.text
            == "Epic sadface: Username and password do not match any user in this service"
        )
        assert page_login.current_url == url, "wrong url"
