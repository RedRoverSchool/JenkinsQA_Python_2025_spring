from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_description_preview(main_page, create_folder):
    wait = WebDriverWait(main_page, 10)
    item_name = "Folder one"
    item_description = "This is a sanity test"
    create_folder(item_name)
    wait.until(EC.visibility_of_element_located((By.ID, "general")))
    main_page.find_element(By.CSS_SELECTOR, "div.setting-main> textarea").send_keys(item_description)
    main_page.find_element(By.CLASS_NAME, "textarea-show-preview").click()
    tested_description = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "textarea-preview"))).text
    main_page.find_element(By.CLASS_NAME, "textarea-hide-preview").click()
    style = main_page.find_element(By.CLASS_NAME, "textarea-preview").get_attribute("style")

    assert tested_description == item_description, "Preview doesn't work"
    assert "display: none" in style, "Preview still visible"
