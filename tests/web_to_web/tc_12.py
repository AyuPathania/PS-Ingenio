from drivers.web_driver import WebDriver
from Modules.signup import Signup
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
from Modules.signup import Signup
from Modules.login import Login
from Modules.credit_card import CreditCard
from Modules.your_details_form import DetailsForm
from Modules.send_message_in_live import SendMessage
import time
import json
import random
import string

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_valid_login_web(self, web_user,web_advisor,test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        user = web_user
        advisor = web_advisor
        user_web_locators = UserWebLocators()
        web_user_web_locators = AdvisorWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        login = Login()
        signup = Signup()
        credit_card = CreditCard()
        details_form = DetailsForm()
        send_message_in_live = SendMessage()
        
        try:
            
            signup.signup_with_user(user)
            login.login_in_with_advisor(advisor, test_data)
            user.wait_for_element_clickable(*user_web_locators.SIDEMENU)
            user.click(*user_web_locators.SIDEMENU)
            user.wait_for_element_visible(*user_web_locators.SIDE_MENU_PAYMENT_METHOD)
            user.click(*user_web_locators.SIDE_MENU_PAYMENT_METHOD)
            
            time.sleep(10)
            credit_card.add_credit_card(user, test_data)
            time.sleep(5)


            # apply_Promocode
            # user.click(*user_web_locators.HOME_PAGE)
            user.wait_for_page_load()
            user.wait_for_document_loaded()
            
            user.wait_for_element_clickable(*user_web_locators.SIDEMENU)
            user.click(*user_web_locators.SIDEMENU)
            user.wait_for_element_clickable(*user_web_locators.SIDEMENU_APPLY_PROMOCODE)
            user.click(*user_web_locators.SIDEMENU_APPLY_PROMOCODE)
            user.wait_for_element_clickable(*user_web_locators.SIDEMENU_PROMOCODE)
            user.input_text(*user_web_locators.SIDEMENU_PROMOCODE, "autotest_pd_9")
            user.wait_for_element_clickable(*user_web_locators.SIDEMENU_SUBMIT_BUTTON)
            user.click(*user_web_locators.SIDEMENU_SUBMIT_BUTTON)
            
            user.wait_for_element_clickable(*user_web_locators.PROMOCODE_SUCCESS_MESSAGE)
            user.click(*user_web_locators.PROMOCODE_SUCCESS_MESSAGE)


            # add_credit_card details
            user.wait_for_element_visible(*user_web_locators.SEARCH_ICON_BUTTON)
            user.click(*user_web_locators.SEARCH_ICON_BUTTON)

            user.wait_for_element_visible(*user_web_locators.SEARCH_ADVISOR)
            user.input_text(*user_web_locators.SEARCH_ADVISOR, "Hubert Blaine")
            user.wait_for_element_clickable(*user_web_locators.HEADER_SIDE_FIND_ADVISOR)
            user.click(*user_web_locators.HEADER_SIDE_FIND_ADVISOR)
            # user.click(*user_web_locators.FIND_ADVISOR)

            # user.click(*user_web_locators.CLICK_ADVISOR)
            formatted_locator = (user_web_locators.CLICK_ADVISOR[0], 
                    user_web_locators.CLICK_ADVISOR[1].format(advisor_name="Hubert Blaine"))
            user.wait_for_element_visible(*formatted_locator)
            user.click(*formatted_locator)
            user.wait_for_element_clickable(*user_web_locators.CLICK_CHAT)
            user.click(*user_web_locators.CLICK_CHAT)
            
            user.click(*user_web_locators.SELECT_ONE_MINUTE)
            user.wait_for_element_clickable(*user_web_locators.START_CHAT)
            user.click(*user_web_locators.START_CHAT)
            
            user.wait_for_element_clickable(*user_web_locators.PAY_BUTTON)
            user.click(*user_web_locators.PAY_BUTTON)
            
            user.wait_for_element_clickable(*user_web_locators.START_LIVE_CHAT_BUTTON)
            user.click(*user_web_locators.START_LIVE_CHAT_BUTTON)
            details_form.your_details_form(user)
            
            user.wait_for_element_clickable(*user_web_locators.START_LIVE_CHAT_BUTTON)
            user.click(*user_web_locators.START_LIVE_CHAT_BUTTON)
            advisor.wait_for_element_visible(*advisor_web_locators.ACCEPT_CHAT)
            advisor.click(*advisor_web_locators.ACCEPT_CHAT)

            time.sleep(75)
            # user.click(*user_web_locators.BACK_BUTTON)
            # user.click(*user_web_locators.ADD_CHAT_TIME)
            user.wait_for_element_visible(*user_web_locators.MINUTES_TEXT)
            while True:
                minute_text = user.get_element_text(*user_web_locators.MINUTES_TEXT)
                if minute_text == "1":
                    user.wait_for_element_clickable(*user_web_locators.ADD_CHAT_TIME)
                    user.click(*user_web_locators.ADD_CHAT_TIME)
                    break
                else:
                    user.wait_for_element_clickable(*user_web_locators.BACK_BUTTON)
                    user.click(*user_web_locators.BACK_BUTTON)
            time.sleep(75)
            
            user.wait_for_element_clickable(*user_web_locators.CALL_END)
            user.click(*user_web_locators.CALL_END)
            user.wait_for_element_clickable(*user_web_locators.CLOSE_QR_CODE_SCREEN)
            
            user.click(*user_web_locators.CLOSE_QR_CODE_SCREEN)
            



            send_message_in_live.discount_50_percent_after_call_assertions(user)
            user.wait_for_element_clickable(*user_web_locators.CONTINUE_BUTTON)
            user.click(*user_web_locators.CONTINUE_BUTTON)







            # assert_bonus_message
            # Expected_Bonus_Message = "Add $10, get $10 bonus"
            # Actual_Bonus_Message=user.get_element_text(*user_web_locators.ADD_BONUS_BUTTON)
            # user.assert_element_text_equals(*user_web_locators.ADD_BONUS_BUTTON, Expected_Bonus_Message)
            # print("✅ Message validation successful — "+Actual_Bonus_Message)

            
            # user.click(*user_web_locators.ADD_BONUS_BUTTON)
            # print("show bonus button")
            # time.sleep(10)
            # user.wait_for_element_visible(*user_web_locators.CONFIRM_BONUS_MESSAGE)
            # user.click(*user_web_locators.CONFIRM_BONUS_MESSAGE)
            # time.sleep(3)
            # user.wait_for_element_visible(*user_web_locators.CLOSE_CHAT_POPUP)
            # user.click(*user_web_locators.CLOSE_CHAT_POPUP)


            # check_user_balance
            # time.sleep(2)
            # user.wait_for_element_visible(*user_web_locators.USER_ICON)
            # user.click(*user_web_locators.USER_ICON)
            # time.sleep(2)
            # user.wait_for_element_visible(*user_web_locators.BALANCE)
            # # user.click(*user_web_locators.BALANCE)

            # # balance_assertion
            # Expected_balance = "Credits: $20"
            # Actual_balance = user.get_element_text(*user_web_locators.BALANCE)
            # user.assert_element_text_equals(*user_web_locators.BALANCE, Expected_balance)
            # print("✅ Message validation successful — "+Actual_balance)



            # user.click(*user_web_locators.START_CHAT)
            time.sleep(10)
            
            
            
            
            
            

         
            
            # Wait a moment to see the result
            # time.sleep(5)
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            raise
        finally:
            # Clean up
            user.quit_driver()
