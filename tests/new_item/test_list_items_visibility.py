from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_list_items_visibility(main_page):
    wait = WebDriverWait(main_page, timeout=5)
    list_expected=["Freestyle project", "Pipeline", "Multi-configuration project", "Folder", "Multibranch Pipeline", "Organization Folder"]

    main_page.find_element(By.LINK_TEXT, "New Item").click()
    actual_elements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".label")))
    actual_list = [element.text for element in actual_elements]

    assert list_expected == actual_list, f"Expected: {list_expected}, but got: {actual_list}"
