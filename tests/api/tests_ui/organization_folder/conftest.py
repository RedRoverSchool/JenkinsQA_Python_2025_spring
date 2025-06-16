import logging
import allure
import pytest
import requests

from tests.api.support.base_api import BaseAPI
from tests.api.tests_ui.organization_folder.data import Config, project_name, display_name, description


@allure.step("Create an Organization Folder by API")
@pytest.fixture(scope="function")
def create_organization_folder(driver):
    url = f"{BaseAPI.BASE_URL}/createItem?name={project_name}"
    config_xml = Config.get_organization_folder_xml(display_name, description)
    username = BaseAPI.USERNAME
    token, crumb_headers = BaseAPI.generate_token()
    headers = {
        "Content-Type": "application/xml",
        **crumb_headers
    }
    response = requests.post(url, data=config_xml, headers=headers, auth=(username, token))
