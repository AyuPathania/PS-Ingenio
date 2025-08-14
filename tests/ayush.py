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
            user.go_to_url("chrome://version")
            
            # print(f"Page source: {user.get_page_source}")
            time.sleep(10)
            user.go_to_url("https://mail.google.com/")
            time.sleep(10)





        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            raise
        finally:
            # Clean up
            user.quit_driver()            