from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SecurityPage(BasePage):
    class Locator:
        TOKEN_LIST = (By.CLASS_NAME, "token-list")
        YES_REVOKE_TOKEN_BUTTON = (By.CSS_SELECTOR, "button[data-id='ok']")
        ADD_NEW_TOKEN_BUTTON = (By.CSS_SELECTOR, "button.repeatable-add")
        TOKEN_NAME = (By.CSS_SELECTOR, "input[placeholder='Default name']")
        GENERATE_BUTTON = (By.ID, "api-token-property-token-save")
        COPY_TOKEN_BUTTON = (By.CSS_SELECTOR, "button[title='Copy this token'")
        SAVE_BUTTON = (By.NAME, "Submit")


    def __init__(self, driver, username,  timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/user/{username}/security/"

    def get_existing_token_list(self):
        self.wait_to_be_visible(self.Locator.TOKEN_LIST)
        return self.find_elements(By.CSS_SELECTOR, ".token-list-existing-item > input[name='tokenName']")

    def revoke_project_tokens(self, project_name, existing_token_list):
        token_names = [token.get_attribute('value') for token in existing_token_list]
        if any(project_name in name for name in token_names):
            revoke_selector = (By.CSS_SELECTOR,
                               f'input[value="{project_name}"]~span.to-right>a[data-target-url*="/revoke"]')
            revoke_links = self.wait_to_be_visible_all(revoke_selector)
            for link in revoke_links:
                self.wait_to_be_clickable(link).click()
                self.wait_to_be_clickable(self.Locator.YES_REVOKE_TOKEN_BUTTON).click()

    def generate_project_token(self, project_name):
        self.wait_to_be_clickable(self.Locator.ADD_NEW_TOKEN_BUTTON).click()
        self.wait_to_be_visible(self.Locator.TOKEN_NAME).send_keys(project_name)
        self.wait_to_be_clickable(self.Locator.GENERATE_BUTTON).click()
        return self.wait_to_be_clickable(self.Locator.COPY_TOKEN_BUTTON).get_attribute("text")

    def save_token(self, user_name):
        from pages.user_page import UserPage
        self.wait_to_be_clickable(self.Locator.SAVE_BUTTON).click()
        return UserPage(self.driver, user_name).wait_for_url()
