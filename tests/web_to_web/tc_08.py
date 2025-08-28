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
            advisor.press_enter(*advisor_web_locators.SEARCH_USER_ID)
            advisor.wait_for_element_clickable(*advisor_web_locators.SEARCH_RESULT_TEXT)
            advisor.wait_for_element_clickable(*advisor_web_locators.CLIENT_ID)
            client_id_on_advisor = advisor.get_element_text(*advisor_web_locators.CLIENT_ID)
            assert client_id_on_advisor == user_id, "User ID not found in the search results"
            advisor.wait_for_element_clickable(*advisor_web_locators.COUPON_BUTTON)
            advisor.click(*advisor_web_locators.COUPON_BUTTON)
            advisor.wait_for_element_clickable(*advisor_web_locators.SELECTED_COUPON)
            coupon_text = advisor.get_element_text(*advisor_web_locators.SELECTED_COUPON)
            print("coupon_text: ",coupon_text)
            coupon_discount = coupon_text.split("%")[0].strip()
            print("coupon_discount: ",coupon_discount)
            coupon_off = coupon_text.split("your next session")[0].strip()
            print("coupon_off: ",coupon_off)
            advisor.wait_for_element_clickable(*advisor_web_locators.SEND_COUPON_BUTTON)
            advisor.click(*advisor_web_locators.SEND_COUPON_BUTTON)
            user.wait_for_element_clickable(*user_web_locators.HOME_PAGE)
            user.click(*user_web_locators.HOME_PAGE)
            user.wait_for_element_clickable(*user_web_locators.PROFILE)
            user.click(*user_web_locators.PROFILE)
            user.wait_for_element_visible(*user_web_locators.FIND_ADVISOR)
            user.input_text(*user_web_locators.SEARCH_ADVISOR, "Hubert Blaine")
            user.click(*user_web_locators.FIND_ADVISOR)
            formatted_locator = (user_web_locators.CLICK_ADVISOR[0], 
                    user_web_locators.CLICK_ADVISOR[1].format(advisor_name="Hubert Blaine"))
            user.wait_for_element_visible(*formatted_locator)
            user.click(*formatted_locator)
            user.wait_for_element_visible(*user_web_locators.COUPON_TEXT_ON_USER_SIDE)
            coupon_text_on_user_side = user.get_element_text(*user_web_locators.COUPON_TEXT_ON_USER_SIDE)
            assert coupon_text_on_user_side == coupon_off, f"expected value is {coupon_off} but got {coupon_text_on_user_side}"
            user.wait_for_element_visible(*user_web_locators.ACTUAL_PRICE)
            actual_price = user.get_element_text(*user_web_locators.ACTUAL_PRICE)
            print("actual_price: ",actual_price)
            user.wait_for_element_visible(*user_web_locators.DISCOUNTED_PRICE)
            discounted_price = user.get_element_text(*user_web_locators.DISCOUNTED_PRICE)
            print("discounted_price: ",discounted_price)
            discount = float(coupon_discount)/100
            





            

            




        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            raise
        finally:
            # Clean up
            user.quit_driver()
