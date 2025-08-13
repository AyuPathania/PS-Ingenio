import pytest
from locators.test.ayush_locator import AyushLocator
from locators.test.advisor_locator import AdvisorLocator

class TestAyush:
    """Test cases for User Login functionality"""
    
    # def test_valid_login_android(self, android_user_driver, android_advisor_driver, test_data):
    #     """Test valid login on Android User app"""
    #     user = android_user_driver
    #     advisor = android_advisor_driver
    #     locators = AyushLocator()
    #     advisor_locators = AdvisorLocator()
        
    #     # Input valid credentials
    #     user.input_text(*locators.PHONE_NUMBER, test_data['user']['phone_number'])
    #     advisor.click(*advisor_locators.GET_STARTED)
    #     user.click(*locators.SEND_OTP_BUTTON)
    #     advisor.input_text(*advisor_locators.PHONE_NUMBER, test_data['advisor']['phone_number'])
    #     user.input_text(*locators.OTP_TEXT, test_data['user']['otp'])
    #     advisor.click(*advisor_locators.OTP_SEND)
    #     user.click(*locators.VERIFY_BUTTON)

def test_valid_login_web(web_user_driver, web_advisor_driver, test_data):
    """Test valid login on Web User app"""
    user = web_user_driver
    advisor = web_advisor_driver
    locators = AyushLocator()
    advisor_locators = AdvisorLocator()
    # Input valid credentials
    user_web_url = "https://st:purplestage@staging.purplegarden.co/"  # Replace with actual user web app URL
    user.go(user_web_url)
    advisor_web_url = "https://stg-expert.purpleocean.co/"  # Replace with actual advisor web app URL
    advisor.get(advisor_web_url)
    user.click(*locators.SIGNIN_BUTTON)
    advisor.input_text(*advisor_locators.EMAIL, test_data['advisor']['valid_email'])
    advisor.input_text(*advisor_locators.PASSWORD, test_data['advisor']['valid_password'])
    user.input_text(*locators.EMAIL, test_data['user']['email'])
    # user.input_text(*locators.PASSWORD, test_data['user']['valid_password'])