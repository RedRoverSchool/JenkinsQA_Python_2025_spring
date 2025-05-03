import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_open_homepage(driver):
    driver.get("https://www.wikipedia.org/")
    assert "Wikipedia" in driver.title


def test_element_with_text(driver):
    driver.get("https://www.wikipedia.org/")
    strong_text = driver.find_element(
        "xpath", '//strong[text()="The Free Encyclopedia"]'
    )
    time.sleep(3)
    assert strong_text.text == "The Free Encyclopedia"


def test_link_navigation(driver):
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    link = driver.find_element("link text", "Donate")
    # link = driver.find_element("xpath", '//*[@id="pt-sitesupport-2"]/a')
    link.click()
    time.sleep(3)
    print(driver.current_url)
    assert "don" in driver.current_url


def test_wikipedia_search(driver):
    driver.get("https://www.wikipedia.org/")
    search_input = driver.find_element("id", "searchInput")
    search_input.send_keys("Python for Happy Coders")
    time.sleep(3)
    search_input.submit()
    assert "Python" in driver.title
