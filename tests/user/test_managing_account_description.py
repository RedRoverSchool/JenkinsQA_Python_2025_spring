from selenium.webdriver.common.by import By


def test_profile_details_accessibility(main_page):
    header_account = main_page.find_element(By.XPATH, '//a[@href="/user/assol"]')
    header_account.click()
    account_link = main_page.find_element(By.CSS_SELECTOR, '[href="/user/assol/account"]')
    account_link.click()
    title_text = main_page.find_element(By.XPATH, '//*[@class="jenkins-form"]//h1')

    assert title_text.is_displayed(), "title account page not found"

    full_name_field = main_page.find_element(By.XPATH, '//input[@name="_.fullName"]')
    description_field = main_page.find_element(By.XPATH, '//textarea[@name="_.description"]')

    assert full_name_field.is_displayed(), "Field not clickable"
    assert description_field.is_enabled(), "Field not clickable"
