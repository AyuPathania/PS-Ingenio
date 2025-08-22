from drivers.web_driver import WebDriver
from locators.MixPanel.MixPanel import MixPanelLocators
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
from Modules.signup import Signup
from Modules.login import Login
from Modules.send_message_in_live import SendMessage
# from Modules.modules import Modules
import time
import random
import string

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_valid_login_web(self, web_user,web_advisor,test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        user = web_user
        advisor = web_advisor
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        signup = Signup()
        login = Login()
        send_message = SendMessage()
        # modules = Modules()
        try:
            login.login_in_with_advisor(advisor, test_data)
            login.signup_with_user(user)
            # user.click(*user_web_locators.SIDEMENU)
            user.wait_for_element_visible(*user_web_locators.FIND_ADVISOR)
            user.input_text(*user_web_locators.SEARCH_ADVISOR, "tetsLanguageOrder")
            user.click(*user_web_locators.FIND_ADVISOR)
            formatted_locator = (user_web_locators.CLICK_ADVISOR[0], 
                    user_web_locators.CLICK_ADVISOR[1].format(advisor_name="tetsLanguageOrder"))
            user.wait_for_element_visible(*formatted_locator)
            user.click(*formatted_locator)
            user.wait_for_element_visible(*user_web_locators.CLICK_CHAT)
            user.click(*user_web_locators.CLICK_CHAT)
            user.wait_for_element_visible(*user_web_locators.MINUTES_TEXT)
            while True:
                minute_text = user.get_element_text(*user_web_locators.MINUTES_TEXT)
                if minute_text == "1":
                    user.click(*user_web_locators.START_CHAT)
                    break
                else:
                    user.click(*user_web_locators.BACK_BUTTON)            
            
            # user.wait_for_element_visible(*user_web_locators.DURATION_CARD)
            # user.click(*user_web_locators.DURATION_CARD)
            user.wait_for_element_visible(*user_web_locators.START_CHAT)
            user.click(*user_web_locators.START_CHAT)
            user.wait_for_element_visible(*user_web_locators.ADD_NEW_CREDIT_DEBIT_CARD)
            user.click(*user_web_locators.ADD_NEW_CREDIT_DEBIT_CARD)
            time.sleep(10)
            # Wait for card holder name field to be clickable (not just visible)
            user.wait_for_element_clickable(*user_web_locators.CARD_HOLDER_NAME)
            user.input_text(*user_web_locators.CARD_HOLDER_NAME, test_data['creditcard']['card_holder_name'])
            
            # Switch to card number iframe and input card number
            card_number_frame = user.find_element(*user_web_locators.CARD_NUMBER_FRAME)
            user.switch_to_frame(card_number_frame)
            user.input_text(*user_web_locators.CARD_NUMBER, test_data['creditcard']['card_number'])
            user.switch_to_default_content()
            
            # Switch to expire date iframe and input expiry date
            expire_date_frame = user.find_element(*user_web_locators.EXPIRE_DATE_FRAME)
            user.switch_to_frame(expire_date_frame)
            user.input_text(*user_web_locators.EXPIRE_DATE, test_data['creditcard']['card_expire'])
            user.switch_to_default_content()
            
            # Switch to CVC iframe and input CVC
            cvc_frame = user.find_element(*user_web_locators.CVC_FRAME)
            user.switch_to_frame(cvc_frame)
            user.input_text(*user_web_locators.CVV, test_data['creditcard']['card_security_code'])
            user.switch_to_default_content()
            
            user.input_text(*user_web_locators.ZIP_CODE, test_data['creditcard']['postcode'])
            user.click(*user_web_locators.ADD_CARD_BUTTON)
            user.wait_for_element_visible(*user_web_locators.PAY_BUTTON)
            user.click(*user_web_locators.PAY_BUTTON)
            user.wait_for_element_visible(*user_web_locators.START_LIVE_CHAT_BUTTON)
            user.click(*user_web_locators.START_LIVE_CHAT_BUTTON)
            user.wait_for_element_visible(*user_web_locators.NICKNAME)
            user.input_text(*user_web_locators.NICKNAME, "Ayush Pathania")
            user.click(*user_web_locators.MALE_RADIO_BUTTON)
            user.input_text(*user_web_locators.DOB, "07031999")
            user.click(*user_web_locators.START_LIVE_CHAT_BUTTON)
            advisor.wait_for_element_visible(*advisor_web_locators.ACCEPT_CHAT)
            advisor.click(*advisor_web_locators.ACCEPT_CHAT)    
            time.sleep(15)
            send_message.send_message_in_live(user, advisor)
            time.sleep(60)
            send_message.after_call_assertions(user, advisor)




         
            
            # Wait a moment to see the result
            time.sleep(5)
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            raise
        finally:
            # Clean up
            user.quit_driver()
            advisor.quit_driver()
