from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_not_accept_special_characters(main_page):
    wait = WebDriverWait(main_page, timeout=5)
    expected_error_text = '» ‘!’ is an unsafe character'
    main_page.find_element(By.LINK_TEXT, "New Item").click()
    wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("!")
    error_text = wait.until(EC.visibility_of_element_located((By.ID, "itemname-invalid"))).text
    assert error_text == expected_error_text
