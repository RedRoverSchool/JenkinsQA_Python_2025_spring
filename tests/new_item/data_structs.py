from selenium.webdriver.common.by import By


class NewItem:
    url = "/view/all/newJob"
    positive_name = "TestCase_01.001.04-PositiveName"
    new_item_button_selector = (By.CSS_SELECTOR, "a[href='/view/all/newJob']")
    name_field_selector = (By.CSS_SELECTOR, "#name")
    page_name_selector = (By.XPATH, "//h1[text()='New Item']")
    common_validation_error_selector = (By.CSS_SELECTOR, ".input-message-disabled")
