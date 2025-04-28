from selenium.webdriver.common.by import By


class JenkinsSidePanel:
    MANAGE_JENKINS = (By.XPATH, "//div[@class='task '][.//span[text()='Manage Jenkins']]")


class ManageJenkinsTask:
    SYSTEM_INFORMATION = (By.XPATH, "//a[@href='systemInfo']/..")


class SystemInformationPage:
    TABS_BAR = (By.CSS_SELECTOR, '.tabBar')
