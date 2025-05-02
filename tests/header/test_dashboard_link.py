from selenium.webdriver.common.by import By


def test_dashboard_link(main_page):
    main_page.find_element(By.XPATH, "//a[@href='/manage']").click()
    main_page.find_element(By.XPATH, "//dd[text()='Configure global settings and paths.']").click()
    main_page.find_element(By.XPATH, "//li/a[@class='model-link']").click()

    assert main_page.current_url == "http://localhost:8080/"