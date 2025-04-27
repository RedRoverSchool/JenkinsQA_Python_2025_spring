from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait

new_folder_name = 'Test_Folder'
DEFAULT_TIMEOUT = 15


def wait_for(driver, by, selector, timeout=DEFAULT_TIMEOUT):
    return wait(driver, timeout).until(
        EC.visibility_of_element_located((by, selector))
    )


def wait_for_clickable(driver, by, selector, timeout=DEFAULT_TIMEOUT):
    return wait(driver, timeout).until(
        EC.element_to_be_clickable((by, selector))
    )


def test_check_create_new_item(new_item_page, main_page):
    new_item_field = wait_for(new_item_page, By.CSS_SELECTOR, '#name')
    new_item_field.send_keys(new_folder_name)
    folder_option = wait_for_clickable(new_item_page, By.CSS_SELECTOR, '[class*="cloudbees_hudson_plugins_folder"]')
    folder_option.click()
    button_ok = wait_for_clickable(main_page, By.CSS_SELECTOR, '#ok-button')
    button_ok.click()
    wait_for(main_page, By.ID, "general")
    main_page.find_element(By.ID, "jenkins-home-link").click()

    assert wait_for(main_page, By.XPATH,
                    f"//table[@id='projectstatus']//a[contains(normalize-space(string()), '{new_folder_name}')]"
                    ), f"Folder '{new_folder_name}' NOT FOUND"
