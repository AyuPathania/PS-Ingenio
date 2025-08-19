from selenium.webdriver.common.by import By

class UserWebLocators:
    """Web locators for User website"""
    
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
    TYPE_MESSAGE_USER2ADVISOR = (By.XPATH, "//textarea[@placeholder='Your message...']")
    SEND_MESSAGE_BUTTON_USER = (By.XPATH, "//button[normalize-space()='Send']")
    NETWORK_OFFLINE = (By.XPATH, "//div[contains(text(),'Network seems to be offline')]")
    NETWORK_SESSION_EXPIRED = (By.XPATH, "//div[@class='hangupError--B8h5h']")
    JOIN = (By.XPATH, "//button[@class='loginButtonContainer--r7uit']")
    RANDOM_EMAIL = (By.XPATH, "//input[@id='email']")
    RETYPE_EMAIL = (By.XPATH, "//input[@id='confirmEmail']")
    RANDOM_PASSWORD = (By.XPATH, "//input[@id='password']")
    CREATE_ACCOUNT = (By.XPATH, "//button[@class='actionButton--UxfDy']")
    TERMS_POLICY = (By.XPATH, "//button[@class='ppTofModalSignUpButton--Imglp']")
    HANG_UP_BUTTON = (By.XPATH, "//button[@class='hangupBtn--EGCTW']")
    CONTINUE_BUTTON = (By.XPATH, "//button[normalize-space()='Continue']")
        # Sidemenu_items

    SIDEMENU = (By.XPATH, "//div[contains(@class, 'contentHolder')]//div[contains(@class, 'headerLogoContainer')]//button[@type='button']//*[name()='svg']")
    SIDEMENU_ACTIVITY = (By.XPATH, "//div[contains(text(),'My activity')]")
    SIDEMENU_ACTIVITY_USERCLICK = (By.XPATH, "//span[normalize-space()='Hubert Blaine'][1]")
    SIDEMENU_ACTIVITY_MESSAGE_FIELD = (By.XPATH, "//textarea[@id='sendInput']")
    SIDEMENU_ACTIVITY_SEND_BUTTON = (By.XPATH, "//button[@class='sendButton--R6WFP']//*[name()='svg']")
    SIDEMENU_ACTIVITY_USER_MESSAGE_VALIDATION = (By.XPATH, "(//div[contains(text(),'Hello Hubert')])[1]")
