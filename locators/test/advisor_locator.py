from appium.webdriver.common.appiumby import AppiumBy

class AdvisorLocator:
    """Android locators for Advisor app"""
    
    # Login Screen
    GET_STARTED = (AppiumBy.XPATH, "//*[@content-desc=\"Get Started\"]")
    PHONE_NUMBER = (AppiumBy.XPATH, "//*[@text=\"Enter 10-digit mobile number\"]")
    OTP_SEND = (AppiumBy.XPATH, "//*[@content-desc=\"Send OTP\"]")
    VERIFY_BUTTON = (AppiumBy.XPATH, "//*[@resource-id=\"Verify\"]")
    SIGNUP_LINK = (AppiumBy.ID, "com.example.advisorapp:id/signup_link")