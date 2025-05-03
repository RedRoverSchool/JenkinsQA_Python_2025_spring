from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_required_itemname_field_validation(main_page):
    wait = WebDriverWait(main_page, 5)

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//a[@href='newJob']"))
    ).click()
    main_page.find_element(By.ID, "ok-button").click()
    error_element = wait.until(
        EC.visibility_of_element_located((By.ID, "itemname-required"))
    )
    actual_error_text = error_element.text.strip()
    expected_error_text = "» This field cannot be empty, please enter a valid name"
    assert actual_error_text == expected_error_text, (
        f"Expected error message '{expected_error_text}', but got '{actual_error_text}'"
    )
