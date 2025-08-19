from drivers.web_driver import WebDriver
from locators.MixPanel.MixPanel import MixPanelLocators
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
from Modules.login import Login
import time

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_valid_login_web(self, web_advisor, web_user, test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        advisor = web_advisor
        user = web_user
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        mixpanel_locators = MixPanelLocators()
        login = Login()
        
        try:
            # Login both users
            print("🔐 Logging in users...")
            login.login_in_with_advisor(advisor, test_data)
            login.login_in_with_user(user, test_data)
            time.sleep(10)
            
            # Test user search and chat functionality
            print("💬 Testing user search and chat...")
            profile_element = user.get_element_text(*user_web_locators.PROFILE)
            print(f"Profile element text: {profile_element}")
            
            user.wait_for_element_visible(*user_web_locators.SEARCH_ADVISOR)
            user.input_text(*user_web_locators.SEARCH_ADVISOR, "Hubert Blaine")
            user.wait_for_element_visible(*user_web_locators.FIND_ADVISOR)
            user.click(*user_web_locators.FIND_ADVISOR)
            user.wait_for_element_visible(*user_web_locators.CLICK_ADVISOR)
            user.click(*user_web_locators.CLICK_ADVISOR)
            user.wait_for_element_visible(*user_web_locators.CLICK_CHAT)
            user.click(*user_web_locators.CLICK_CHAT)
            user.wait_for_element_visible(*user_web_locators.START_CHAT)
            user.click(*user_web_locators.START_CHAT)
            
            # Accept chat on advisor side
            print("✅ Accepting chat on advisor side...")
            advisor.wait_for_element_visible(*advisor_web_locators.ACCEPT_CHAT)
            advisor.click(*advisor_web_locators.ACCEPT_CHAT)
            time.sleep(10)
            
            print("🎉 Test completed successfully!")
            
        except Exception as e:
            print(f"❌ Test failed: {e}")
            # Take screenshot on failure
            try:
                advisor.driver.save_screenshot("advisor_failure.png")
                user.driver.save_screenshot("user_failure.png")
                print("📸 Screenshots saved: advisor_failure.png, user_failure.png")
            except:
                print("⚠️ Could not save screenshots")
            raise
        finally:
            # Clean up
            print("🧹 Cleaning up...")
            advisor.quit_driver()
            user.quit_driver()
