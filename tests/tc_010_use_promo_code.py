from drivers.web_driver import WebDriver
from Modules.signup import Signup
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
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
        
        signup = Signup()
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
            
            signup.signup_with_user(user)
            # add_credit_card details
            user.wait_for_element_visible(*user_web_locators.FIND_ADVISOR)
            user.input_text(*user_web_locators.SEARCH_ADVISOR, "Hubert Blaine")
            user.click(*user_web_locators.FIND_ADVISOR)
            time.sleep(10)
            user.click(*user_web_locators.CLICK_ADVISOR)
            user.click(*user_web_locators.CLICK_CHAT)
            user.click(*user_web_locators.START_CHAT)
            print("Chat started successfully")
            # credit_card_details
            user.wait_for_element_visible(*user_web_locators.ADD_NEW_CREDIT_DEBIT_CARD)
            print("Add new credit card button is visible")
            user.click(*user_web_locators.ADD_NEW_CREDIT_DEBIT_CARD)
            time.sleep(10)
            user.input_text(*user_web_locators.CARD_HOLDER_NAME, test_data['creditcard']['card_holder_name'])
            # user.switch_to_frame(*user_web_locators.CARD_NUMBER_FRAME)
            user.switch_to_frame(0)
            user.input_text(*user_web_locators.CARD_NUMBER, test_data['creditcard']['card_number'])
            user.switch_to_default_content()
            # user.switch_to_frame(user_web_locators.EXPIRE_DATE_FRAME)
            user.switch_to_frame(1)
            user.input_text(*user_web_locators.EXPIRE_DATE, test_data['creditcard']['expire_date'])
            user.switch_to_default_content()
            # user.switch_to_frame(user_web_locators.CVC_FRAME)
            user.switch_to_frame(2)
            user.input_text(*user_web_locators.CVV, test_data['creditcard']['cvv'])
            user.switch_to_default_content()
            user.input_text(*user_web_locators.ZIP_CODE, test_data['creditcard']['zip_code'])
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
