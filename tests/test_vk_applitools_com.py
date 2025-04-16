import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def chrome_options():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920x1080")
    return options


@pytest.fixture(scope="module")
def browser(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://demo.applitools.com/index.html")
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def authorized(browser):
    browser.find_element(By.ID, "username").send_keys("user")
    browser.find_element(By.ID, "password").send_keys("pass")
    browser.find_element(By.CSS_SELECTOR, "#log-in").click()
    return browser


def test_title(browser):
    actual_title = browser.title
    expected_title = "ACME Demo App by Applitools"
    assert actual_title == expected_title, f"wrong title. expected '{expected_title}'"


class TestLogin:
    def test_url(self, authorized):
        actual_url = authorized.current_url
        expected_url = "https://demo.applitools.com/app.html"
        assert actual_url == expected_url, f"wrong url. expected '{expected_url}'"

    def test_balance_value(self, authorized):
        actual_text = authorized.find_element(
            By.XPATH, "//div[@class='balance-value danger']"
        ).text
        expected_text = "$180"
        assert actual_text == expected_text, f"wrong text. expected '{expected_text}'"
