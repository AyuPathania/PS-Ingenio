from appium.webdriver.common.appiumby import AppiumBy

class AyushLocator:
    """Android locators for Advisor app"""
    
    # Login Screen
    PHONE_NUMBER = (AppiumBy.XPATH, "//*[@text=\"Enter Mobile Number\"]")
    SEND_OTP_BUTTON = (AppiumBy.XPATH, "//*[@resource-id=\"Send_Otp\"]")
    OTP_TEXT = (AppiumBy.XPATH, "//*[@class=\"android.view.ViewGroup\" and ./parent::*[@resource-id=\"OTPInputView\"]]/*[1]/*[@class=\"android.widget.EditText\"]")
    VERIFY_BUTTON = (AppiumBy.XPATH, "//*[@resource-id=\"Verify\"]")
    SIGNUP_LINK = (AppiumBy.ID, "com.example.advisorapp:id/signup_link")