from drivers.web_driver import WebDriver
from locators.test.ayush_locator import AyushLocator
import time

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_valid_login_web(self, web_user, test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        
        user = web_user
        locators = AyushLocator()

        
        try:
            user.go_to_url("https://st:purplestage@staging.purplegarden.co/")
            user.wait_for_page_load()
            





        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            raise
        finally:
            # Clean up
            user.quit_driver()            