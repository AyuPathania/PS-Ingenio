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
            login.login_in_with_user(user, "tc02@lt.com", "test123")
            time.sleep(10)
            
            user.wait_for_element_visible(*user_web_locators.SEARCH_ADVISOR)
            user.wait_for_element_visible(*user_web_locators.FIND_ADVISOR)
            user.input_text(*user_web_locators.SEARCH_ADVISOR, "tetsLanguageOrder")
            user.click(*user_web_locators.FIND_ADVISOR)
            formatted_locator = (user_web_locators.CLICK_ADVISOR[0], 
                    user_web_locators.CLICK_ADVISOR[1].format(advisor_name="tetsLanguageOrder"))
            user.wait_for_element_visible(*formatted_locator)
            user.click(*formatted_locator)
            user.wait_for_element_visible(*user_web_locators.CLICK_CHAT)
            user.click(*user_web_locators.CLICK_CHAT)
            time.sleep(5)
            if  user.is_element_displayed(*user_web_locators.AMOUNT_BEFORE_PAYMENT_PRICE):
                amount_before_payment=user.get_element_text(*user_web_locators.AMOUNT_BEFORE_PAYMENT_PRICE)
            else:
                amount_before_payment=user.get_element_text(*user_web_locators.AMOUNT_BEFORE_PAYMENT_SALES)
                
            
            print(f"Amount before payment: {amount_before_payment}")
            user.wait_for_element_visible(*user_web_locators.START_CHAT)
            user.click(*user_web_locators.START_CHAT)

            user.wait_for_element_visible(*user_web_locators.ACTUAL_AMOUNT)
            actual_amount = user.get_element_text(*user_web_locators.ACTUAL_AMOUNT)
            print(f"Actual amount: {actual_amount}")
            assert amount_before_payment == actual_amount, "Amount before payment and actual amount are not the same"
            print("✅ Amount before payment and actual amount are the same")
            pay_button=user.get_element_text(*user_web_locators.PAY_TEXT)
            print(f"Pay button: {pay_button}")
            # pay_button_text= f'Pay ('+pay_button+')'
            pay_button_verify_text= f'Pay ('+actual_amount+')'
            assert pay_button == pay_button_verify_text, "Pay button text and verify text are not the same"
            print("✅ Pay button text and verify text are the same")

            user.wait_for_element_visible(*user_web_locators.PAY_BUTTON)
            user.click(*user_web_locators.PAY_BUTTON)
            user.wait_for_element_visible(*user_web_locators.START_LIVE_CHAT_BUTTON)
            user.click(*user_web_locators.START_LIVE_CHAT_BUTTON)
            print("✅ Accepting chat on advisor side...")
            advisor.wait_for_element_visible(*advisor_web_locators.ACCEPT_CHAT)
            advisor.click(*advisor_web_locators.ACCEPT_CHAT)
            time.sleep(240)
            
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
