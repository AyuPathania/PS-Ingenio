from selenium.webdriver.common.by import By
from locators.locator_factory import LocatorFactory
from config.url_config import URLConfig
from config.credential_config import CredentialConfig
import time
import random
import string

class Signup:
    def signup_with_user(self, web_user, user_name=None, password=None):
        """Test valid signup on Web user using LambdaTest"""
        user = web_user
        user_web_locators = LocatorFactory.get_user_web_locators()
        user_urls = URLConfig.get_user_urls()
        user_credentials = CredentialConfig.get_user_credentials()
        
        try:
                
                # Use dynamic URL based on platform
                user.go_to_url(user_urls['base_url'])
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
                # Use dynamic URL for the second navigation
                user.go_to_url(user_urls['login_url'])
                # Wait for storage clearing to take effect
                user.wait_for_page_load()

                user.wait_for_element_clickable(*user_web_locators.JOIN)
                user.click(*user_web_locators.JOIN)
                
                # Wait for and click Accept button
                user.wait_for_element_visible(*user_web_locators.ACCEPT)
                user.wait_for_element_clickable(*user_web_locators.ACCEPT)
                user.click(*user_web_locators.ACCEPT)

                # random_Email
                prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5)) +'@' +'aa.com' 
                char = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
                user.input_text(*user_web_locators.RANDOM_EMAIL, prefix)
                user.input_text(*user_web_locators.RETYPE_EMAIL, prefix)
                user.input_text(*user_web_locators.RANDOM_PASSWORD, char)
                user.click(*user_web_locators.CREATE_ACCOUNT)
                user.wait_for_element_clickable(*user_web_locators.TERMS_POLICY)
                user.click(*user_web_locators.TERMS_POLICY)
                user.wait_for_page_load()
                time.sleep(3)



        except Exception as e:
                print(f"Test failed: {e}")
                # Take screenshot on failure