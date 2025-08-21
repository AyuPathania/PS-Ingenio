from drivers.web_driver import WebDriver
from Modules.signup import Signup
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
from Modules.modules import Modules
import time
import random
import string

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_valid_login_web(self, web_user,test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        user = web_user
        user_web_locators = UserWebLocators()
        web_user_web_locators = AdvisorWebLocators()
        
        # signup = Signup()
        modules = Modules()
        # card_holder_name = "abcdef"

        
        try:
            
            # user.go_to_url("https://st:purplestage@staging.purplegarden.co/")
            # user.wait_for_page_load()

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
            
            modules.signup_with_user(user)
            # add_credit_card details
            user.wait_for_element_visible(*user_web_locators.FIND_ADVISOR)
            user.input_text(*user_web_locators.SEARCH_ADVISOR, "Hubert Blaine")
            user.click(*user_web_locators.FIND_ADVISOR)
            time.sleep(10)
            user.click(*user_web_locators.CLICK_ADVISOR)
            user.click(*user_web_locators.CLICK_CHAT)
            user.wait_for_element_visible(*user_web_locators.MINUTES_TEXT)
            while True:
                minute_text = user.get_element_text(*user_web_locators.MINUTES_TEXT)
                if minute_text == "1":
                    user.click(*user_web_locators.START_CHAT)
                    break
                else:
                    user.click(*user_web_locators.BACK_BUTTON)
            # user.click(*user_web_locators.START_CHAT)
            print("Chat started successfully")
            # credit_card_details
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
            

         
            
            # Wait a moment to see the result
            time.sleep(5)
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            raise
        finally:
            # Clean up
            user.quit_driver()
