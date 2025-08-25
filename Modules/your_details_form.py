from selenium.webdriver.common.by import By
# from locators.test.ayush_locator import AyushLocator
from locators.MixPanel.MixPanel import MixPanelLocators
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators

import time

class DetailsForm:
    
    def your_details_form(self, web_user):
        """Test valid login on Web Advisor app using LambdaTest"""
        user = web_user
        user_web_locators = UserWebLocators()

        
        try:
            user.wait_for_element_visible(*user_web_locators.NICKNAME)
            user.input_text(*user_web_locators.NICKNAME, "Ayush Pathania")
            user.click(*user_web_locators.MALE_RADIO_BUTTON)
            user.input_text(*user_web_locators.DOB, "07031999")
           
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
