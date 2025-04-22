from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_new_item_page_is_accessible(main_page):
    wait = WebDriverWait(main_page, 5)

    main_page.find_element(By.LINK_TEXT, "New Item").click()
    wait.until(EC.url_to_be("http://localhost:8080/view/all/newJob"))
    title = main_page.title
    assert "new item" in title.lower()
