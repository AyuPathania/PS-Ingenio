from selenium.webdriver.common.by import By

class KasambaAdvisorWebLocators:
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
    SEND_MESSAGE_BUTTON_ADVISOR = (By.XPATH, "//button[@class='client-card-messages__send-button']")