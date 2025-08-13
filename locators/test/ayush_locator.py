from selenium.webdriver.common.by import By

class AyushLocator:
    """Web locators for Advisor app using Selenium By"""
    
    # User
    SIGN_IN = (By.XPATH, "//button[normalize-space()='Sign in']")
    EMAIL = (By.XPATH, "//input[@id='email']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    ACCEPT = (By.XPATH, "//button[@class='wpccBtn--dwsPv']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[@data-testid='login-button' and @type='button']")
    PROFILE = (By.XPATH, "//div[@type='button']//div[contains(text(),'Sweet')]")
    SEARCH_ADVISOR = (By.XPATH, "//input[@placeholder='Search by specialty or reading type']")
    FIND_ADVISOR = (By.XPATH, "(//button[@class='searchButton--zl5Mn'])[1]")
    CLICK_ADVISOR = (By.XPATH, "//img[@alt='Hubert Blaine']")
    CLICK_CHAT = (By.XPATH, "(//span[@class='modeTitle--KFD4l'][normalize-space()='Chat'])[2]")
    START_CHAT = (By.XPATH, "//button[@class='mbw-button-primary']")
    TYPE_MESSAGE_USER2ADVISOR = (By.XPATH, "//div[@class='formContainer--LzD2M']//textarea[@placeholder='Your message...']")
    SEND_MESSAGE_BUTTON_USER = (By.XPATH, "//button[normalize-space()='Send']")
    MIXPANEL_EMAIL = (By.XPATH, "//input[@placeholder='e.g. eleanor@mixpanel.com']")
    MIXPANEL_PASSWORD = (By.XPATH, "//input[@placeholder='e.g. ····················']")
    MIXPANEL_CONTINUE = (By.XPATH, "//button[@name='primaryLoginButton']")
    MIXPANEL_LEFTPANEL = (By.XPATH, "//div[@class='_label-container_17b46_19']")
    MIXPANEL_LEFTPANEL_PROJECT = (By.XPATH, "//span[@class='label' and text()='Purple Garden - Staging']")
    MIXPANEL_USER = (By.XPATH, "//div[normalize-space()='Users']")
    MIXPANEL_USER_SELECTION = (By.XPATH, "//div[title='anna.benishai+2705qa@ingenio.com']")
    MIXPANEL_USER_CHAT=(By.XPATH, "//body[1]/mp-browser-context-root[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/profile-activity[1]/div[1]/div[2]/div[1]/div[1]/div[2]/mp-section[1]/div[1]")
    # advisor
    EMAIL_ADVISOR = (By.XPATH, "//input[@placeholder='Email']")
    PASSWORD_ADVISOR = (By.XPATH, "//input[@placeholder='Password']")
    SIGN_IN_BUTTON_ADVISOR = (By.XPATH, "//button[text()='LOG IN TO YOUR ACCOUNT']")
    PROFILE_ADVISOR = (By.XPATH, "//div[@class='advisor-name']")
    AWAY_ADVISOR = (By.XPATH, "(//div[@class='status away'][normalize-space()='Away'])[1]")
    AVAILABLE_ADVISOR = (By.XPATH, "//div[@class='status available']")
    ACCEPT_CHAT = (By.XPATH, "(//button[normalize-space()='ANSWER CHAT'])[1]")
    TYPE_MESSAGE_ADVISOR2USER = (By.XPATH, "//textarea[@placeholder='Type your message here']")
    SEND_MESSAGE_BUTTON_ADVISOR = (By.XPATH, "//button[normalize-space()='Send']")


    