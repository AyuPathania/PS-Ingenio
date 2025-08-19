from selenium.webdriver.common.by import By

class MixPanelLocators:
    """MixPanel locators"""
    
    MIXPANEL_EMAIL = (By.XPATH, "//input[@placeholder='e.g. eleanor@mixpanel.com']")
    MIXPANEL_PASSWORD = (By.XPATH, "//input[@placeholder='e.g. ····················']")
    MIXPANEL_CONTINUE = (By.XPATH, "//button[@name='primaryLoginButton']")
    MIXPANEL_LEFTPANEL = (By.XPATH, "//div[@class='_label-container_17b46_19']")
    MIXPANEL_LEFTPANEL_PROJECT = (By.XPATH, "//span[@class='label' and text()='Purple Garden - Staging']")
    MIXPANEL_USER = (By.XPATH, "//div[normalize-space()='Users']")
    MIXPANEL_USER_SELECTION = (By.XPATH, "//div[title='anna.benishai+2705qa@ingenio.com']")
    MIXPANEL_USER_CHAT=(By.XPATH, "//body[1]/mp-browser-context-root[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/profile-activity[1]/div[1]/div[2]/div[1]/div[1]/div[2]/mp-section[1]/div[1]")
