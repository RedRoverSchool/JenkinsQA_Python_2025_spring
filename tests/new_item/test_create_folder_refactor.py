import os
import time
from dotenv import load_dotenv
from pages.main_page import MainPage

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path)

jenkins_username = os.getenv("JENKINS_USERNAME")
jenkins_password = os.getenv("JENKINS_PASSWORD")

assert jenkins_username, "JENKINS_USERNAME не задан в .env"
assert jenkins_password, "JENKINS_PASSWORD не задан в .env"

def test_create_folder_from_dashboard(driver):
    from pages.login_page import LoginPage

    folder_name = f"TestFolder_{int(time.time())}"

    driver.get("http://localhost:8080")

    login_page = LoginPage(driver)
    main_page = login_page.login(jenkins_username, jenkins_password)

    new_item_page = main_page.go_to_new_item_page()
    folder_config_page = new_item_page.create_new_folder(folder_name)
    folder_config_page.click_on(folder_config_page.Locators.SUBMIT_BTN)

    folder_config_page.wait_for_url()

    driver.get(main_page.base_url)
    main_page = MainPage(driver)
    main_page.wait_for_url()

    assert main_page.is_job_with_name_displayed(folder_name, timeout=10), \
        f"Папка '{folder_name}' не отображается на дашборде"

    main_page.click_on_folder_by_name(folder_name)

    assert main_page.is_header_contains(folder_name), \
        f"Имя папки '{folder_name}' не отображается в заголовке страницы"