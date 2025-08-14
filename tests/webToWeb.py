from drivers.web_driver import WebDriver
from locators.test.ayush_locator import AyushLocator
import time

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_valid_login_web(self, web_advisor, web_user, test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        advisor = web_advisor
        user = web_user
        locators = AyushLocator()

        
        try:
            advisor.go_to_url("https://stg-expert.purpleocean.co/sign-in")
            advisor.wait_for_page_load()
            user.go_to_url("https://st:purplestage@staging.purplegarden.co/")
            user.wait_for_page_load()
            # advisor.wait_for_element_visible(*locators.EMAIL_ADVISOR)
            # advisor.input_text(*locators.EMAIL_ADVISOR, test_data['advisor']['valid_email'])
            # advisor.wait_for_element_visible(*locators.PASSWORD_ADVISOR)
            # advisor.input_text(*locators.PASSWORD_ADVISOR, test_data['advisor']['valid_password'])
            # advisor.click(*locators.SIGN_IN_BUTTON_ADVISOR)
            # advisor.wait_for_element_visible(*locators.PROFILE_ADVISOR)
            # time.sleep(30)
            # advisor.click(*locators.AWAY_ADVISOR)
            # advisor.wait_for_element_visible(*locators.AVAILABLE_ADVISOR)
            # advisor.click(*locators.AVAILABLE_ADVISOR)
            # time.sleep(10)
        
        #     # Navigate to the staging URL

        
            
            # Wait for and click Sign In button
            user.wait_for_element_visible(*locators.SIGN_IN)
            user.click(*locators.SIGN_IN)
            
            # Wait for and fill email field
            user.wait_for_element_visible(*locators.EMAIL)
            user.input_text(*locators.EMAIL, test_data['user']['valid_email'])
            
            # Wait for and fill password field
            user.wait_for_element_visible(*locators.PASSWORD)
            user.input_text(*locators.PASSWORD, test_data['user']['valid_password'])
            
            # Wait for and click Accept button
            user.wait_for_element_visible(*locators.ACCEPT)
            user.click(*locators.ACCEPT)
            
            # Wait for and click Sign In Button
            user.wait_for_element_visible(*locators.SIGN_IN_BUTTON)
            user.click(*locators.SIGN_IN_BUTTON)
            user.wait_for_page_load()
            
            
        #     # Verify we're logged in by checking profile element
        #     profile_element = user.get_element_text(*locators.PROFILE)
        #     print(f"Profile element text: {profile_element}")
            
            user.wait_for_element_visible(*locators.SEARCH_ADVISOR)
            user.input_text(*locators.SEARCH_ADVISOR, "Hubert Blaine")
        #     time.sleep(10)
        #     user.click(*locators.FIND_ADVISOR)
        #     time.sleep(10)
        #     user.click(*locators.CLICK_ADVISOR)
        #     user.wait_for_element_visible(*locators.CLICK_CHAT)
        #     user.click(*locators.CLICK_CHAT)
        #     user.wait_for_element_visible(*locators.START_CHAT)
        #     user.click(*locators.START_CHAT)
        #     time.sleep(10)
        #     advisor.click(*locators.ACCEPT_CHAT)
        #     time.sleep(10)
        #    # advisor.input_text(*locators.TYPE_MESSAGE_ADVISOR2USER, test_data['advisor']['messageadvisor'])
        #    # advisor.click(*locators.SEND_MESSAGE_BUTTON_ADVISOR)
            
        #    # user.input_text(*locators.TYPE_MESSAGE_USER2ADVISOR, test_data['user']['messageuser'])
        #    # user.click(*locators.SEND_MESSAGE_BUTTON_USER)
        #    # time.sleep(10)
        #     user.go_to_url("https://eu.mixpanel.com/login/")
        #     user.wait_for_element_visible(*locators.MIXPANEL_EMAIL)
        #     user.input_text(*locators.MIXPANEL_EMAIL, test_data['user']['valid_email_mp'])
        #     user.click(*locators.MIXPANEL_CONTINUE)
        #     user.input_text(*locators.MIXPANEL_PASSWORD, test_data['user']['valid_password_mp'])
        #     user.click(*locators.MIXPANEL_CONTINUE)
        #     time.sleep(20)
        #     user.click(*locators.MIXPANEL_LEFTPANEL)
        #     user.click(*locators.MIXPANEL_LEFTPANEL_PROJECT)
        #     time.sleep(15)
        #     user.click(*locators.MIXPANEL_USER)
        #     time.sleep(10)
        #     user.click(*locators.MIXPANEL_USER_SELECTION)
        #     time.sleep(10)
        #     user.click(*locators.MIXPANEL_USER_CHAT)
            time.sleep(10)

            
            
            # Wait a moment to see the result
            time.sleep(5)
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            raise
        finally:
            # Clean up
            advisor.quit_driver()
