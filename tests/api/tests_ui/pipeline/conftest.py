import logging
import time

import allure
import pytest
import requests

from tests.api.support.base_api import BaseAPI
from tests.api.tests_ui.pipeline.data import Data, BuildsCounter

logger = logging.getLogger(__name__)


@allure.step("Create a new Pipeline project with a script as attached.")
@pytest.fixture(scope="function")
def create_pipeline_project_scripted_keep_70_by_api():
    token, crumb_headers = BaseAPI.generate_token()
    project_name, log_rotator, script, config_xml = Data.get_pipeline_scripted_keep_70_data(token)
    create_item_url = f"{BaseAPI.BASE_URL}/createItem?name={project_name}"
    user = BaseAPI.USERNAME
    headers = {"Content-Type": "application/xml", **crumb_headers}

    logger.info(f"Creating Pipeline project '{project_name}' with {log_rotator} builds to keep via API POST request.")
    with allure.step(f"Sending POST to create item: {project_name} with script and config.xml as attached."):
        response = requests.post(
            create_item_url,
            auth=(user, token),
            headers=headers,
            data=config_xml
        )
        allure.attach(script, name="Pipeline script", attachment_type=allure.attachment_type.TEXT)
        allure.attach(config_xml, name="Config XML", attachment_type=allure.attachment_type.XML)

        if response.status_code not in [200, 201]:
            logger.error(f"Failed to create job: {response.status_code} - {response.text}")
            raise Exception(f"Failed to create job: {response.status_code}, {response.text}")
        else:
            logger.info(f"Pipeline project '{project_name}' created successfully.")

    return project_name, user, token


@allure.step("Trigger 31 builds remotely.")
@pytest.fixture
def trigger_builds_31(create_pipeline_project_scripted_keep_70_by_api):
    job_name, user, token = create_pipeline_project_scripted_keep_70_by_api
    job_name_encoded = job_name.replace(" ", "%20")
    builds_to_trigger = BuildsCounter.builds_history_limit_31
    job_url = f"{BaseAPI.BASE_URL}/job/{job_name_encoded}"
    job_info_url = f"{job_url}/api/json"
    build_delay_0_url = f"{job_url}/build?delay=0sec"
    auth = (user, token)
    timeout_short = 60
    timeout_long = 120

    for i in range(builds_to_trigger):
        job_info_resp = requests.get(job_info_url, auth=auth)
        next_build_number = job_info_resp.json()["nextBuildNumber"]
        build_info_url = f"{job_url}/{next_build_number}/api/json"
        build_info_resp = ""

        requests.post(build_delay_0_url, auth=auth)

        for _ in range(timeout_short):
            build_info_resp = requests.get(build_info_url, auth=auth)
            if build_info_resp.status_code == 200:
                break
            time.sleep(1)
        else:
            logger.warning(f"Build #{next_build_number} did not start in time")

        for _ in range(timeout_long):
            build_info = build_info_resp.json()
            if not build_info.get("building", True):
                logger.info(f"Build #{next_build_number} finished.")
                break
            time.sleep(1)
            build_info_resp = requests.get(build_info_url, auth=auth)
        else:
            logger.warning(f"Build #{next_build_number} did not finish in time")

    return job_name