from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_create_folder_with_description_only(main_page, create_folder):
    wait = WebDriverWait(main_page, 10)
    item_name = "Folder one"
    item_description = "This is a sanity test"
    create_folder(item_name)
    wait.until(EC.visibility_of_element_located((By.ID, "general")))
    main_page.find_element(By.CSS_SELECTOR, "div.setting-main> textarea").send_keys(item_description)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='Submit']"))).click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "h4")))
    check_display_name_element = main_page.find_element(By.XPATH, "//*[@id='main-panel']/h1")
    check_display_name = check_display_name_element.text
    check_description_element = main_page.find_element(By.XPATH, "//*[@id='view-message']")
    check_description = check_description_element.text

    assert check_display_name == item_name, "Folder name is incorrect"
    assert check_description == item_description, "Description is incorrect"


def test_create_folder_with_display_and_description(main_page, create_folder):
    wait = WebDriverWait(main_page, 10)
    initial_values =["Displayed name", "Folder one", "This is a sanity test"]
    tested_values = []
    create_folder(initial_values[0])
    wait.until(EC.visibility_of_element_located((By.ID, "general")))
    main_page.find_element(By.CSS_SELECTOR, "div.setting-main> input").send_keys(initial_values[1])
    main_page.find_element(By.CSS_SELECTOR, "div.setting-main> textarea").send_keys(initial_values[2])
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='Submit']"))).click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "h4")))
    main_panel_text = main_page.find_element(By.ID, "main-panel").text
    for line in main_panel_text.splitlines():
        if line.strip().startswith("Folder name:"):
            tested_values.append(line.split(":")[1].strip())
    tested_values.append(main_page.find_element(By.XPATH, "//*[@id='main-panel']/h1").text)
    tested_values.append(main_page.find_element(By.XPATH, "//*[@id='view-message']").text)

    for i in range(len(initial_values)):
        assert tested_values[i] == initial_values[i], f"Do not match {initial_values[i]}"