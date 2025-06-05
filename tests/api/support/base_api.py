from typing import Any

import allure
import logging
import requests
from requests.auth import HTTPBasicAuth

from core.settings import Config

logger = logging.getLogger(__name__)

class BaseAPI:
    config = Config.load()

    BASE_URL = config.jenkins.base_url
    USERNAME = config.jenkins.USERNAME
    PASSWORD = config.jenkins.PASSWORD
    AUTH = HTTPBasicAuth(USERNAME, PASSWORD)

    @classmethod
    @allure.step("Fetch Jenkins CSRF crumb")
    def get_crumb_headers(cls, session: requests.Session) -> dict[str, str] | None:
        crumb_url = f"{cls.BASE_URL}/crumbIssuer/api/json"

        response = session.get(crumb_url, auth=cls.AUTH)
        if not response.ok:
            logger.error(f"Failed to get CSRF crumb: {response.status_code} {response.text}")
            allure.attach(response.text, name="Crumb Error", attachment_type=allure.attachment_type.TEXT)
            return None

        crumb_data = response.json()
        crumb_headers = {crumb_data["crumbRequestField"]: crumb_data["crumb"]}
        allure.attach(str(crumb_headers), name="Jenkins CSRF crumb", attachment_type=allure.attachment_type.TEXT)

        return crumb_headers


    @classmethod
    @allure.step("Generate a new Jenkins API token for the current user.")
    def generate_token(cls, token_name="api-token") -> tuple[str, dict[str, str]] | None:
        session = requests.Session()
        crumb_headers = cls.get_crumb_headers(session)

        if not crumb_headers:
            logger.error(f"Failed to create crumb_headers.")
            return None

        url = f"{cls.BASE_URL}/user/{cls.USERNAME}/descriptorByName/jenkins.security.ApiTokenProperty/generateNewToken"
        headers = {"Content-Type": "application/json", **crumb_headers}
        auth = cls.AUTH
        data = f"newTokenName={token_name}"

        logger.info(f"Generating Jenkins API token at: \"/{url.split("/")[-1]}\"")
        with allure.step(f"POST to generate new token: {token_name}"):
            response = session.post(url=url, headers=headers, auth=auth, data=data)

        if not response.ok:
            logger.error(f"Failed to generate token. Status: {response.status_code}, Response: {response.text}")
            allure.attach(response.text, name="Token Error", attachment_type=allure.attachment_type.TEXT)
            return None

        try:
            token_value = response.json()["data"]["tokenValue"]
            logger.info(f"Generated token: {token_value[:4]}...")
            allure.attach(token_value, name="New API Token", attachment_type=allure.attachment_type.TEXT)
            return token_value, crumb_headers

        except (KeyError, ValueError) as e:
            logger.error(f"Failed to parse token response: {e}")
            return None