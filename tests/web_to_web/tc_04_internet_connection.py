from drivers.web_driver import WebDriver
from locators.MixPanel.MixPanel import MixPanelLocators
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
from Modules.login import Login
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
        try:

            login.login_in_with_advisor(advisor, test_data)
            login.login_in_with_user(user, test_data['user']['valid_email'], test_data['user']['valid_password'])
            time.sleep(10)
            
            profile_element = user.get_element_text(*user_web_locators.PROFILE)
            print(f"Profile element text: {profile_element}")
            user.wait_for_element_visible(*user_web_locators.FIND_ADVISOR)
            user.input_text(*user_web_locators.SEARCH_ADVISOR, "Hubert Blaine")
            user.click(*user_web_locators.FIND_ADVISOR)
            formatted_locator = (user_web_locators.CLICK_ADVISOR[0], 
                    user_web_locators.CLICK_ADVISOR[1].format(advisor_name="Hubert Blaine"))
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
            time.sleep(10)

            #First message before disconnection of network
            advisor.input_text(*advisor_web_locators.TYPE_MESSAGE_ADVISOR2USER, test_data['advisor']['messageadvisor'])
            advisor.click(*advisor_web_locators.SEND_MESSAGE_BUTTON_ADVISOR)

            user.input_text(*user_web_locators.TYPE_MESSAGE_USER2ADVISOR, test_data['user']['messageuser'])
            user.click(*user_web_locators.SEND_MESSAGE_BUTTON_USER)
            time.sleep(10)

            #User disconnects the network..wait for 20 seconds
            user.go_offline()
            print("🔌 Network disabled")

            time.sleep(20)
            assert user.is_element_displayed(*user_web_locators.NETWORK_OFFLINE), "Network offline message is not displayed on User side"
            print("✅ User: Network offline message is displayed")

            #User reconnects the network
            user.go_online()
            print("🔌 Network enabled")
            time.sleep(20)
            user.input_text(*user_web_locators.TYPE_MESSAGE_USER2ADVISOR, 'User side message after network reconnection after 20 seconds')
            user.click(*user_web_locators.SEND_MESSAGE_BUTTON_USER)

            # advisor disconnects the network..wait for 20 seconds
            advisor.go_offline()
            print("🔌 Network disabled")
            time.sleep(20)

            # advisor reconnects the network
            advisor.go_online()
            print("🔌 Network enabled")
            time.sleep(20)
              
            advisor.input_text(*advisor_web_locators.TYPE_MESSAGE_ADVISOR2USER, 'Advisor side message after network reconnection after 20 seconds')
            advisor.click(*advisor_web_locators.SEND_MESSAGE_BUTTON_ADVISOR)

            # advisor disconnects the network..wait for 40 seconds
            advisor.go_offline()
            print("🔌 Network disabled")
            time.sleep(100)
           
           # advisor reconnects the network
            advisor.go_online()
            print("🔌 Network enabled")
            time.sleep(20)

            assert user.is_element_displayed(*user_web_locators.NETWORK_SESSION_EXPIRED), "Network session expired message is not displayed on User side"
            print("✅ User: Network session expired message is displayed")

            assert advisor.is_element_displayed(*advisor_web_locators.NETWORK_SESSION_EXPIRED), "Network session expired message is not displayed on Advisor side"
            print("✅ Advisor: Network session expired message is displayed")

            assert advisor.is_element_not_displayed(*advisor_web_locators.TYPE_MESSAGE_ADVISOR2USER), "Message input field is still visible on Advisor side after going offline"
            print("✅ Advisor: After going offline and online after 40 seconds, message input field is not visible")

            assert user.is_element_not_displayed(*user_web_locators.TYPE_MESSAGE_USER2ADVISOR), "Message input field is visible on User side after going offline"
            print("✅ User & Advisor: After going offline, hang up button is not visible")

            assert user.is_element_not_displayed(*user_web_locators.HANG_UP_BUTTON), "Hang up button is still visible on User side after going offline"
            print("✅ User: After going offline, hang up button is not visible")



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
            # advisor.wait_for_element_visible(*advisor_web_locators.CLOSE_CHAT_BUTTON)
            # advisor.click(*advisor_web_locators.CLOSE_CHAT_BUTTON)

            
           


        #    # advisor.input_text(*locators.TYPE_MESSAGE_ADVISOR2USER, test_data['advisor']['messageadvisor'])
        #    # advisor.click(*locators.SEND_MESSAGE_BUTTON_ADVISOR)
            
        #    # user.input_text(*locators.TYPE_MESSAGE_USER2ADVISOR, test_data['user']['messageuser'])
        #    # user.click(*locators.SEND_MESSAGE_BUTTON_USER)
        #    # time.sleep(10)
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
