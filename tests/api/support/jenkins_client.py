import logging

import requests
from requests.auth import HTTPBasicAuth

from tests.api.support.base_api import BaseAPI

logger = logging.getLogger(__name__)


class JenkinsClient(BaseAPI):
    def __init__(self):
        super().__init__()
        self.session = requests.Session()
        self.token, self.crumb_headers = self.generate_token("api-token")
        self.session.auth = HTTPBasicAuth(self.USERNAME, self.token)

    def post_xml(self, endpoint: str, xml_data: str):
        headers = {'Content-Type': 'application/xml'}
        headers.update(self.crumb_headers)
        url = f"{self.BASE_URL}/{endpoint}"
        response = self.session.post(url, data=xml_data, headers=headers)
        logger.info(f"[POST /{endpoint}] Status: {response.status_code} - {response.reason}")

        if not response.ok:
            logger.error(f"[POST {url}] Status: {response.status_code} - {response.reason}")
            return response

        return response

    def get(self, endpoint: str, params: dict = None) -> requests.Response:
        headers = {'Content-Type': 'application/json'}
        headers.update(self.crumb_headers)
        url = f"{self.BASE_URL}/{endpoint}"
        response = self.session.get(url, headers=headers, params=params)
        logger.info(f"[GET] /{endpoint} - Status: {response.status_code} - {response.reason}")
        return response
