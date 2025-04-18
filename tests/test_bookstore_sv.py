import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def base_url():
    url = "https://compendiumdev.co.uk/"
    return url

def test_find_published_books(driver, base_url):
    driver.get(base_url)
    section_title = driver.find_element(By.ID, "published-books").text
    assert section_title == "Published Books", "There are no published books on the main page"

@pytest.mark.parametrize('book_number', ['2', '3', '4'])
def test_open_a_book_page_for_testers(driver, base_url, book_number):
    driver.get(base_url)
    driver.find_element(By.CSS_SELECTOR, f"article > div:nth-child(3) > a:nth-child({book_number}) > img").click()
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)  # switch to the new browser's tab
    book = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "title"))
    ).text
    print(f"Book title is {book}")
    assert "Test" in book, f'It seems you have chosen a book that is not for testers.'