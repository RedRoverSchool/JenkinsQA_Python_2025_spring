import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def textbox_page(driver):
    page = ElementsTextBoxPage(driver)
    page.open()
    return page


TEST_USER = {
    'full_name': 'John Doe',
    'valid_email': 'valid_email@mail.com',
    'current_address': '123 Main St, New York, NY 10001, USA',
    'permanent_address': '456 Fountain Ave, San Francisco, CA 94102, USA'
}

INVALID_EMAIL = [
    'space @mail.com',
    'missed_atmail.com',
    'missed_dot@mailcom'
]


class BasePage:
    """Base class with common values and methods for all pages"""
    BASE_URL = 'https://demoqa.com'
    TIMEOUT = 5

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, self.TIMEOUT)

    def open(self):
        self.driver.get(self.url)

    def send_keys(self, locator: tuple[str, str], text: str):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def click(self, locator: tuple[str, str]):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def is_displayed(self, locator: tuple[str, str]):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_not_displayed(self, locator: tuple[str, str]):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


class ElementsTextBoxPage(BasePage):
    """Class with specific values and methods for Elements -> TextBox page"""
    URL = f'{BasePage.BASE_URL}/text-box'
    FULL_NAME_FIELD = (By.ID, 'userName')
    EMAIL_FIELD = (By.XPATH, "//input[@class='mr-sm-2 form-control']")
    WRONG_EMAIL_FIELD = (By.XPATH, "//input[@class='mr-sm-2 field-error form-control']")
    CURRENT_ADDRESS_FIELD = (By.ID, 'currentAddress')
    PERMANENT_ADDRESS_FIELD = (By.ID, 'permanentAddress')
    SUBMIT_BUTTON = (By.ID, 'submit')
    SUBMITTED_FULL_NAME = (By.ID, 'name')
    SUBMITTED_EMAIL = (By.ID, 'email')
    SUBMITTED_CURRENT_ADDRESS = (By.XPATH, "//div[@id='output']//p[@id='currentAddress']")
    SUBMITTED_PERMANENT_ADDRESS = (By.XPATH, "//div[@id='output']//p[@id='permanentAddress']")

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)

    def submitted_element_text(self, locator: tuple[str, str]) -> str:
        return self.driver.find_element(*locator).text.split(':')[1]


class TestElementsTextBoxPage:
    """Tests for Elements -> TextBox page only - https://demoqa.com/text-box"""
    def test_submit_all_correct_fields(self, driver: webdriver.Chrome, textbox_page: ElementsTextBoxPage):
        """Open https://demoqa.com/text-box and fill all fields with random correct data.
           Check that after click on "Submit" button correct data appears in output field."""
        page = textbox_page
        page.send_keys(page.FULL_NAME_FIELD, TEST_USER.get('full_name'))
        page.send_keys(page.EMAIL_FIELD, TEST_USER.get('valid_email'))
        page.send_keys(page.CURRENT_ADDRESS_FIELD, TEST_USER.get('current_address'))
        page.send_keys(page.PERMANENT_ADDRESS_FIELD, TEST_USER.get('permanent_address'))
        page.scroll_to_bottom()  # Otherwise submit button can be covered by advertising block
        page.click(page.SUBMIT_BUTTON)
        assert page.submitted_element_text(page.SUBMITTED_FULL_NAME) == TEST_USER.get('full_name')
        assert page.submitted_element_text(page.SUBMITTED_EMAIL) == TEST_USER.get('valid_email')
        assert page.submitted_element_text(page.SUBMITTED_CURRENT_ADDRESS) == TEST_USER.get('current_address')
        assert page.submitted_element_text(page.SUBMITTED_PERMANENT_ADDRESS) == TEST_USER.get('permanent_address')

    @pytest.mark.parametrize('invalid_email', INVALID_EMAIL)
    def test_submit_invalid_email(self, driver: webdriver.Chrome, textbox_page: ElementsTextBoxPage, invalid_email: str):
        """Open https://demoqa.com/text-box and fill email field with not valid email.
           Check that before click on "Submit" button email field looks normally,
           and after click this field change style as a warning about invalid email."""
        page = textbox_page
        page.send_keys(page.EMAIL_FIELD, invalid_email)
        page.scroll_to_bottom()  # Otherwise submit button can be covered by advertising block
        assert page.is_not_displayed(page.WRONG_EMAIL_FIELD)
        page.click(page.SUBMIT_BUTTON)
        assert page.is_displayed(page.WRONG_EMAIL_FIELD)
