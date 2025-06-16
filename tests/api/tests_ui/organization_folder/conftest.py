import logging
import allure
import pytest
import requests

from tests.api.support.base_api import BaseAPI
from tests.api.tests_ui.organization_folder.data import Config, project_name, display_name, description

logger = logging.getLogger(__name__)


@allure.step("Create a new Organization Folder via Jenkins API.")
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
    logger.info(f"Creating Organization Folder '{project_name}' via API POST request.")
    with allure.step(f"Sending POST request to create item: {project_name} with XML configuration attached."):
        response = requests.post(
            url,
            data=config_xml,
            headers=headers,
            auth=(username, token)
        )

        allure.attach(config_xml, name="Organization Folder Config XML", attachment_type=allure.attachment_type.XML)

        if response.status_code not in [200, 201]:
            logger.error(
                f"Failed to create Organization Folder. Status code: {response.status_code}, Response: {response.text}")
            response.raise_for_status()
        else:
            logger.info(f"Organization Folder '{project_name}' was created successfully.")
