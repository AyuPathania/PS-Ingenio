from selenium.webdriver.common.by import By

class AdvisorWebLocators:
    """Web locators for Advisor website"""
    
    EMAIL_ADVISOR = (By.XPATH, "//input[@placeholder='Email']")
    PASSWORD_ADVISOR = (By.XPATH, "//input[@placeholder='Password']")
    SIGN_IN_BUTTON_ADVISOR = (By.XPATH, "//button[text()='LOG IN TO YOUR ACCOUNT']")
    ALLOW_NOTIFICATIONS = (By.XPATH, "//button[@class='primary']")
    PROFILE_ADVISOR = (By.XPATH, "//div[@class='advisor-name']")
    AWAY_ADVISOR = (By.XPATH, "(//div[@class='status away'][normalize-space()='Away'])[1]")
    AVAILABLE_ADVISOR = (By.XPATH, "//div[@class='status available']")
    ACCEPT_CHAT = (By.XPATH, "(//button[normalize-space()='ANSWER CHAT'])[1]")
    TYPE_MESSAGE_ADVISOR2USER = (By.XPATH, "//textarea[@placeholder='Say hello to your client']")
    SEND_MESSAGE_BUTTON_ADVISOR = (By.XPATH, "//div[@class='send-button']")
    NETWORK_SESSION_EXPIRED = (By.XPATH, "//div[normalize-space()='Your session got disconnected due to connectivity issues, we apologize for the inconvenience']")
    TOTAL_DURATION = (By.XPATH, "//label[normalize-space()='Total duration']/following-sibling::span")
    YOUR_RATE = (By.XPATH, "//label[normalize-space()='Your rate']/following-sibling::span")
    TOTAL_CREDIT_CHARGED = (By.XPATH, "//label[normalize-space()='Total credit charged']/following-sibling::span")
    TOTAL_EARNED = (By.XPATH, "//label[normalize-space()='Total earned']/following-sibling::span")
    FIRST_MSG_BTN = (By.XPATH, "(//button[contains(@class, 'cl-shedule-button')])[1]")
    ADVISOR_SIDE_MESSAGE_VALIDATION = (By.XPATH, "//div[@class='client-card-messages']//div[contains(text(), 'Hello Hubert')]")
    ADVISOR_MESSAGE_BOX = (By.XPATH, "//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
    ADVISOR_SIDE_OWN_MESSAGE_VALIDATION = (By.XPATH, "//div[normalize-space()='Hello Sweet']")
    CLIENT_NAME = (By.XPATH, "//td[normalize-space()='Sweet']")
    MESSAGE_TAB = (By.XPATH, "//div[normalize-space()='Messages']")
    CLOSE_CHAT_BUTTON = (By.XPATH, "//button[normalize-space()='Close Chat']")
    NOTES_TAB = (By.XPATH, "//div[normalize-space()='Notes']")