import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

def wait_until_visible(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

def wait_until_visible_all_elements(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_all_elements_located(locator))

def test_verify_unsuccessful_login(driver):
    driver.get("http://localhost:8080")
    driver.maximize_window()

    wait_until_visible(driver, (By.ID, "j_username")).send_keys("1234")
    wait_until_visible(driver, (By.ID, "j_password")).send_keys("1234")
    wait_until_visible(driver,(By.CSS_SELECTOR, "[name='Submit']")).click()

    actual_text = wait_until_visible(driver, (By.CSS_SELECTOR, ".app-sign-in-register__error")).text
    expected_text = "Invalid username or password"

    assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"

def test_verify_dropdown_menu(driver):
    driver.get("http://localhost:8080")
    driver.maximize_window()

    driver.find_element(By.NAME, "j_username").send_keys("admin")
    driver.find_element(By.NAME, "j_password").send_keys("admin")
    driver.find_element(By.NAME, "Submit").click()

    actions = ActionChains(driver)

    expected_menu = [
        "New Item",
        "Build History",
        "Manage Jenkins",
        "My Views"
    ]

    # Hover and click the dropdown menu
    dashboard_link = driver.find_element(By.XPATH, "//a[text()='Dashboard']")
    dropdown_menu = driver.find_element(By.CSS_SELECTOR, "#breadcrumbBar .jenkins-menu-dropdown-chevron")
    actions.move_to_element(dashboard_link).move_to_element(dropdown_menu).click().perform()

    # Wait for and collect dropdown menu items
    menu_elements = wait_until_visible_all_elements(driver, (By.CSS_SELECTOR, "a.jenkins-dropdown__item"))

    actual_menu = [item.text.strip() for item in menu_elements]

    assert actual_menu == expected_menu, f"Expected {expected_menu}, but got {actual_menu}"

