from selenium.webdriver.common.by import By
# from locators.test.ayush_locator import AyushLocator
from locators.MixPanel.MixPanel import MixPanelLocators
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators

import time

class Login:
    
    def login_in_with_user(self, web_user, test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        user = web_user
        user_web_locators = UserWebLocators()

        
        try:
            user.go_to_url("https://st:purplestage@staging.purplegarden.co/")
            user.wait_for_page_load()
            print("Clearing user cookies, localStorage, and sessionStorage")
            user.driver.delete_all_cookies()
            user.execute_script("""
                try {
                    localStorage.clear();
                    sessionStorage.clear();
                    // Force clear by setting to empty object
                    Object.keys(localStorage).forEach(key => localStorage.removeItem(key));
                    Object.keys(sessionStorage).forEach(key => sessionStorage.removeItem(key));
                } catch(e) {
                    console.log('Storage clear error:', e);
                }
            """)
            user.go_to_url("https://staging.purplegarden.co/")
            # Wait for storage clearing to take effect
            user.wait_for_page_load()
            user.wait_for_element_visible(*user_web_locators.SIGN_IN)
            user.click(*user_web_locators.SIGN_IN)
            user.wait_for_element_visible(*user_web_locators.EMAIL)
            user.input_text(*user_web_locators.EMAIL, test_data['user']['valid_email'])
            user.wait_for_element_visible(*user_web_locators.PASSWORD)
            user.input_text(*user_web_locators.PASSWORD, test_data['user']['valid_password'])
            user.wait_for_element_visible(*user_web_locators.ACCEPT)
            user.click(*user_web_locators.ACCEPT)
            user.wait_for_element_visible(*user_web_locators.SIGN_IN_BUTTON)
            user.click(*user_web_locators.SIGN_IN_BUTTON)
            user.wait_for_page_load()
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            

    def login_in_with_advisor(self, web_advisor, test_data):
   
        advisor = web_advisor
        advisor_web_locators = AdvisorWebLocators()

        try:
            advisor.go_to_url("https://stg-expert.purpleocean.co/sign-in")
            advisor.wait_for_page_load()
            advisor.wait_for_element_visible(*advisor_web_locators.EMAIL_ADVISOR)
            advisor.input_text(*advisor_web_locators.EMAIL_ADVISOR, test_data['advisor']['valid_email'])
            advisor.wait_for_element_visible(*advisor_web_locators.PASSWORD_ADVISOR)
            advisor.input_text(*advisor_web_locators.PASSWORD_ADVISOR, test_data['advisor']['valid_password'])
            advisor.click(*advisor_web_locators.SIGN_IN_BUTTON_ADVISOR)
            # advisor.wait_for_element_visible(*locators.ALLOW_NOTIFICATIONS)
            # advisor.click(*locators.ALLOW_NOTIFICATIONS)
            # time.sleep(30)
            #advisor.switch_to.alert.accept()
            # advisor.handle_alert()
            advisor.wait_for_element_visible(*advisor_web_locators.PROFILE_ADVISOR)
            time.sleep(30)
            advisor.click(*advisor_web_locators.AWAY_ADVISOR)
            advisor.wait_for_element_visible(*advisor_web_locators.AVAILABLE_ADVISOR)
            advisor.click(*advisor_web_locators.AVAILABLE_ADVISOR)

        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            
