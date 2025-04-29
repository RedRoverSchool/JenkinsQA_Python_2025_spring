from selenium.webdriver.common.by import By


def test_account_fullname_fields(main_page):

    test_full_name = "newadmin"

    header_account = main_page.find_element(By.XPATH, '//header//a[contains(@href, "user")]')
    header_account.click()
    account_link = main_page.find_element(By.XPATH, '//a[contains(@href, "account")]')
    account_link.click()

    full_name_field = main_page.find_element(By.XPATH, '//input[@name="_.fullName"]')
    full_name_field.clear()
    full_name_field.send_keys(test_full_name)
    main_page.find_element(By.XPATH, '//button[@name="Submit"]').click()
    account_h1_heading = main_page.find_element(By.XPATH, '//h1').text

    assert account_h1_heading == test_full_name