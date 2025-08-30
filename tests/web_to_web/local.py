import allure
from drivers.web_driver import WebDriver
from locators.locator_factory import LocatorFactory
from Modules.signup import Signup
from Modules.login import Login
from Modules.send_message_in_live import SendMessage
from Modules.credit_card import CreditCard
from config.credentials import CredentialConfig
from config.url_config import URLConfig
import time
from config.config import Config
import re
import random
import string

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_url_local(self, web_user, platform_credentials):
        
        
        """Test valid login on Web Advisor app using LambdaTest"""
        # advisor = web_advisor
        user = web_user
        
        # Get dynamic locators based on current platform
        user_web_locators = LocatorFactory.get_user_web_locators()
        advisor_web_locators = LocatorFactory.get_advisor_web_locators()
        
        # Get dynamic URLs and credentials based on current platform
        user_urls = URLConfig.get_user_urls()
        advisor_urls = URLConfig.get_advisor_urls()
        
        # Get current platform first
        current_platform = Config.get_platform()
        
        # Now use current_platform
        creds = platform_credentials[current_platform]['tc_01']
        
        signup = Signup()
        login = Login()
        send_message_in_live = SendMessage()
        credit_card = CreditCard()
        status = "failed"
        
        try:                
                print("--------------------------------signup with user--------------------------------")
                # Using dynamic credentials (no parameters needed)
                # signup.signup_with_user(user)
                # time.sleep(10)
                
                print("--------------------------------login with user--------------------------------")
                # Using dynamic credentials (no parameters needed)
                login.login_in_with_user(user, creds['user']['email'], creds['user']['password'])
                time.sleep(10)
                
                print("--------------------------------login with advisor--------------------------------")
                # Using dynamic credentials (no parameters needed)
                # login.login_in_with_advisor(advisor, creds['advisor']['email'], creds['advisor']['password'])
                # time.sleep(10)
                
                # If we reach here, test passed
                status = "passed"
                print("--------------------------------Test completed successfully!--------------------------------")

        except Exception as e:
                
            print(f"Test failed: {e}")
            status = "failed"
            # Take screenshot on failure
            raise
        finally:

                user.execute_script(f"lambda-status={status}")
                # advisor.execute_script(f"lambda-status={status}")                
                # Clean up
                user.quit_driver()
                # advisor.quit_driver()