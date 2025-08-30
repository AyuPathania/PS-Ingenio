from drivers.web_driver import WebDriver
from locators.MixPanel.MixPanel import MixPanelLocators
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
from Modules.signup import Signup
from Modules.login import Login
from Modules.send_message_in_live import SendMessage
from Modules.credit_card import CreditCard
from Modules.your_details_form import DetailsForm
import time
import random
import string
import re
class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_tc_03(self, web_user,web_advisor,test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        user = web_user
        advisor = web_advisor
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        signup = Signup()
        login = Login()
        send_message_in_live = SendMessage()
        credit_card = CreditCard()
        details_form = DetailsForm()
        status = "failed"
        try:
            login.login_in_with_advisor(advisor, test_data)
            signup.signup_with_user(user)
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
                    user.get_element_text(*user_web_locators.MINUTES_TEXT)
            user.wait_for_element_visible(*user_web_locators.ADD_NEW_CREDIT_DEBIT_CARD)
            user.click(*user_web_locators.ADD_NEW_CREDIT_DEBIT_CARD)
            credit_card.add_credit_card(user, test_data)
            user.wait_for_element_visible(*user_web_locators.PAY_BUTTON)
            user.click(*user_web_locators.PAY_BUTTON)

                        
            user.wait_for_element_visible(*user_web_locators.START_LIVE_CHAT_BUTTON)
            user.click(*user_web_locators.START_LIVE_CHAT_BUTTON)
        
            details_form.your_details_form(user)
        
            user.click(*user_web_locators.START_LIVE_CHAT_BUTTON)
            advisor.wait_for_element_visible(*advisor_web_locators.ACCEPT_CHAT)
            advisor.click(*advisor_web_locators.ACCEPT_CHAT)
            time.sleep(20)
            send_message_in_live.user_send_special_character_message_in_live(user)
            time.sleep(5)
                # special character assertion
            user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user_send_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            result = re.sub(r'\n\d{1,2}:\d{2}', '', user_send_message)
            
            advisor_receive_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            assert result == advisor_receive_message, f"Expected user message '{result}' to match advisor message '{advisor_receive_message}'"
            # time.sleep(10)
            send_message_in_live.advisor_send_special_character_message_in_live(advisor)
            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            
            advisor_send_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user_receive_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            result = re.sub(r'\n\d{1,2}:\d{2}', '', user_receive_message)
            assert advisor_send_message == result, f"Expected user message '{advisor_send_message}' to match advisor message '{result}'"
            # time.sleep(10)
            send_message_in_live.user_send_short_message_in_live(user)
            time.sleep(5)
            # short message assertion
            user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user_send_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            result = re.sub(r'\n\d{1,2}:\d{2}', '', user_send_message)
            advisor_receive_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            assert result == advisor_receive_message, f"Expected user message '{result}' to match advisor message '{advisor_receive_message}'"
            # time.sleep(10)
            send_message_in_live.advisor_send_short_message_in_live(advisor)
            time.sleep(5)
            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            
            advisor_send_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user_receive_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            result = re.sub(r'\n\d{1,2}:\d{2}', '', user_receive_message)
            assert advisor_send_message == result, f"Expected user message '{advisor_send_message}' to match advisor message '{result}'"
            # time.sleep(10)
            send_message_in_live.user_send_Long_message_in_live(user)
            time.sleep(5)
            # long message assertion
            user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user_send_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            result = re.sub(r'\n\d{1,2}:\d{2}', '', user_send_message)
            advisor_receive_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            assert result == advisor_receive_message, f"Expected user message '{result}' to match advisor message '{advisor_receive_message}'"
            # time.sleep(10)
            send_message_in_live.advisor_send_Long_message_in_live(advisor)
            time.sleep(5)
            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            
            advisor_send_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user_receive_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            result = re.sub(r'\n\d{1,2}:\d{2}', '', user_receive_message)
            assert advisor_send_message == result, f"Expected user message '{advisor_send_message}' to match advisor message '{result}'"
            # time.sleep(10)
            send_message_in_live.user_send_emojis_message_in_live(user)
            time.sleep(5)
            # emoji assertion
            user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user_send_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            result = re.sub(r'\n\d{1,2}:\d{2}', '', user_send_message)
            
            advisor_receive_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            assert result == advisor_receive_message, f"Expected user message '{result}' to match advisor message '{advisor_receive_message}'"
            # time.sleep(10)
            send_message_in_live.advisor_send_emojis_message_in_live(advisor)
            time.sleep(5)
            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            
            advisor_send_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user_receive_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            result = re.sub(r'\n\d{1,2}:\d{2}', '', user_receive_message)
            assert advisor_send_message == result, f"Expected user message '{advisor_send_message}' to match advisor message '{result}'"
            time.sleep(40)
            user.wait_for_element_clickable(*user_web_locators.ADD_CHAT_TIME)
            while True:
                minute_text = user.get_element_text(*user_web_locators.MINUTES_TEXT)
                if minute_text == "1":
                    user.click(*user_web_locators.ADD_CHAT_TIME)
                    break
                else:
                    user.click(*user_web_locators.BACK_BUTTON)
                    user.wait_for_element_visible(*user_web_locators.MINUTES_TEXT)
            time.sleep(70)

            user.wait_for_element_clickable(*user_web_locators.CALL_END)
            user.click(*user_web_locators.CALL_END)
            user.wait_for_element_clickable(*user_web_locators.CLOSE_POPUP_AFTER_CALL)
            user.click(*user_web_locators.CLOSE_POPUP_AFTER_CALL)
            send_message_in_live.after_call_assertions(advisor)
            status = "passed"



         
            
            # Wait a moment to see the result
            time.sleep(5)
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            raise
        finally:
            # Update the status at the end
            
            user.execute_script(f"lambda-status={status}")
            advisor.execute_script(f"lambda-status={status}")

            # Clean up
            user.quit_driver()
            advisor.quit_driver()
