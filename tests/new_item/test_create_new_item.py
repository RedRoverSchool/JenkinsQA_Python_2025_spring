from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait

new_folder_name = 'Test_Folder'
DEFAULT_TIMEOUT = 15


def wait_for(driver, by, selector, timeout=DEFAULT_TIMEOUT):
    return wait(driver, timeout).until(
        EC.visibility_of_element_located((by, selector))
    )


def test_check_create_new_item(new_item_page, jenkins_reset):
    wait_for(new_item_page, By.CSS_SELECTOR, '#name').send_keys(new_folder_name)
    wait_for(new_item_page, By.CSS_SELECTOR, '[class*="cloudbees_hudson_plugins_folder"]').click()
    wait_for(new_item_page, By.CSS_SELECTOR, '#ok-button').click()
    wait_for(new_item_page, By.CSS_SELECTOR, '[name=Submit]').click()
    wait_for(new_item_page, By.CSS_SELECTOR, "#jenkins-name-icon").click()

    assert new_item_page.find_elements(By.XPATH,
                                       f"//table[@id='projectstatus']//tbody//tr[contains(., '{new_folder_name}')]"), \
        f"Folder '{new_folder_name}' NOT FOUND"
