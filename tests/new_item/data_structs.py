from selenium.webdriver.common.by import By


class NewItem:
    url = "/view/all/newJob"
    positive_name = "TestCase_01.001.04-PositiveName"
    new_item_button_selector = (By.CSS_SELECTOR, "a[href='/view/all/newJob']")
    name_field_selector = (By.CSS_SELECTOR, "#name")
    page_name_selector = (By.XPATH, "//h1[text()='New Item']")
    common_validation_error_selector = (By.CSS_SELECTOR, ".input-message-disabled")
    ok_button_selector = (By.ID, "ok-button")

class FreestyleItem:
    freestyle_selector = (By.CSS_SELECTOR, ".hudson_model_FreeStyleProject")
    configuration_page = f"/job/{NewItem.positive_name}/configure"
    save_button_selector = (By.NAME, "Submit")
    item_page = f"/job/{NewItem.positive_name}/"
    copy_from_field_selector = (By.ID, "from")

    @classmethod
    def get_first_letter_of_project_name(cls):
        return NewItem.positive_name[0]
