from drivers.web_driver import WebDriver
from locators.MixPanel.MixPanel import MixPanelLocators
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
from Modules.signup import Signup
import time
import random
import string

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_valid_login_web(self, web_user,):
        """Test valid login on Web Advisor app using LambdaTest"""
        user = web_user
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        mixpanel_locators = MixPanelLocators()
        signup = Signup()

        
        try:
            
            # user.go_to_url("https://st:purplestage@staging.purplegarden.co/")
            # user.wait_for_page_load()
            
            # # user.click(*user_web_locators.JOIN)
            # # time.sleep(5)
            # # # Wait for and click Accept button
            # # user.wait_for_element_visible(*user_web_locators.ACCEPT)
            # # user.click(*user_web_locators.ACCEPT)

            # # # random_Email
            # # prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5)) +'@' +'aa.com' 
            # # char = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
            # # user.input_text(*user_web_locators.RANDOM_EMAIL, prefix)
            # # user.input_text(*user_web_locators.RETYPE_EMAIL, prefix)
            # # user.input_text(*user_web_locators.RANDOM_PASSWORD, char)
            # # user.click(*user_web_locators.CREATE_ACCOUNT)
            # # time.sleep(10)
            # # user.click(*user_web_locators.TERMS_POLICY)
            # # user.wait_for_page_load()
            # # time.sleep(50)
            signup.signup_with_user(user)

            # add_credit_card details
            user.wait_for_element_visible(*user_web_locators.FIND_ADVISOR)
            user.input_text(*user_web_locators.SEARCH_ADVISOR, "Hubert Blaine")
            user.click(*user_web_locators.FIND_ADVISOR)
            time.sleep(10)
            user.click(*user_web_locators.CLICK_ADVISOR)
            user.click(*user_web_locators.CLICK_CHAT)
            user.click(*user_web_locators.START_CHAT)

         
            
            # Wait a moment to see the result
            time.sleep(5)
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            raise
        finally:
            # Clean up
            user.quit_driver()
