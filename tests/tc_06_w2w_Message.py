from drivers.web_driver import WebDriver
from locators.MixPanel.MixPanel import MixPanelLocators
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
from Modules.login import Login
from Modules.send_message_in_live import SendMessage
import time

class TestAdvisorLogin: 
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_valid_login_web(self, web_advisor, web_user, test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        advisor = web_advisor
        user = web_user
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        mixpanel_locators = MixPanelLocators()
        # login = Login()
        login = Login() 
        send_message = SendMessage()
        try:

            login.login_in_with_advisor(advisor, test_data)
            login.login_in_with_user(user, test_data['user']['valid_email'], test_data['user']['valid_password'])
            time.sleep(10)
            
            profile_element = user.get_element_text(*user_web_locators.PROFILE)
            print(f"Profile element text: {profile_element}")
            user.wait_for_element_visible(*user_web_locators.SEARCH_ADVISOR)
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

            advisor.wait_for_element_visible(*advisor_web_locators.ACCEPT_CHAT)
            advisor.click(*advisor_web_locators.ACCEPT_CHAT)
            time.sleep(40)
            send_message.send_message_in_live(user, advisor)
            time.sleep(10)
            send_message.after_call_assertions(user, advisor)
            # user.click(*user_web_locators.HANG_UP_BUTTON)
            # user.wait_for_element_visible(*user_web_locators.CONTINUE_BUTTON)
            # user.click(*user_web_locators.CONTINUE_BUTTON)
            
            # advisor.wait_for_element_visible(*advisor_web_locators.TOTAL_DURATION)
            # total_duration = advisor.get_element_text(*advisor_web_locators.TOTAL_DURATION)
            # advisor.assert_element_text_equals(*advisor_web_locators.TOTAL_DURATION, total_duration)
            # # print(f"Total duration: {total_duration}")
            # your_rate = advisor.get_element_text(*advisor_web_locators.YOUR_RATE)
            # advisor.assert_element_text_equals(*advisor_web_locators.YOUR_RATE, your_rate)
            # # print(f"Your rate: {your_rate}")
            # total_credit_charged = advisor.get_element_text(*advisor_web_locators.TOTAL_CREDIT_CHARGED)
            # advisor.assert_element_text_equals(*advisor_web_locators.TOTAL_CREDIT_CHARGED, total_credit_charged)
            # # print(f"Total credit charged: {total_credit_charged}")
            # total_earned = advisor.get_element_text(*advisor_web_locators.TOTAL_EARNED)
            # advisor.assert_element_text_equals(*advisor_web_locators.TOTAL_EARNED, total_earned)
            # print(f"Total earned: {total_earned}")
            advisor.wait_for_element_visible(*advisor_web_locators.CLOSE_CHAT_BUTTON)
            advisor.click(*advisor_web_locators.CLOSE_CHAT_BUTTON)


            # Advisor sends a message to User
            advisor.click(*advisor_web_locators.CLIENT_NAME)
            advisor.wait_for_element_visible(*advisor_web_locators.MESSAGE_TAB)
            advisor.click(*advisor_web_locators.MESSAGE_TAB)
            advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_MESSAGE_BOX)
            advisor.input_text_advisor(*advisor_web_locators.ADVISOR_MESSAGE_BOX, "Hello Sweet")
            advisor.click(*advisor_web_locators.SEND_MESSAGE_BUTTON_ADVISOR)
            

            own_message_val_advisor_side = advisor.get_element_text(*advisor_web_locators.ADVISOR_SIDE_OWN_MESSAGE_VALIDATION)
            advisor.assert_element_text_equals(*advisor_web_locators.ADVISOR_SIDE_OWN_MESSAGE_VALIDATION, own_message_val_advisor_side)
            print(f"Message displayed on the advisor side is: {own_message_val_advisor_side}")
            
            user.scroll_to_element(*user_web_locators.SIDEMENU_ACTIVITY_MESSAGE_FIELD)
            own_message_val_user_side = user.get_element_text(*advisor_web_locators.ADVISOR_SIDE_OWN_MESSAGE_VALIDATION)
            user.assert_element_text_equals(*advisor_web_locators.ADVISOR_SIDE_OWN_MESSAGE_VALIDATION, own_message_val_user_side)
            print(f"Message displayed on the user side is: {own_message_val_user_side}")
            

            # ✅ compare messages send by advisor side first and then to user side
            assert own_message_val_advisor_side == own_message_val_user_side, "User and Advisor messages do not match!"
            print("✅ Message validation successful — Advisor to user:both sides show the same message.")
            
            
            #User sends a message to Advisor

            user.input_text(*user_web_locators.SIDEMENU_ACTIVITY_MESSAGE_FIELD, "Hello Hubert")
            user.click(*user_web_locators.SIDEMENU_ACTIVITY_SEND_BUTTON)
            
            message_val_userside = user.get_element_text(*user_web_locators.SIDEMENU_ACTIVITY_USER_MESSAGE_VALIDATION)
            user.assert_element_text_equals(*user_web_locators.SIDEMENU_ACTIVITY_USER_MESSAGE_VALIDATION, message_val_userside)
            print(f"Message displayed on the user side is: {message_val_userside}")


            advisor.click(*advisor_web_locators.NOTES_TAB)
            advisor.click(*advisor_web_locators.MESSAGE_TAB)
            message_val_advisor_side = advisor.get_element_text(*advisor_web_locators.ADVISOR_SIDE_MESSAGE_VALIDATION)
            advisor.assert_element_text_equals(*advisor_web_locators.ADVISOR_SIDE_MESSAGE_VALIDATION, message_val_advisor_side)
            print(f"Message displayed on the advisor side is: {message_val_advisor_side}")

            # # ✅ compare messages send by user side first and then to advisor side
            assert message_val_userside == message_val_advisor_side, "User and Advisor messages do not match!"
            print("✅ User to Advisor: Message validation successful — both sides show the same message.")
            time.sleep(10)
            
            # user.go_to_url("https://eu.mixpanel.com/login/")
            # user.wait_for_element_visible(*locators.MIXPANEL_EMAIL)
            # user.input_text(*locators.MIXPANEL_EMAIL, test_data['user']['valid_email_mp'])
            # user.click(*locators.MIXPANEL_CONTINUE)
            # user.input_text(*locators.MIXPANEL_PASSWORD, test_data['user']['valid_password_mp'])
            # user.click(*locators.MIXPANEL_CONTINUE)
            # time.sleep(20)
            # user.click(*locators.MIXPANEL_LEFTPANEL)
            # user.click(*locators.MIXPANEL_LEFTPANEL_PROJECT)
            # time.sleep(15)
            # user.click(*locators.MIXPANEL_USER)
            # time.sleep(10)
            # user.click(*locators.MIXPANEL_USER_SELECTION)
            # time.sleep(10)
            # user.click(*locators.MIXPANEL_USER_CHAT)
            # time.sleep(10)

            
            
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
