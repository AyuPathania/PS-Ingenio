from drivers.web_driver import WebDriver
from locators.MixPanel.MixPanel import MixPanelLocators
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
from Modules.login import Login
from Modules.send_message_in_live import SendMessage
import time
import re

class TestAdvisorLogin: 
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_06(self, web_advisor, web_user, test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        advisor = web_advisor
        user = web_user
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        mixpanel_locators = MixPanelLocators()
        login = Login() 
        
        try:

            login.login_in_with_advisor(advisor, test_data)
            login.login_in_with_user(user, test_data['user']['valid_email'], test_data['user']['valid_password'])
            
            user.wait_for_element_clickable(*user_web_locators.PROFILE)
            user.click(*user_web_locators.PROFILE)
            user.wait_for_element_clickable(*user_web_locators.SETTING_BUTTON_ON_PROFILE)
            user.click(*user_web_locators.SETTING_BUTTON_ON_PROFILE)
            user.wait_for_element_clickable(*user_web_locators.USER_ID)
            user_id = user.get_element_text(*user_web_locators.USER_ID)
            print(user_id)
            user.wait_for_element_clickable(*user_web_locators.SIDEMENU)
            user.click(*user_web_locators.SIDEMENU)
            user.wait_for_element_clickable(*user_web_locators.SIDEMENU_ACTIVITY)
            user.click(*user_web_locators.SIDEMENU_ACTIVITY)
            user.wait_for_element_visible(*user_web_locators.SEARCH_BY_ADVISORS)
            user.input_text(*user_web_locators.SEARCH_BY_ADVISORS, "tetsLanguageOrder")
            time.sleep(5)
            user.wait_for_element_clickable(*user_web_locators.SELECT_ADVISOR)
            user.click(*user_web_locators.SELECT_ADVISOR)
            user.wait_for_element_visible(*user_web_locators.CONNECT_NOW_BUTTON)
            user.scroll_to_element(*user_web_locators.MESSAGE_LIMIT_TEXT)
            user.wait_for_element_visible(*user_web_locators.MESSAGE_LIMIT_TEXT)
            message_limit_before_send = user.get_element_text(*user_web_locators.MESSAGE_LIMIT_TEXT)
            # Extract digits from the string
            number_before_send = int(re.search(r'\d+', message_limit_before_send).group())
            decrease_message_number = number_before_send -1

            print(number_before_send)  # Output: 5
            # print(type(number_before_send))  # Output: <class 'int'>

            # send_message_in_live.user_send_special_character_message_in_live(user)
            user.wait_for_element_visible(*user_web_locators.YOUR_MESSAGE)
            user.input_text_without_clear(*user_web_locators.YOUR_MESSAGE, "Hello Expert")
            user.wait_for_element_clickable(*user_web_locators.SEND_MESSAGE_BUTTON_USER)
            user.click(*user_web_locators.SEND_MESSAGE_BUTTON_USER)
            time.sleep(3)
            user.wait_for_element_visible(*user_web_locators.USER_MESSAGE_ON_USER_SIDE)
            user_send_msg_text = user.get_element_text(*user_web_locators.USER_MESSAGE_ON_USER_SIDE)
            print("user_send_msg_text: ", user_send_msg_text)

            # msg time split
            
            # Remove the time format (HH:MM AM/PM)
            split_user_text = re.sub(r'\b\d{1,2}:\d{2}\s?(AM|PM)\b', '', user_send_msg_text).strip()

            print("split_user_text: ",split_user_text)  # Output: Hello Expert
            
            
            user.wait_for_element_visible(*user_web_locators.MESSAGE_LIMIT_TEXT)
            message_limit_after_send = user.get_element_text(*user_web_locators.MESSAGE_LIMIT_TEXT)
            # Extract digits from the string
            number_after_send = int(re.search(r'\d+', message_limit_after_send).group())
            
            try:
                assert decrease_message_number == number_after_send
            except AssertionError:
                print(f"Assertion failed for message Limit: expected {decrease_message_number}, found {number_after_send}")
                raise
            



            # advisor activity
            advisor.wait_for_element_clickable(*advisor_web_locators.SEARCH_USER_ID)
            advisor.input_text(*advisor_web_locators.SEARCH_USER_ID, user_id)
            advisor.press_enter(*advisor_web_locators.SEARCH_USER_ID)
            time.sleep(7)
            # advisor.wait_for_element_clickable(*advisor_web_locators.SEARCH_RESULT_TEXT)
            advisor.wait_for_element_clickable(*advisor_web_locators.CLIENT_ID)
            client_id_on_advisor = advisor.get_element_text(*advisor_web_locators.CLIENT_ID)
            print(client_id_on_advisor)
            
            advisor.wait_for_element_clickable(*advisor_web_locators.ACTIONS_MESSAGE)
            advisor.click(*advisor_web_locators.ACTIONS_MESSAGE)
            # Advisor sends a message to User
            # advisor.click(*advisor_web_locators.CLIENT_NAME)
            advisor.wait_for_element_visible(*advisor_web_locators.MESSAGE_TAB)
            advisor.click(*advisor_web_locators.MESSAGE_TAB)

            time.sleep(3)
            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            advisor_side_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            print("advisor_received_message: ", advisor_side_message)

            # message validation
            try:
                assert split_user_text == advisor_side_message
            except AssertionError:
                print(f"Assertion failed for message Limit: expected {split_user_text}, found {advisor_side_message}")
                raise
            


            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_MESSAGE_BOX)
            advisor.input_text_without_clear(*advisor_web_locators.ADVISOR_MESSAGE_BOX, "Hello user")
            advisor.wait_for_element_clickable(*advisor_web_locators.SEND_MESSAGE_BUTTON_ADVISOR)
            advisor.click(*advisor_web_locators.SEND_MESSAGE_BUTTON_ADVISOR)
            
            time.sleep(3)
            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            advisor_side_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
            print("advisor_send_message: ", advisor_side_message)
            

            advisor.wait_for_element_clickable(*advisor_web_locators.CLOSE_ACTIVITY_CHATBOX)
            advisor.click(*advisor_web_locators.CLOSE_ACTIVITY_CHATBOX)
            
            
            # user.refresh_page()
            # time.sleep(10)
            # user.scroll_to_element(*user_web_locators.SIDEMENU_ACTIVITY_MESSAGE_FIELD)
            time.sleep(3)
            user.wait_for_element_visible(*user_web_locators.USER_MESSAGE_ON_USER_SIDE)
            user_send_msg_text = user.get_element_text(*user_web_locators.USER_MESSAGE_ON_USER_SIDE)
            print("user_received_msg_text : ", user_send_msg_text)
            # validation message
            # message validation
            try:
                assert user_send_msg_text == split_user_text
            except AssertionError:
                print(f"Assertion failed for user received msg: expected {user_send_msg_text}, found {split_user_text}")
                raise
            
            
            # Wait a moment to see the result
            time.sleep(5)
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            raise
        finally:
            # Clean up
            advisor.quit_driver()
            user.quit_driver()
