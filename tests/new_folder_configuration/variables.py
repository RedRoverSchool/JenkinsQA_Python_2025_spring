from selenium.webdriver.common.by import By

class FolderNames():
    item_name = "Folder one"
    item_display_name = "My first folder"
    item_description = "This is a sanity test description"

class FolderLocators():
    GENERAL_FIELD = (By.ID, "general")
    SUBMIT_BTN = (By.CSS_SELECTOR, "[name='Submit']")
    DISPLAY_NAME = (By.XPATH, "//*[@id='main-panel']/h1")
    DESCRIPTION = (By.XPATH, "//*[@id='view-message']")
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, "div.setting-main> textarea")
    PREVIEW = (By.CLASS_NAME, "textarea-show-preview")
    TEXT_PREVIEW = (By.CLASS_NAME, "textarea-preview")
    HIDE_PREVIEW = (By.CLASS_NAME, "textarea-hide-preview")