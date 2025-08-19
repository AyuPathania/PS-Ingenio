from selenium.webdriver.common.by import By
from locators.user.web_locators import UserWebLocators
import time
import random
import string

class Signup:
    def signup_with_user(self, web_user):
        """Test valid signup on Web user using LambdaTest"""
        user = web_user
        user_web_locators = UserWebLocators()
        
        
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

                user.click(*user_web_locators.JOIN)
                time.sleep(5)
                # Wait for and click Accept button
                user.wait_for_element_visible(*user_web_locators.ACCEPT)
                user.click(*user_web_locators.ACCEPT)

                # random_Email
                prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5)) +'@' +'aa.com' 
                char = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
                user.input_text(*user_web_locators.RANDOM_EMAIL, prefix)
                user.input_text(*user_web_locators.RETYPE_EMAIL, prefix)
                user.input_text(*user_web_locators.RANDOM_PASSWORD, char)
                user.click(*user_web_locators.CREATE_ACCOUNT)
                time.sleep(10)
                user.click(*user_web_locators.TERMS_POLICY)
                user.wait_for_page_load()
                time.sleep(50)


        except Exception as e:
                print(f"Test failed: {e}")
                # Take screenshot on failure