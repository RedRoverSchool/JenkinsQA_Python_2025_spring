import logging
from typing import Dict, Any

import allure
import pytest
import requests

from tests.api.support.base_api import BaseAPI
from tests.api.tests_ui.freestyle.data import Data, Config
from tests.api.utils.helpers import create_unique_word_name

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


@allure.step("Create a new empty/not configured freestyle project via Jenkins API.")
@pytest.fixture(scope="function")
def create_empty_job_with_api() -> Dict[str, Any]:
    name = create_unique_word_name(prefix="api-freestyle")
    url = f"{BaseAPI.BASE_URL}/createItem?name={name}"
    params = {"name": name}
    token, crumb_headers = BaseAPI.generate_token()
    headers = {"Content-Type": "application/xml", **crumb_headers}
    user = BaseAPI.USERNAME

    response = requests.post(
        url,
        params=params,
        auth=(user, token),
        headers=headers,
        data=Config.get_empty_job_xml()
    )

    if response.status_code not in [200, 201]:
        pytest.fail(f"Precondition failed. Failed to create an empty job: {response.status_code} - {response.text}")

    return {
        "job_name": name,
        "job_url": url,
        "token": token,
        "crumb_headers": crumb_headers
    }


@pytest.fixture(scope="function")
def create_freestyle_scheduled_project_by_xml_via_api(jenkins_steps, main_page):
    project_name, timer, timeout, config_xml = Data.get_freestyle_scheduled_every_minute_data()
    jenkins_steps.post_create_item(project_name, config_xml)
    main_page.driver.refresh()
    main_page.go_to_freestyle_project_page(project_name).wait_for_build_execution(timeout)
    json_data = jenkins_steps.get_job_config_json(project_name)
    return project_name, json_data
