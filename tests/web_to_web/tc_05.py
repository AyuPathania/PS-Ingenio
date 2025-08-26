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
import re
import random
import string

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_valid_login_web(self, web_user, web_advisor, test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        advisor = web_advisor
        user = web_user
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        mixpanel_locators = MixPanelLocators()
        login = Login()
        send_message_in_live = SendMessage()

        
        try:
        
            login.login_in_with_user(user, test_data['user']['valid_email'], test_data['user']['valid_password'])
            login.login_in_with_advisor(advisor, test_data)
            time.sleep(10)

            # add_credit_card details
            user.wait_for_element_visible(*user_web_locators.FIND_ADVISOR)
            user.input_text(*user_web_locators.SEARCH_ADVISOR, "Hubert Blaine")
            user.click(*user_web_locators.FIND_ADVISOR)
            formatted_locator = (user_web_locators.CLICK_ADVISOR[0], 
                    user_web_locators.CLICK_ADVISOR[1].format(advisor_name="Hubert Blaine"))
            user.wait_for_element_visible(*formatted_locator)
            user.click(*formatted_locator)
            user.click(*user_web_locators.CLICK_CHAT)
            user.wait_for_element_visible(*user_web_locators.START_CHAT)
            user.click(*user_web_locators.START_CHAT)
            time.sleep(10)
            # credit_card.add_credit_card(user, test_data)


            # user.wait_for_element_visible(*user_web_locators.START_LIVE_CHAT_BUTTON)
            # user.click(*user_web_locators.START_LIVE_CHAT_BUTTON)

            # details_form.your_details_form(user)

            # user.click(*user_web_locators.START_LIVE_CHAT_BUTTON)
            # advisor.wait_for_element_visible(*advisor_web_locators.ACCEPT_CHAT)
            advisor.click(*advisor_web_locators.ACCEPT_CHAT)
            time.sleep(15)
            send_message_in_live.user_send_special_character_message_in_live(user)
            time.sleep(5)

            # special character assertion
            user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user_send_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            # result = user_send_message.split(":")[0].strip()[:-2].strip()
            result = re.sub(r'\n\d{1,2}:\d{2}', '', user_send_message)
            # Remove "\n" followed by dynamic time in hh:mm format
            
            advisor_receive_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            assert result == advisor_receive_message, f"Expected user message '{result}' to match advisor message '{advisor_receive_message}'"
            print("Special character message assertion passed.")
            
            time.sleep(10)
            send_message_in_live.advisor_send_special_character_message_in_live(advisor)
            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            
            advisor_send_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user_receive_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            # Remove "\n" followed by dynamic time in hh:mm format
            result = re.sub(r'\n\d{1,2}:\d{2}', '', user_receive_message)
            assert advisor_send_message == result, f"Expected user message '{advisor_send_message}' to match advisor message '{result}'"
            print("Special character message assertion passed.")


            time.sleep(10)
            send_message_in_live.user_send_short_message_in_live(user)
            time.sleep(5)
            # short message assertion
            user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user_send_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            result = re.sub(r'\n\d{1,2}:\d{2}', '', user_send_message)

            advisor_receive_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            assert result == advisor_receive_message, f"Expected user message '{result}' to match advisor message '{advisor_receive_message}'"
            print("Short message assertion passed.")

            time.sleep(10)
            send_message_in_live.advisor_send_short_message_in_live(advisor)
            time.sleep(5)
            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            
            advisor_send_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user_receive_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            # Remove "\n" followed by dynamic time in hh:mm format
            result = re.sub(r'\n\d{1,2}:\d{2}', '', user_receive_message)
            assert advisor_send_message == result, f"Expected user message '{advisor_send_message}' to match advisor message '{result}'"
            print("Short message assertion passed.")

            time.sleep(10)
            send_message_in_live.user_send_Long_message_in_live(user)
            time.sleep(5)
            # long message assertion
            user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user_send_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            result = re.sub(r'\n\d{1,2}:\d{2}', '', user_send_message)

            advisor_receive_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            assert result == advisor_receive_message, f"Expected user message '{result}' to match advisor message '{advisor_receive_message}'"
            print("Short message assertion passed.")

            time.sleep(10)
            send_message_in_live.advisor_send_Long_message_in_live(advisor)
            time.sleep(5)
            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            
            advisor_send_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user_receive_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            # Remove "\n" followed by dynamic time in hh:mm format
            result = re.sub(r'\n\d{1,2}:\d{2}', '', user_receive_message)
            assert advisor_send_message == result, f"Expected user message '{advisor_send_message}' to match advisor message '{result}'"
            print("Short message assertion passed.")

            time.sleep(10)
            send_message_in_live.user_send_emojis_message_in_live(user)
            time.sleep(5)
            # emogie assertion
            user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user_send_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            # result = user_send_message.split(":")[0].strip()[:-2].strip()
            result = re.sub(r'\n\d{1,2}:\d{2}', '', user_send_message)
            # Remove "\n" followed by dynamic time in hh:mm format
            
            advisor_receive_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            assert result == advisor_receive_message, f"Expected user message '{result}' to match advisor message '{advisor_receive_message}'"
            print("Special character message assertion passed.")

            time.sleep(10)
            send_message_in_live.advisor_send_emojis_message_in_live(advisor)
            time.sleep(5)
            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            
            advisor_send_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            user_receive_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
            # Remove "\n" followed by dynamic time in hh:mm format
            result = re.sub(r'\n\d{1,2}:\d{2}', '', user_receive_message)
            assert advisor_send_message == result, f"Expected user message '{advisor_send_message}' to match advisor message '{result}'"
            print("Special character message assertion passed.")

            user.minimize_window()
            time.sleep(2)
            user.maximize_window()





            
            # Wait a moment to see the result
            time.sleep(5)
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            raise
        finally:
            # Clean up
            user.quit_driver()
