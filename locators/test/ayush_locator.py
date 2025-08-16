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
    USER_SIDE_ADVISOR_MESSAGE_VALIDATION = (By.XPATH, "//div[contains(text(),'Hello Sweet')]")

    # Advisor
    EMAIL_ADVISOR = (By.XPATH, "//input[@placeholder='Email']")
    PASSWORD_ADVISOR = (By.XPATH, "//input[@placeholder='Password']")
    SIGN_IN_BUTTON_ADVISOR = (By.XPATH, "//button[text()='LOG IN TO YOUR ACCOUNT']")
    ALLOW_NOTIFICATIONS = (By.XPATH, "//button[@class='primary']")
    PROFILE_ADVISOR = (By.XPATH, "//div[@class='advisor-name']")
    AWAY_ADVISOR = (By.XPATH, "(//div[@class='status away'][normalize-space()='Away'])[1]")
    AVAILABLE_ADVISOR = (By.XPATH, "//div[@class='status available']")
    ACCEPT_CHAT = (By.XPATH, "(//button[normalize-space()='ANSWER CHAT'])[1]")
    TYPE_MESSAGE_ADVISOR2USER = (By.XPATH, "//textarea[@placeholder='Type your message here']")
    SEND_MESSAGE_BUTTON_ADVISOR = (By.XPATH, "//button[normalize-space()='Send']")
    TOTAL_DURATION = (By.XPATH, "//label[normalize-space()='Total duration']/following-sibling::span")
    YOUR_RATE = (By.XPATH, "//label[normalize-space()='Your rate']/following-sibling::span")
    TOTAL_CREDIT_CHARGED = (By.XPATH, "//label[normalize-space()='Total credit charged']/following-sibling::span")
    TOTAL_EARNED = (By.XPATH, "//label[normalize-space()='Total earned']/following-sibling::span")
    FIRST_MSG_BTN = (By.XPATH, "(//button[contains(@class, 'cl-shedule-button')])[1]")
    ADVISOR_SIDE_MESSAGE_VALIDATION = (By.XPATH, "//div[@class='client-card-messages']//div[contains(text(), 'Hello Hubert')]")
    ADVISOR_MESSAGE_BOX = (By.XPATH, "//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
    ADVISOR_SIDE_OWN_MESSAGE_VALIDATION = (By.XPATH, "//div[normalize-space()='Hello Sweet']")

    # Mixpanel
    MIXPANEL_EMAIL = (By.XPATH, "//input[@placeholder='e.g. eleanor@mixpanel.com']")
    MIXPANEL_PASSWORD = (By.XPATH, "//input[@placeholder='e.g. ····················']")
    MIXPANEL_CONTINUE = (By.XPATH, "//button[@name='primaryLoginButton']")
    MIXPANEL_LEFTPANEL = (By.XPATH, "//div[@class='_label-container_17b46_19']")
    MIXPANEL_LEFTPANEL_PROJECT = (By.XPATH, "//span[@class='label' and text()='Purple Garden - Staging']")
    MIXPANEL_USER = (By.XPATH, "//div[normalize-space()='Users']")
    MIXPANEL_USER_SELECTION = (By.XPATH, "//div[title='anna.benishai+2705qa@ingenio.com']")
    MIXPANEL_USER_CHAT=(By.XPATH, "//body[1]/mp-browser-context-root[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/profile-activity[1]/div[1]/div[2]/div[1]/div[1]/div[2]/mp-section[1]/div[1]")

    # Sidemenu_items

    SIDEMENU = (By.XPATH, "//div[contains(@class, 'contentHolder')]//div[contains(@class, 'headerLogoContainer')]//button[@type='button']//*[name()='svg']")
    SIDEMENU_Activity = (By.XPATH, "//div[contains(text(),'My activity')]")
    SIDEMENU_Activity_UserClick = (By.XPATH, "//span[normalize-space()='Hubert Blaine'][1]")
    SIDEMENU_Activity_Message_Field = (By.XPATH, "//textarea[@id='sendInput']")
    SIDEMENU_Activity_Send_Button = (By.XPATH, "//button[@class='sendButton--R6WFP']//*[name()='svg']")
    SIDEMENU_Activity_User_Message_Validation = (By.XPATH, "(//div[contains(text(),'Hello Hubert')])[2]")