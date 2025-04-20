import pytest
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver

@pytest.fixture
def quotes_web(driver):
    driver.get("https://quotes.toscrape.com/")
    return driver

def test_login(quotes_web: WebDriver):
    """ тест выполняет логин и проверяет, что вход выполнен"""
    quotes_web.find_element(By.CSS_SELECTOR, "a[href='/login']").click()
    quotes_web.find_element(By.ID, "username").send_keys("Uenny")
    quotes_web.find_element(By.ID, "password").send_keys("UennyTest")
    quotes_web.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    time.sleep(1)
    logout_button = quotes_web.find_element(By.CSS_SELECTOR, "a[href='/logout']")
    assert logout_button.text == "Logout" # после логина, появилась кнопка logout


def test_find_authors_and_quotes(quotes_web: WebDriver):
    """ Тест находит все цитаты и всех авторов на сайте (должно быть 100)"""
    count_of_quotes = 0
    count_of_authors = 0
    while True:
        quotes = quotes_web.find_elements(By.CSS_SELECTOR, ".text")
        count_of_quotes += len(quotes)
        authors = quotes_web.find_elements(By.CSS_SELECTOR, ".author")
        count_of_authors += len(authors)
        time.sleep(1)
        try:
            next_button = quotes_web.find_element(By.XPATH, "//li[@class='next']/a")
            quotes_web.execute_script("arguments[0].scrollIntoView();", next_button)
            time.sleep(1)
            next_button.click()
            time.sleep(1)
        except NoSuchElementException:
            break
    assert count_of_quotes == 100, count_of_authors == 100 #проверяем, что количество всех собранных цитат и авторов 100


