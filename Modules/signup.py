from selenium.webdriver.common.by import By
from locators.test.ayush_locator import AyushLocator
import time
import random
import string

class Signup:
    def signup_with_user(self, web_user):
        """Test valid signup on Web user using LambdaTest"""
        user = web_user
        locators = AyushLocator()
        
        
        try:
                
                # user.go_to_url("https://st:purplestage@staging.purplegarden.co/")
                # user.wait_for_page_load()
                
                user.click(*locators.JOIN)
                time.sleep(5)
                # Wait for and click Accept button
                user.wait_for_element_visible(*locators.ACCEPT)
                user.click(*locators.ACCEPT)

                # random_Email
                prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5)) +'@' +'aa.com' 
                char = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
                user.input_text(*locators.RANDOM_EMAIL, prefix)
                user.input_text(*locators.RETYPE_EMAIL, prefix)
                user.input_text(*locators.RANDOM_PASSWORD, char)
                user.click(*locators.CREATE_ACCOUNT)
                time.sleep(10)
                user.click(*locators.TERMS_POLICY)
                user.wait_for_page_load()
                time.sleep(50)


        except Exception as e:
                print(f"Test failed: {e}")
                # Take screenshot on failure