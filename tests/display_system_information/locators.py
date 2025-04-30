from selenium.webdriver.common.by import By


class JenkinsSidePanel:
    MANAGE_JENKINS = (By.XPATH, "//div[@class='task '][.//span[text()='Manage Jenkins']]")


class ManageJenkinsTask:
    SYSTEM_INFORMATION = (By.XPATH, "//a[@href='systemInfo']/..")


class SystemInformationPage:
    TABS_BAR = (By.CSS_SELECTOR, '.tabBar')
    SYSTEM_PROPERTIES_TAB = (By.XPATH, "//a[@href='#'][text()='System Properties']/..")
    ENVIRONMENT_VARIABLES_TAB = (By.XPATH, "//a[@href='#'][text()='Environment Variables']/..")
    PLUGINS_TAB = (By.XPATH, "//a[@href='#'][text()='Plugins']/..")
    MEMORY_USAGE_TAB = (By.XPATH, "//a[@href='#'][text()='Memory Usage']/..")
    THREAD_DUMPS_TAB = (By.XPATH, "//a[@href='#'][text()='Thread Dumps']/..")
    SHOW_SYS_VALUES_BUTTON = (By.XPATH, "(//button[contains(normalize-space(text()), 'Show values')])[1]")
    SHOW_ENV_VALUES_BUTTON = (By.XPATH, "(//button[contains(normalize-space(text()), 'Show values')])[2]")
    HIDE_SYS_VALUES_BUTTON = (By.XPATH, "(//button[contains(normalize-space(text()), 'Hide values')])[1]")
    HIDE_ENV_VALUES_BUTTON = (By.XPATH, "(//button[contains(normalize-space(text()), 'Hide values')])[2]")
    PLUGINS_TABLE_BODY = (By.XPATH, "(//table[@class='jenkins-table sortable'])[3]/tbody")
    TIMESPAN_DROPDOWN = (By.ID, 'timespan-select')
