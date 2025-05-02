from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_new_item_page_accessibility(main_page):
    # Click on the "New Item" link
    main_page.find_element(By.LINK_TEXT, "New Item").click()

    # We expect that the input field will be available
    wait = WebDriverWait(main_page, 10)
    input_field = wait.until(EC.visibility_of_element_located((By.NAME, "name")))
    print(input_field)
    print(input_field.get_attribute("outerHTML"))
    # Checking the input field
    assert input_field.is_displayed()

def test_available_project_types_displayed(main_page):
    main_page.find_element(By.LINK_TEXT, "New Item").click()
    wait = WebDriverWait(main_page, 10)

    expected_items = [
        "Freestyle project",
        "Pipeline",
        "Multi-configuration project",
        "Folder",
        "Multibranch Pipeline",
        "Organization Folder"
    ]

    for item in expected_items:
        item_label = wait.until(EC.visibility_of_element_located((By.XPATH, f"//label[contains(., '{item}')]")))
        print(item_label.text)  # Отладка
        assert item_label.is_displayed(), f"Project type '{item}' not displayed"