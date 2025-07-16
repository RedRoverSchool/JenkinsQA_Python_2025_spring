import allure

from tests.api.support.jenkins_client import JenkinsClient


class JenkinsSteps:
    def __init__(self, client: JenkinsClient):
        self.client = client

    @allure.step('POST /createItem')
    def post_create_item(self, project_name: str, config_xml: str) -> bool:
        endpoint = f"createItem?name={project_name}"
        response = self.client.post_xml(endpoint, config_xml)

        if response and response.ok:
            allure.attach(config_xml, name=f"[Created]{project_name}", attachment_type=allure.attachment_type.XML)
            return True
        else:
            msg = response.text if response else "No response"
            allure.attach(msg, name=f"[Failed]{project_name}", attachment_type=allure.attachment_type.TEXT)
            raise RuntimeError(
                f"Failed to create project '{project_name}'.\n"
                f"Endpoint: {endpoint}\n"
                f"Status: {getattr(response, 'status_code', 'N/A')}"
            )

    @allure.step("POST /job/<folder_name>/createItem")
    def post_create_item_in_folder(self, folder_name: str, project_name: str, config_xml: str) -> bool:
        endpoint = f"job/{folder_name}/createItem?name={project_name}"
        response = self.client.post_xml(endpoint, config_xml)

        if response and response.ok:
            allure.attach(config_xml, name=f"[Created]{project_name}", attachment_type=allure.attachment_type.XML)
            return True
        else:
            msg = response.text if response else "No response"
            allure.attach(msg, name=f"[Failed]{project_name}", attachment_type=allure.attachment_type.TEXT)
            raise RuntimeError(
                f"Failed to create project '{project_name}' in folder '{folder_name}'.\n"
                f"Endpoint: {endpoint}\n"
                f"Status: {getattr(response, 'status_code', 'N/A')}"
            )

    @allure.step("GET /job/{project_name}/api/json")
    def get_job_config_json(self, project_name: str, params: dict = None) -> dict:
        endpoint = f"job/{project_name}/api/json"
        query_params = {"pretty": "true", **(params or {})}
        response = self.client.get(endpoint, params=query_params)

        if response and response.ok:
            allure.attach(response.text, name="JSON data", attachment_type=allure.attachment_type.JSON)
            return response.json()

        else:
            msg = response.text if response else "No response"
            allure.attach(msg, name=f"[Failed]{project_name}", attachment_type=allure.attachment_type.TEXT)
            raise RuntimeError(
                f"Failed to get config for job '{project_name}'.\n"
                f"Endpoint: /{endpoint}\n"
                f"Params: {params}\n"
                f"Status: {response.status_code} - {response.reason}"
            )
