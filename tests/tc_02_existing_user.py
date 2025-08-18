from drivers.web_driver import WebDriver
from locators.test.ayush_locator import AyushLocator
from Modules.login import Login
import time

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_valid_login_web(self, web_advisor, web_user, test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        advisor = web_advisor
        user = web_user
        locators = AyushLocator()
        login = Login()
        
        try:
            advisor.go_to_url("https://stg-expert.purpleocean.co/sign-in")
            advisor.wait_for_page_load()
            user.go_to_url("https://st:purplestage@staging.purplegarden.co/")
            user.refresh_page()
            
            user.wait_for_page_load()
            login.login_in_with_advisor(advisor, test_data)
            login.login_in_with_user(user, test_data)
            time.sleep(10)
            
            profile_element = user.get_element_text(*locators.PROFILE)
            print(f"Profile element text: {profile_element}")
            user.wait_for_element_visible(*locators.SEARCH_ADVISOR)
            user.input_text(*locators.SEARCH_ADVISOR, "Hubert Blaine")
            user.wait_for_element_visible(*locators.FIND_ADVISOR)
            user.click(*locators.FIND_ADVISOR)
            user.wait_for_element_visible(*locators.CLICK_ADVISOR)
            user.click(*locators.CLICK_ADVISOR)
            user.wait_for_element_visible(*locators.CLICK_CHAT)
            user.click(*locators.CLICK_CHAT)
            user.wait_for_element_visible(*locators.START_CHAT)
            user.click(*locators.START_CHAT)
            advisor.wait_for_element_visible(*locators.ACCEPT_CHAT)
            advisor.click(*locators.ACCEPT_CHAT)
            time.sleep(40)
            advisor.wait_for_element_visible(*locators.TOTAL_DURATION)
            total_duration = advisor.get_element_text(*locators.TOTAL_DURATION)
            advisor.assert_element_text_equals(*locators.TOTAL_DURATION, total_duration)
            # print(f"Total duration: {total_duration}")
            your_rate = advisor.get_element_text(*locators.YOUR_RATE)
            advisor.assert_element_text_equals(*locators.YOUR_RATE, your_rate)
            # print(f"Your rate: {your_rate}")
            total_credit_charged = advisor.get_element_text(*locators.TOTAL_CREDIT_CHARGED)
            advisor.assert_element_text_equals(*locators.TOTAL_CREDIT_CHARGED, total_credit_charged)
            # print(f"Total credit charged: {total_credit_charged}")
            total_earned = advisor.get_element_text(*locators.TOTAL_EARNED)
            advisor.assert_element_text_equals(*locators.TOTAL_EARNED, total_earned)
            print(f"Total earned: {total_earned}")


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
