from selenium.webdriver.common.by import By


class Authorization:
    def __init__(self, driver):
        self.driver = driver

    def open_authorization_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_standard_user_login(self, username="standard_user"):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def enter_locked_out_user_login(self, username="locked_out_user"):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def enter_problem_user_login(self, username="problem_user"):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def enter_performance_glitch_user_login(self, username="performance_glitch_user"):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def enter_error_user_login(self, username="error_user"):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def enter_visual_user_login(self, username="visual_user"):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def enter_password_for_authorization(self, password="secret_sauce"):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_to_login(self):
        self.driver.find_element(By.ID, "login-button").click()

    def check_title_is_locked_out_user_login(self, title):
        value = self.driver.find_element(
            By.XPATH,
            "//h3[text() = 'Epic sadface: Sorry, this user has been locked out.']",
        )
        assert value.text == title
