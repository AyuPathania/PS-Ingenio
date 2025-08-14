from selenium.webdriver.common.by import By
from locators.test.ayush_locator import AyushLocator
import time

class Login:
    
    def login_in_with_user(self, web_user, test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        user = web_user
        locators = AyushLocator()

        
        try:
            user.wait_for_element_visible(*locators.SIGN_IN)
            user.click(*locators.SIGN_IN)
            user.wait_for_element_visible(*locators.EMAIL)
            user.input_text(*locators.EMAIL, test_data['user']['valid_email'])
            user.wait_for_element_visible(*locators.PASSWORD)
            user.input_text(*locators.PASSWORD, test_data['user']['valid_password'])
            user.wait_for_element_visible(*locators.ACCEPT)
            user.click(*locators.ACCEPT)
            user.wait_for_element_visible(*locators.SIGN_IN_BUTTON)
            user.click(*locators.SIGN_IN_BUTTON)
            user.wait_for_page_load()
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            

    def login_in_with_advisor(self, web_advisor, test_data):
   
        advisor = web_advisor
        locators = AyushLocator()

        try:
            advisor.wait_for_element_visible(*locators.EMAIL_ADVISOR)
            advisor.input_text(*locators.EMAIL_ADVISOR, test_data['advisor']['valid_email'])
            advisor.wait_for_element_visible(*locators.PASSWORD_ADVISOR)
            advisor.input_text(*locators.PASSWORD_ADVISOR, test_data['advisor']['valid_password'])
            advisor.click(*locators.SIGN_IN_BUTTON_ADVISOR)
            advisor.wait_for_element_visible(*locators.PROFILE_ADVISOR)
            time.sleep(30)
            advisor.click(*locators.AWAY_ADVISOR)
            advisor.wait_for_element_visible(*locators.AVAILABLE_ADVISOR)
            advisor.click(*locators.AVAILABLE_ADVISOR)

        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            
