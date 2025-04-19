from selenium.webdriver.common.by import By


def test_new_freestyle_project(freestyle, main_page, jenkins_reset):

    assert main_page.find_element(By.CSS_SELECTOR, 'h1').text == "Configure"
