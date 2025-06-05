import logging
import allure
import pytest
import requests

from tests.api.support.base_api import BaseAPI
from tests.api.tests_ui.freestyle.data import Data


logger = logging.getLogger(__name__)


@allure.step("Create a new Freestyle project scheduled every minute via Jenkins API.")
@pytest.fixture(scope="function")
def create_freestyle_project_scheduled_every_minute_by_api():
    project_name, timer, timeout, config_xml = Data.get_freestyle_scheduled_every_minute_data()
    create_item_url = f"{BaseAPI.BASE_URL}/createItem?name={project_name}"
    user = BaseAPI.USERNAME
    token, crumb_headers = BaseAPI.generate_token()
    headers = {"Content-Type": "application/xml", **crumb_headers}

    logger.info(f"Creating Freestyle project '{project_name}' with schedule '{timer}' via API POST request.")
    with allure.step(f"Sending POST to create item: {project_name} with config.xml as attached."):
        response = requests.post(
            create_item_url,
            auth=(user, token),
            headers=headers,
            data=config_xml
        )
        allure.attach(config_xml, name="Config XML", attachment_type=allure.attachment_type.XML)

        if response.status_code not in [200, 201]:
            logger.error(f"Failed to create job: {response.status_code} - {response.text}")
        else:
            logger.info(f"Triggering build for the project '{project_name}' by schedule '{timer}'.")
            logger.info(f"Waiting for the build to finish (up to {timeout} sec)...")

    return project_name, timeout
