from drivers.web_driver import WebDriver
from locators.test.ayush_locator import AyushLocator
from Modules.signup import Signup
import time
import random
import string

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_valid_login_web(self, web_user,):
        """Test valid login on Web Advisor app using LambdaTest"""
        user = web_user
        locators = AyushLocator()
        signup = Signup()

        
        try:
            
            user.go_to_url("https://st:purplestage@staging.purplegarden.co/")
            user.wait_for_page_load()
            
            # user.click(*locators.JOIN)
            # time.sleep(5)
            # # Wait for and click Accept button
            # user.wait_for_element_visible(*locators.ACCEPT)
            # user.click(*locators.ACCEPT)

            # # random_Email
            # prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5)) +'@' +'aa.com' 
            # char = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
            # user.input_text(*locators.RANDOM_EMAIL, prefix)
            # user.input_text(*locators.RETYPE_EMAIL, prefix)
            # user.input_text(*locators.RANDOM_PASSWORD, char)
            # user.click(*locators.CREATE_ACCOUNT)
            # time.sleep(10)
            # user.click(*locators.TERMS_POLICY)
            # user.wait_for_page_load()
            # time.sleep(50)
            signup.signup_with_user(user)

            # add_credit_card details
            user.wait_for_element_visible(*locators.FIND_ADVISOR)
            user.input_text(*locators.SEARCH_ADVISOR, "Hubert Blaine")
            user.click(*locators.FIND_ADVISOR)
            time.sleep(10)
            user.click(*locators.CLICK_ADVISOR)
            user.click(*locators.CLICK_CHAT)
            user.click(*locators.START_CHAT)

         
            
            # Wait a moment to see the result
            time.sleep(5)
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            raise
        finally:
            # Clean up
            user.quit_driver()
