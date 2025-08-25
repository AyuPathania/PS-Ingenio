from drivers.web_driver import WebDriver
from Modules.signup import Signup
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
from Modules.login import Login
import time
import random
import string

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_valid_login_web(self, web_user,test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        user = web_user
        user_web_locators = UserWebLocators()
        web_user_web_locators = AdvisorWebLocators()
        
        # signup = Signup()
        login = Login() 

        
        try:
            
            login.login_in_with_user(user, "tc02@lt.com", "test123")
            # apply_Promocode
            # user.click(*user_web_locators.HOME_PAGE)
            user.wait_for_page_load()
            user.wait_for_document_loaded()
            time.sleep(5)
            user.click(*user_web_locators.SIDEMENU)
            user.click(*user_web_locators.SIDEMENU_APPLY_PROMOCODE)
            user.input_text(*user_web_locators.SIDEMENU_PROMOCODE, "autotest13")
            user.click(*user_web_locators.SIDEMENU_SUBMIT_BUTTON)
            time.sleep(2)
            user.wait_for_element_visible(*user_web_locators.PROMOCODE_SUCCESS_MESSAGE)
            user.click(*user_web_locators.PROMOCODE_SUCCESS_MESSAGE)


            # user.click(*user_web_locators.CLICK_CHAT)
            # user.click(*user_web_locators.START_CHAT)
            time.sleep(3)

            # add 10 on 10 bonus
            # user.click(*user_web_locators.HOME_PAGE)
            user.wait_for_page_load()
            user.wait_for_document_loaded()
            time.sleep(5)
            user.click(*user_web_locators.SIDEMENU)
            user.click(*user_web_locators.SIDE_MENU_ADD_FUNDS)
            # user.input_text(*user_web_locators.SIDEMENU_PROMOCODE,)
            user.click(*user_web_locators.GET_20_CREDIT)
            user.click(*user_web_locators.PAY_BUTTON)
            time.sleep(2)
            user.wait_for_element_visible(*user_web_locators.PROMOCODE_SUCCESS_MESSAGE)
            user.click(*user_web_locators.PROMOCODE_SUCCESS_MESSAGE)


            


            # add_credit_card details
            user.wait_for_element_visible(*user_web_locators.FIND_ADVISOR)
            user.input_text(*user_web_locators.SEARCH_ADVISOR, "Hubert Blaine")
            user.click(*user_web_locators.FIND_ADVISOR)
            time.sleep(10)
            user.click(*user_web_locators.CLICK_ADVISOR)
            user.click(*user_web_locators.CLICK_CHAT)
            user.wait_for_element_visible(*user_web_locators.MINUTES_TEXT)
            while True:
                minute_text = user.get_element_text(*user_web_locators.MINUTES_TEXT)
                if minute_text == "1":
                    user.click(*user_web_locators.START_CHAT)
                    break
                else:
                    user.click(*user_web_locators.BACK_BUTTON)
            # user.click(*user_web_locators.START_CHAT)
            print("Chat started successfully")
            # credit_card_details
            # user.wait_for_element_visible(*user_web_locators.ADD_NEW_CREDIT_DEBIT_CARD)
            # user.click(*user_web_locators.ADD_NEW_CREDIT_DEBIT_CARD)
            time.sleep(10)

            


            # add_credit_card details
            user.wait_for_element_visible(*user_web_locators.SEARCH_ICON_BUTTON)
            user.click(*user_web_locators.SEARCH_ICON_BUTTON)

            user.input_text(*user_web_locators.SEARCH_ADVISOR, "Hubert Blaine")
            user.click(*user_web_locators.HEADER_SIDE_FIND_ADVISOR)
            # user.click(*user_web_locators.FIND_ADVISOR)
            time.sleep(10)
            # user.click(*user_web_locators.CLICK_ADVISOR)
            formatted_locator = (user_web_locators.CLICK_ADVISOR[0], 
                    user_web_locators.CLICK_ADVISOR[1].format(advisor_name="Hubert Blaine"))
            user.wait_for_element_visible(*formatted_locator)
            user.click(*formatted_locator)
            user.click(*user_web_locators.CLICK_CHAT)
            # user.click(*user_web_locators.START_CHAT)
            time.sleep(3)

            # assert_bonus_message
            Expected_Bonus_Message = "Add $10, get $10 bonus"
            Actual_Bonus_Message=user.get_element_text(*user_web_locators.ADD_BONUS_BUTTON)
            user.assert_element_text_equals(*user_web_locators.ADD_BONUS_BUTTON, Expected_Bonus_Message)
            print("✅ Message validation successful — "+Actual_Bonus_Message)

            
            user.click(*user_web_locators.ADD_BONUS_BUTTON)
            print("show bonus button")
            time.sleep(10)
            user.wait_for_element_visible(*user_web_locators.CONFIRM_BONUS_MESSAGE)
            user.click(*user_web_locators.CONFIRM_BONUS_MESSAGE)
            time.sleep(3)
            user.wait_for_element_visible(*user_web_locators.CLOSE_CHAT_POPUP)
            user.click(*user_web_locators.CLOSE_CHAT_POPUP)


            # check_user_balance
            time.sleep(2)
            user.wait_for_element_visible(*user_web_locators.USER_ICON)
            user.click(*user_web_locators.USER_ICON)
            time.sleep(2)
            user.wait_for_element_visible(*user_web_locators.BALANCE)
            # user.click(*user_web_locators.BALANCE)

            # balance_assertion
            Expected_balance = "Credits: $20"
            Actual_balance = user.get_element_text(*user_web_locators.BALANCE)
            user.assert_element_text_equals(*user_web_locators.BALANCE, Expected_balance)
            print("✅ Message validation successful — "+Actual_balance)



            # user.click(*user_web_locators.START_CHAT)
            time.sleep(10)
            # user_Details_form
            # user.wait_for_element_visible(*user_web_locators.NICKNAME)
            # user.input_text(*user_web_locators.NICKNAME, "TestUser")
            # user.click(*user_web_locators.GENDER)
            # user.input_text(*user_web_locators.DATE_OF_BIRTH, "01/01/1990")
            # user.click(*user_web_locators.START_LIVE_CHAT_BUTTON)
            # time.sleep(5)
            # start live chat
            # credit_card_details
            # user.wait_for_element_visible(*user_web_locators.ADD_NEW_CREDIT_DEBIT_CARD)
            # print("Add new credit card button is visible")
            # user.click(*user_web_locators.ADD_NEW_CREDIT_DEBIT_CARD)
            
            
            
            
            
            

         
            
            # Wait a moment to see the result
            time.sleep(5)
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            raise
        finally:
            # Clean up
            user.quit_driver()
