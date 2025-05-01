import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from tests.freestyle_project.freestyle_data import Freestyle


@pytest.fixture(scope="function")
def freestyle(main_page, config):
    wait5 = WebDriverWait(main_page, 5)
    wait5.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/view/all/newJob"]'))).click()
    wait5.until(EC.presence_of_element_located((By.ID, 'name'))).send_keys(Freestyle.project_name)
    main_page.find_elements(By.CSS_SELECTOR, '.j-item-options>li[tabindex="0"]')[0].click()
    main_page.find_element(By.ID, 'ok-button').click()
    wait5.until(EC.url_changes(config.jenkins.base_url + "/view/all/newJob"))

    return main_page

@pytest.fixture(scope="function")
def tooltip(freestyle):
    wait = WebDriverWait(freestyle, 10)
    actions = ActionChains(freestyle)
    tooltip_link = freestyle.find_element(By.XPATH, '//span[@tooltip="Enable or disable the current project"]')
    actions.move_to_element(tooltip_link).perform()
    wait.until(EC.presence_of_element_located((By.XPATH, '//span[@aria-describedby="tippy-15"]')))

    return freestyle.find_element(By.XPATH, '//div[@class="tippy-content"]').text

@pytest.fixture(scope="function")
def disabled_message(freestyle):
    wait = WebDriverWait(freestyle, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'jenkins-toggle-switch__label__checked-title')))
    freestyle.find_element(By.XPATH, '//label[@data-title="Disabled"]').click()
    freestyle.find_element(By.XPATH, '//button[@name="Submit"]').click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//form[@action="enable"]')))

    return freestyle

@pytest.fixture(scope="function")
def enable_automatically(disabled_message):
    is_warning_message_disappear = False
    is_project_enable = False
    wait = WebDriverWait(disabled_message, 10)
    wait2 = WebDriverWait(disabled_message, 2)
    disabled_message.find_element(By.XPATH, '//button[@name="Submit"]').click()
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Build Now')))
    try:
        wait2.until(EC.presence_of_element_located((By.XPATH, '//form[@action="enable"]')))
    except Exception:
        pass
        is_warning_message_disappear = True
    disabled_message.find_element(By.LINK_TEXT, 'Configure').click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//label[@class="jenkins-toggle-switch__label "]')))
    is_enable_text = disabled_message.find_element(By.XPATH, '//label[@class="jenkins-toggle-switch__label "]').text
    if is_enable_text == "Enabled":
        is_project_enable = True

    return [is_warning_message_disappear, is_project_enable]

@pytest.fixture()
def can_add_description(freestyle):
    wait = WebDriverWait(freestyle, 10)
    (wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@name="description"]')))
     .send_keys(Freestyle.description_text))
    freestyle.find_element(By.XPATH, '//button[@name="Apply"]').click()

    return freestyle.find_element(By.XPATH, '//textarea[@name="description"]').get_attribute("value")

@pytest.fixture()
def empty_configure(freestyle):
    wait = WebDriverWait(freestyle, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, '//button[@name="Submit"]'))).click()
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Build Now')))
    h1_txt = freestyle.find_element(By.CSS_SELECTOR, 'h1').text
    if h1_txt == Freestyle.project_name:
        return True
    else:
        return Freestyle

@pytest.fixture()
def description_appears(freestyle):
    wait = WebDriverWait(freestyle, 10)
    freestyle.find_element(By.XPATH, '//textarea[@name="description"]').send_keys(Freestyle.description_text)
    freestyle.find_element(By.XPATH, '//button[@name="Submit"]').click()
    wait.until(EC.presence_of_element_located((By.ID, 'description')))

    return freestyle.find_element(By.ID, 'description').text

@pytest.fixture()
def preview_hide(freestyle):
    wait = WebDriverWait(freestyle, 10)
    preview = False
    hide = False
    freestyle.find_element(By.XPATH, '//textarea[@name="description"]').send_keys(Freestyle.description_text)
    preview_webelement = freestyle.find_element(By.LINK_TEXT, 'Preview')
    if preview_webelement.is_enabled():
        preview = True
    preview_webelement.click()
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Hide preview')))
    hide_preview_webelement = freestyle.find_element(By.LINK_TEXT, 'Hide preview')
    if hide_preview_webelement.is_enabled():
        hide = True

    return [preview, hide]

@pytest.fixture(scope="function")
def revoke_project_tokens(main_page, config):
    """
    Fixture to revoke project-specific tokens from the user's security settings
    if they match the current project name defined in Freestyle.project_name.
    """
    wait = WebDriverWait(main_page, 10)

    main_page.find_element(By.CSS_SELECTOR, 'a[href*="/user/"]').click()
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Security'))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[tooltip*="Current token(s)"]')))

    existing_tokens = main_page.find_elements(By.CSS_SELECTOR, '.token-list-existing-item > input[name="tokenName"]')

    if existing_tokens:
        token_names = [token.get_attribute('value') for token in existing_tokens]

        if any(Freestyle.project_name in name for name in token_names):
            revoke_selector = (
                By.CSS_SELECTOR,
                f'input[value="{Freestyle.project_name}"] ~ span.to-right > a[data-target-url*="/revoke"]'
            )

            revoke_links = wait.until(EC.visibility_of_all_elements_located(revoke_selector))

            for link in revoke_links:
                wait.until(EC.element_to_be_clickable(link)).click()
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-id='ok']"))).click()


@pytest.fixture(scope="function")
def auth_token(main_page, config):
    """
    Fixture to generate a new authentication token for the current project
    and return its value for use in tests.
    """
    wait = WebDriverWait(main_page, 10)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.repeatable-add"))).click()
    token_name_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[placeholder='Default name']")))
    token_name_input.send_keys(Freestyle.project_name)
    wait.until(EC.element_to_be_clickable((By.ID, "api-token-property-token-save"))).click()
    token_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Copy this token'")))

    token = token_element.get_attribute("text")

    main_page.find_element(By.NAME, "Submit").click()
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Dashboard"))).click()

    return token