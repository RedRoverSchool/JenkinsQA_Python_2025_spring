from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_new_item_page_is_available(main_page):
    wait = WebDriverWait(main_page, 5)

    main_page.find_element(By.LINK_TEXT, "New Item").click()
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//li[contains(text(),'New Item')]")
        )
    )

    assert "new item" in main_page.title.lower()
