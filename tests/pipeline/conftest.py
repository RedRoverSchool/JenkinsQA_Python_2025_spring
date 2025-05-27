import time
import pytest
import requests

from conftest import logger
from core.jenkins_utils import generate_token
from pages.pipeline_page import PipelinePage
from pages.pipeline_config_page import PipelineConfigPage

from tests.pipeline.pipeline_data import pipeline_project_name, Script, Config, BuildCounter


@pytest.fixture(scope="function")
def pipeline_config_page(new_item_page) -> PipelineConfigPage:
    return new_item_page.create_new_pipeline_project(pipeline_project_name)


@pytest.fixture(scope="function")
def create_pipeline_with_script(pipeline_config_page) -> PipelinePage:
    return pipeline_config_page.type_script(Script.script).click_save_button(pipeline_project_name)


@pytest.fixture(scope="function")
def create_builds(create_pipeline_with_script):
    pipeline_page = create_pipeline_with_script

    def _create_builds_per_amount(total: int, start: int = 1, amount_to_wait: int = 5) -> PipelinePage:
        for i in range(start, start + total):
            pipeline_page.click_build_now_button()

            build_index = i - start + 1
            if build_index % amount_to_wait == 0 or i == total:
                pipeline_page.wait_for_build_execution(i)

        return pipeline_page

    return _create_builds_per_amount


@pytest.fixture(scope="function")
def jenkins_auth(driver, config):
    username = config.jenkins.USERNAME
    api_token = generate_token(config, driver, Config.job_name)
    return username, api_token


@pytest.fixture(scope="function")
def create_pipeline_job_by_api(config, driver, jenkins_auth):
    username, token = jenkins_auth
    job_name = Config.job_name
    config_xml = Config.get_config_xml(token)
    headers = {"Content-Type": "application/xml"}

    response = requests.post(
        f"{config.jenkins.base_url}/createItem?name={job_name}",
        data=config_xml,
        headers=headers,
        auth= (username, token)
    )
    if response.status_code not in [200, 201]:
        raise Exception(f"Failed to create job: {response.status_code}, {response.text}")

    return job_name, username, token


@pytest.fixture
def trigger_builds(create_pipeline_job_by_api, driver, config, main_page) -> PipelinePage:
    job_name, username, token = create_pipeline_job_by_api
    base_url = config.jenkins.base_url

    pipeline_page = main_page.go_to_pipeline_page(job_name)

    for i in range(BuildCounter.build_history_limit_31):
        next_build_resp = requests.get(
            f"{base_url}/job/{job_name}/api/json",
            auth=(username, token)
        )
        next_build_number = next_build_resp.json()["nextBuildNumber"]

        # remote_build_trigger(driver, job_name, token, config)
        job_name_encoded = job_name.replace(" ", "%20")
        url = f"{base_url}/job/{job_name_encoded}/build?delay=0sec"

        requests.post(url, auth=(username, token))
        logger.info(f"Triggered build #{next_build_number}")
        build_info_resp = ""

        for _ in range(60):
            build_info_resp = requests.get(
                f"{base_url}/job/{job_name}/{next_build_number}/api/json",
                auth=(username, token)
            )
            if build_info_resp.status_code == 200:
                logger.info(f"Build #{next_build_number} started...")
                break
            time.sleep(1)
        else:
            logger.warning(f"Build #{next_build_number} did not start in time")

        for _ in range(120):
            build_info = build_info_resp.json()
            if not build_info.get("building", True):
                logger.info(f"Build #{next_build_number} finished.")
                break
            time.sleep(1)
            build_info_resp = requests.get(
                f"{base_url}/job/{job_name}/{next_build_number}/api/json",
                auth=(username, token)
            )
        else:
            logger.warning(f"Build #{next_build_number} did not finish in time")

        driver.refresh()

    return pipeline_page
