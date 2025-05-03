from selenium.webdriver.common.by import By


class AddUserLocators:
    LOCATOR_ADDUSER_HEADER = (By.XPATH, "/form/h1")
    LOCATOR_ADDUSER_USERNAME_FIELD = (By.CLASS_NAME, "username")
    LOCATOR_ADDUSER_PASSWORD1_FIELD = (By.CLASS_NAME, "password1")
    LOCATOR_ADDUSER_PASSWORD2_FIELD = (By.CLASS_NAME, "password2")
    LOCATOR_ADDUSER_FULLNAME_FIELD = (By.CLASS_NAME, "fullname")
    LOCATOR_ADDUSER_EMAIL_FIELD = (By.CLASS_NAME, "email")
    LOCATOR_ADDUSER_CREATE_BUTTON = (By.CLASS_NAME, "Submit")


def enter_text(self, target_field, input_text):
    input_field = self.find_element(target_field)
    input_field.click()
    input_field.send_keys(input_text)
    return input_field


def click_on_the_create_button(self):
    return self.find_element(
        AddUserLocators.LOCATOR_ADDUSER_CREATE_BUTTON).click()


def get_validation_message():
    print("tbd")
