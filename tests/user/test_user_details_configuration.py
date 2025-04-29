from selenium.webdriver.common.by import By


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