import time
import os
import pytest
from pages.dashboard_page import DashboardPage
from pages.newfolder_page import NewItemPage
from pages.folderconfig_page import FolderConfigPage
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path)

@pytest.mark.usefixtures("driver")
class TestCreateFolder:
    def test_create_folder_from_dashboard(self, driver, login_page, main_page):
        folder_name = f"TestFolder_{int(time.time())}"

        dashboard_page = DashboardPage(driver)
        new_item_page = NewItemPage(driver)
        folder_config_page = FolderConfigPage(driver)

        assert driver.title == "Sign in [Jenkins]" or driver.title == "Dashboard [Jenkins]"

        dashboard_page.click_new_item()
        new_item_page.create_folder(folder_name)
        folder_config_page.save_and_verify(folder_name)
        dashboard_page.go_to_dashboard()
        dashboard_page.verify_folder_exists(folder_name)
