import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def python_org(driver):
    driver.get("https://www.python.org/")
    return driver


def test_source_releases_page_title(driver, python_org):
    driver.find_element(By.ID, "downloads").click()
    driver.find_element(
        By.XPATH, "//a[@href='/downloads/source/' and contains(text(), 'Linux/UNIX')]"
    ).click()

    assert (
        driver.find_element(By.CLASS_NAME, "page-title").text
        == "Python Source Releases"
    )


def test_getting_started_h1_headers(driver, python_org):
    h1_list = [
        "",
        "Python For Beginners",
        "Installing",
        "Learning",
        "Looking for Something Specific?",
        "Frequently Asked Questions",
        "Looking to Help?",
    ]

    element = driver.find_element(By.XPATH, "//p/a[@href='/about/gettingstarted/']")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    h1_elements = [item.text for item in driver.find_elements(By.CSS_SELECTOR, "h1")]

    assert all([i1 == i2 for i1, i2 in zip(h1_list, h1_elements)]), (
        "The list of H1 headings does not match the reference list."
    )
