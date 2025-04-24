from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait

new_folder_name = 'Test_Folder'
DEFAULT_TIMEOUT = 25


def wait_for(driver, by, selector, timeout=DEFAULT_TIMEOUT):
    return wait(driver, timeout).until(
        EC.visibility_of_element_located((by, selector))
    )


def wait_for_clickable(driver, by, selector, timeout=DEFAULT_TIMEOUT):
    return wait(driver, timeout).until(
        EC.element_to_be_clickable((by, selector))
    )


def test_check_create_new_item(main_page):
    new_item_button = wait_for(main_page, By.CSS_SELECTOR, "a[href='/view/all/newJob']")
    new_item_button.click()
    wait_for(main_page, By.CSS_SELECTOR, '#name').send_keys(new_folder_name)
    wait_for_clickable(main_page, By.CSS_SELECTOR, '[class*="cloudbees_hudson_plugins_folder"]').click()
    wait_for_clickable(main_page, By.CSS_SELECTOR, '#ok-button').click()
    wait_for_clickable(main_page, By.CSS_SELECTOR, '[name=Submit]').click()
    jenkins_icon = wait_for_clickable(main_page, By.CSS_SELECTOR, "#jenkins-home-link")
    jenkins_icon.click()

    # assert wait_for(main_page, By.XPATH,f"//table[@id='projectstatus']/tbody/tr[contains(., '{new_folder_name}')]"), \
    #     f"Folder '{new_folder_name}' NOT FOUND"
