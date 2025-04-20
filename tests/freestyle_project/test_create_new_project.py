from selenium.webdriver.common.by import By


def test_new_freestyle_project(jenkins_reset, freestyle, main_page):

    assert main_page.find_element(By.CSS_SELECTOR, 'h1').text == "Configure"
