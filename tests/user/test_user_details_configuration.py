from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_account_fullname_field(main_page):

    test_full_name = "newadmin"

    main_page.find_element(By.XPATH, '//header//a[contains(@href, "user")]').click()
    main_page.find_element(By.XPATH, '//a[contains(@href, "account")]').click()
    full_name_field = main_page.find_element(By.XPATH, '//input[@name="_.fullName"]')
    full_name_field.clear()
    full_name_field.send_keys(test_full_name)
    main_page.find_element(By.XPATH, '//button[@name="Submit"]').click()
    account_h1_heading = main_page.find_element(By.XPATH, '//h1').text

    assert account_h1_heading == test_full_name

def test_account_description_field(main_page):

    test_description_name = "test description"

    main_page.find_element(By.XPATH, '//header//a[contains(@href, "user")]').click()
    main_page.find_element(By.XPATH, '//a[contains(@href, "account")]').click()
    description_field = main_page.find_element(By.XPATH, '//textarea[@name="_.description"]')
    description_field.clear()
    description_field.send_keys(test_description_name)
    main_page.find_element(By.XPATH, '//button[@name="Submit"]').click()

    assert main_page.find_element(By.ID, "description").text == test_description_name

def test_account_description_field_value(main_page):
    wait = WebDriverWait(main_page, 5)
    test_description_name = "test description"

    main_page.find_element(By.XPATH, '//header//a[contains(@href, "user")]').click()
    main_page.find_element(By.XPATH, '//a[contains(@href, "account")]').click()
    description_field = main_page.find_element(By.XPATH, '//textarea[@name="_.description"]')
    description_field.clear()
    description_field.send_keys(test_description_name)
    main_page.find_element(By.XPATH, '//button[@name="Submit"]').click()
    account_link = wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "account")]')))
    account_link.click()
    description_field = main_page.find_element(By.XPATH, '//textarea[@name="_.description"]')
    description_field_value = description_field.get_attribute("value")

    assert description_field_value == test_description_name