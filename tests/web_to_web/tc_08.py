from drivers.web_driver import WebDriver
from Modules.signup import Signup
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
from Modules.signup import Signup
from Modules.login import Login
from Modules.credit_card import CreditCard
import time
import json
import re
import random
import string

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_tc_08(self, web_user,web_advisor,test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        user = web_user
        advisor = web_advisor
        user_web_locators = UserWebLocators()
        
        advisor_web_locators = AdvisorWebLocators()
        login = Login()
        
        

        
        try:
            
            login.login_in_with_user(user, "tc08@lt.com", "test123")
            login.login_in_with_advisor(advisor, test_data)

            user.wait_for_element_clickable(*user_web_locators.PROFILE)
            user.click(*user_web_locators.PROFILE)
            user.wait_for_element_clickable(*user_web_locators.SETTING_BUTTON_ON_PROFILE)
            user.click(*user_web_locators.SETTING_BUTTON_ON_PROFILE)
            user.wait_for_element_clickable(*user_web_locators.USER_ID)
            user_id = user.get_element_text(*user_web_locators.USER_ID)
            print(user_id)
            advisor.wait_for_element_clickable(*advisor_web_locators.SEARCH_USER_ID)
            advisor.input_text(*advisor_web_locators.SEARCH_USER_ID, user_id)
            advisor.press_enter()
            advisor.wait_for_element_clickable(*advisor_web_locators.SEARCH_RESULT_TEXT)
            advisor.wait_for_element_clickable(*advisor_web_locators.CLIENT_ID)
            client_id_on_advisor = advisor.get_element_text(*advisor_web_locators.CLIENT_ID)
            assert client_id_on_advisor == user_id, "User ID not found in the search results"




        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            raise
        finally:
            # Clean up
            user.quit_driver()
