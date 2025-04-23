from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_displayed_empty_field_error(main_page):
    wait = WebDriverWait(main_page, 5)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='newJob']"))).click()
    main_page.find_element(By.ID, "ok-button").click()
    assert wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@id='itemname-required' and contains(text(), 'This field cannot be empty')]"))), \
        "message invalid field not found"


