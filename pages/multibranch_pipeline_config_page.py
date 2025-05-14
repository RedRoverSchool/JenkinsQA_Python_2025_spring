from pages.base_page import BasePage

from tests.multibranch_pipeline_configuration.mbp_data import Toggle


class MultibranchPipelineConfigPage(BasePage):
    def __init__(self, driver, job_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{job_name}/configure"

    def get_state_of_the_toggle(self):
        return self.find_element(*Toggle.TOGGLE).text
