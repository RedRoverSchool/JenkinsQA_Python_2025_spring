from pages.manage_jenkins.manage_jenkins_page import ManageJenkinsPage


class LoadStatisticsPage(ManageJenkinsPage):

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/manage/load-statistics"
