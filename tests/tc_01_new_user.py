from drivers.web_driver import WebDriver
from locators.MixPanel.MixPanel import MixPanelLocators
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
from Modules.modules import Modules
import time
import random
import string

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_valid_login_web(self, web_user,):
        """Test valid login on Web Advisor app using LambdaTest"""
        user = web_user
        user_web_locators = UserWebLocators()
        # advisor_web_locators = AdvisorWebLocators()
        # mixpanel_locators = MixPanelLocators()
        # signup = Signup()
        modules = Modules()

        
        try:
        
            modules.signup_with_user(user)

            # add_credit_card details
            user.wait_for_element_visible(*user_web_locators.FIND_ADVISOR)
            user.input_text(*user_web_locators.SEARCH_ADVISOR, "tetsLanguageOrder")
            user.click(*user_web_locators.FIND_ADVISOR)
            formatted_locator = (user_web_locators.CLICK_ADVISOR[0], 
                    user_web_locators.CLICK_ADVISOR[1].format(advisor_name="tetsLanguageOrder"))
            user.wait_for_element_visible(*formatted_locator)
            user.click(*formatted_locator)
            user.click(*user_web_locators.CLICK_CHAT)
            user.wait_for_element_visible(*user_web_locators.MINUTES_TEXT)
            while True:
                minute_text = user.get_element_text(*user_web_locators.MINUTES_TEXT)
                if minute_text == "1":
                    user.click(*user_web_locators.START_CHAT)
                    break
                else:
                    user.click(*user_web_locators.BACK_BUTTON)
            

         
            
            # Wait a moment to see the result
            time.sleep(5)
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            raise
        finally:
            # Clean up
            user.quit_driver()
