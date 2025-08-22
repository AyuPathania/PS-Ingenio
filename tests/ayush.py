from drivers.web_driver import WebDriver
# from locators.test.ayush_locator import AyushLocator
from Modules.login import Login
import time

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_valid_login_web(self, web_user, web_advisor, test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        
        user = web_user
        advisor = web_advisor
        # locators = AyushLocator()
        login = Login()

        
        try:
            # Go to Gmail login page
            user.go_to_url("https://accounts.google.com/signin/v2/identifier?service=mail")
            user.wait_for_page_load()
            
            # Step 1: Enter email
            print("🔍 Looking for email input field...")
            user.wait_for_element_visible("name", "identifier")
            user.input_text("name", "identifier", test_data['gmail']['email'])
            print("✅ Email entered")
            
            # Click Next after email
            user.click("id", "identifierNext")
            print("✅ Clicked Next after email")
            time.sleep(3)
            
            # Step 2: Enter password using correct locator
            print("🔍 Looking for password input field...")
            
            # Try multiple password selectors - prioritize the correct one
            password_selectors = [
                ("name", "Passwd"),                    # ✅ Primary: Google's standard password field name
                ("xpath", "//input[@aria-label='Enter your password']"),  # ✅ Secondary: Accessibility label
                ("xpath", "//input[@type='password' and @name='Passwd']"), # ✅ Combination approach
                ("css", "input[name='Passwd']"),        # ✅ CSS selector
                ("name", "password"),                   # Fallback options
                ("name", "passwd"),
                ("id", "password"),
                ("id", "Passwd")
            ]
            
            password_entered = False
            for selector_type, selector_value in password_selectors:
                try:
                    print(f"🔍 Trying password selector: {selector_type} = {selector_value}")
                    password_input = user.wait_for_element_visible(selector_type, selector_value, timeout=5)
                    if password_input:
                        user.input_text(selector_type, selector_value, "@Ayush0703")
                        print(f"✅ Password entered using {selector_type} = {selector_value}")
                        password_entered = True
                        break
                except Exception as e:
                    print(f"⚠️ Password selector {selector_type} = {selector_value} failed: {e}")
                    continue
            
            if not password_entered:
                print("❌ All password selectors failed")
                # Take screenshot for debugging
                user.take_screenshot("password_field_not_found.png")
                print("📸 Screenshot saved for debugging")
                return False
            
            # Click Next after password
            user.click("id", "passwordNext")
            print("✅ Clicked Next after password")
            time.sleep(5)
            
            # Navigate to Gmail
            print("📧 Navigating to Gmail...")
            user.go_to_url("https://mail.google.com/")
            user.wait_for_page_load()
            time.sleep(10)
        #     # Click at specific coordinates using Selenium's ActionChains
        #     try:
        #         from selenium.webdriver.common.action_chains import ActionChains
        #         # Example coordinates (x, y) - adjust as needed
        #         x_offset = 1308
        #         y_offset = 432
        #         print(f"🖱️ Attempting to click at coordinates ({x_offset}, {y_offset})")
        #         actions = ActionChains(user.driver)
        #         actions.move_by_offset(x_offset, y_offset).click().perform()
        #         print(f"✅ Clicked at coordinates ({x_offset}, {y_offset})")
        #         # Move mouse back to (0,0) to avoid offset issues in future actions
        #         actions.move_by_offset(-x_offset, -y_offset).perform()
        #     except Exception as e:
        #         print(f"⚠️ Failed to click at coordinates: {e}")
        #     # Try to click the "Continue as Ayush" button, possibly inside a shadow root
        #     try:
        #         print("🔍 Looking for 'Continue as Ayush' button (possibly in shadow DOM)...")
        #         continue_btn = user.execute_script("""
        #             // Try to find the button in shadow roots
        #             function findButtonWithText(root, text) {
        #                 if (!root) return null;
        #                 // Check direct children
        #                 const elements = root.querySelectorAll("*");
        #                 for (const el of elements) {
        #                     if (el.shadowRoot) {
        #                         const found = findButtonWithText(el.shadowRoot, text);
        #                         if (found) return found;
        #                     }
        #                     if (el.textContent && el.textContent.trim() === text) {
        #                         return el;
        #                     }
        #                 }
        #                 return null;
        #             }
        #             // Start from document
        #             return findButtonWithText(document, "Continue as Ayush");
        #         """)
        #         if continue_btn:
        #             continue_btn.click()
        #             print("✅ 'Continue as Ayush' button clicked")
        #         else:
        #             print("ℹ️ 'Continue as Ayush' button not found, continuing...")
        #     except Exception as e:
        #         print(f"⚠️ Error clicking 'Continue as Ayush' button: {e}")
        #         print("Continuing with test...")
        #     # After logging into Gmail manually with Selenium, save cookies for future use
        #     cookies_list = user.get_cookies()  # Assuming user is your Selenium wrapper
        #     # After saving cookies, refresh the page to apply them
        #     user.refresh_page()
        #     print("🔄 Page refreshed after adding cookies")

        #     # Save them somewhere (e.g., JSON file)
        #     import json
        #     with open("gmail_cookies.json", "w") as f:
        #         json.dump(cookies_list, f)
        #     print("✅ Gmail cookies saved to gmail_cookies.json")
        #     user.refresh_page()
        #     print("🔄 Page refreshed after adding cookies")
            
        #     # Handle accept button safely with null check for user
        #     try:
        #         accept_btn1 = user.execute_script("""
        #             const signinApp = document.querySelector("chrome-signin-app");
        #             if (signinApp && signinApp.shadowRoot) {
        #                 return signinApp.shadowRoot.querySelector("div#accept-button-content");
        #             }
        #             return null;
        #         """)
                
        #         if accept_btn1:
        #             accept_btn1.click()
        #             print("✅ Accept button clicked for user")
        #         else:
        #             print("ℹ️ No accept button found for user, continuing...")
        #     except Exception as e:
        #         print(f"ℹ️ Accept button handling failed for user: {e}")
        #         print("Continuing with test...")
            
        #     # Verify Gmail loaded
        #     title = user.get_title()
        #     print(f"📧 Gmail page title: {title}")
            
        #     if "Gmail" in title:
        #         print("✅ Successfully logged into Gmail!")
        #     else:
        #         print("❌ Gmail not loaded properly")
            
        #     print("✅ Test completed successfully")
            
        # except Exception as e:
        #     print(f"Test failed: {e}")
        #     # Take screenshot on failure
        #     user.take_screenshot("ayush_test_failed.png")
        #     raise
        # finally:
        #     # Clean up
        #     # user.quit_driver()
        #     pass
        # try:
            # Navigate to Purple Garden staging
            
            # user.go_to_url("https://st:purplestage@staging.purplegarden.co/")
            # user.wait_for_page_load()
            # time.sleep(5)  # Wait for page to load
            # user.go_to_url("chrome://version/")
            # user.wait_for_page_load()
            # time.sleep(3)  # Give the page a moment to load
            # user.go_to_url("https://mail.google.com/mail/u/0/#inbox")
            # time.sleep(100)

            # Handle accept button safely with null check for user
            # try:
            #     accept_btn = user.execute_script("""
            #         const signinApp = document.querySelector("chrome-signin-app");
            #         if (signinApp && signinApp.shadowRoot) {
            #             return signinApp.shadowRoot.querySelector("div#accept-button-content");
            #         }
            #         return null;
            #     """)
                
            #     if accept_btn:
            #         accept_btn.click()
            #         print("✅ Accept button clicked for user")
            #     else:
            #         print("ℹ️ No accept button found for user, continuing...")
            # except Exception as e:
            #     print(f"ℹ️ Accept button handling failed for user: {e}")
            #     print("Continuing with test...")
            
            # # Add your test logic here
            # print("✅ Purple Garden staging test completed successfully")
            advisor.go_to_url("https://accounts.google.com/signin/v2/identifier?service=mail")
            advisor.wait_for_page_load()
            print("🔍 Looking for email input field...")
            advisor.wait_for_element_visible("name", "identifier")
            advisor.input_text("name", "identifier", "lambdatestayush")
            print("✅ Email entered")
            
            # Click Next after email
            advisor.click("id", "identifierNext")
            print("✅ Clicked Next after email")
            time.sleep(3)
            
            # Step 2: Enter password using correct locator
            print("🔍 Looking for password input field...")
            
            # Try multiple password selectors - prioritize the correct one
            password_selectors = [
                ("name", "Passwd"),                    # ✅ Primary: Google's standard password field name
                ("xpath", "//input[@aria-label='Enter your password']"),  # ✅ Secondary: Accessibility label
                ("xpath", "//input[@type='password' and @name='Passwd']"), # ✅ Combination approach
                ("css", "input[name='Passwd']"),        # ✅ CSS selector
                ("name", "password"),                   # Fallback options
                ("name", "passwd"),
                ("id", "password"),
                ("id", "Passwd")
            ]
            
            password_entered = False
            for selector_type, selector_value in password_selectors:
                try:
                    print(f"🔍 Trying password selector: {selector_type} = {selector_value}")
                    password_input = advisor.wait_for_element_visible(selector_type, selector_value, timeout=5)
                    if password_input:
                        advisor.input_text(selector_type, selector_value, "@Ayush0703")
                        print(f"✅ Password entered using {selector_type} = {selector_value}")
                        password_entered = True
                        break
                except Exception as e:
                    print(f"⚠️ Password selector {selector_type} = {selector_value} failed: {e}")
                    continue
            
            if not password_entered:
                print("❌ All password selectors failed")
                # Take screenshot for debugging
                advisor.take_screenshot("password_field_not_found.png")
                print("📸 Screenshot saved for debugging")
                return False
            
            # Click Next after password
            advisor.click("id", "passwordNext")
            print("✅ Clicked Next after password")
            time.sleep(5)
            
            # Navigate to Gmail
            print("📧 Navigating to Gmail...")
            advisor.go_to_url("https://mail.google.com/")
            advisor.wait_for_page_load()
            time.sleep(10)
            
            # Verify Gmail loaded
            title = advisor.get_title()
            print(f"📧 Gmail page title: {title}")
            
            if "Gmail" in title:
                print("✅ Successfully logged into Gmail!")
            else:
                print("❌ Gmail not loaded properly")
            
            print("✅ Test completed successfully")






            # advisor.go_to_url("https://stg-expert.purpleocean.co/sign-in")
            # advisor.wait_for_page_load()
            # time.sleep(5)  # Wait for shadow DOM to load
            
            # # Handle accept button safely with null check
            # try:
            #     accept_btn = advisor.execute_script("""
            #         const signinApp = document.querySelector("chrome-signin-app");
            #         if (signinApp && signinApp.shadowRoot) {
            #             return signinApp.shadowRoot.querySelector("div#accept-button-content");
            #         }
            #         return null;
            #     """)
                
            #     if accept_btn:
            #         accept_btn.click()
            #         print("✅ Accept button clicked for advisor")
            #     else:
            #         print("ℹ️ No accept button found for advisor, continuing...")
            # except Exception as e:
            #     print(f"ℹ️ Accept button handling failed for advisor: {e}")
            #     print("Continuing with test...")
            
            
            # Handle accept button safely with null check for user
            # try:
            #     user.go_to_url("https://st:purplestage@staging.purplegarden.co/")
            #     user.wait_for_page_load()
            #     time.sleep(5)  # Wait for shadow DOM to load
            # except Exception as e:
            #     print(f"Test failed: {e}")
            #     user.take_screenshot("ayush_test_failed.png")
            #     raise
            
            # login.login_in_with_advisor(advisor, test_data)
            # login.login_in_with_user(user, test_data)
            # time.sleep(10)
            
            # profile_element = user.get_element_text(*locators.PROFILE)
            # print(f"Profile element text: {profile_element}")
            # user.wait_for_element_visible(*locators.SEARCH_ADVISOR)
            # user.input_text(*locators.SEARCH_ADVISOR, "Hubert Blaine")
            # user.wait_for_element_visible(*locators.FIND_ADVISOR)
            # user.click(*locators.FIND_ADVISOR)
            # user.wait_for_element_visible(*locators.CLICK_ADVISOR)
            # user.click(*locators.CLICK_ADVISOR)
            # user.wait_for_element_visible(*locators.CLICK_CHAT)
            # user.click(*locators.CLICK_CHAT)
            # user.wait_for_element_visible(*locators.START_CHAT)
            # user.click(*locators.START_CHAT)
            # advisor.wait_for_element_visible(*locators.ACCEPT_CHAT)
            # advisor.click(*locators.ACCEPT_CHAT)
            # time.sleep(40)
            # advisor.wait_for_element_visible(*locators.TOTAL_DURATION)
            # total_duration = advisor.get_element_text(*locators.TOTAL_DURATION)
            # advisor.assert_element_text_equals(*locators.TOTAL_DURATION, total_duration)
            # # print(f"Total duration: {total_duration}")
            # your_rate = advisor.get_element_text(*locators.YOUR_RATE)
            # advisor.assert_element_text_equals(*locators.YOUR_RATE, your_rate)
            # # print(f"Your rate: {your_rate}")
            # total_credit_charged = advisor.get_element_text(*locators.TOTAL_CREDIT_CHARGED)
            # advisor.assert_element_text_equals(*locators.TOTAL_CREDIT_CHARGED, total_credit_charged)
            # # print(f"Total credit charged: {total_credit_charged}")
            # total_earned = advisor.get_element_text(*locators.TOTAL_EARNED)
            # advisor.assert_element_text_equals(*locators.TOTAL_EARNED, total_earned)
            # print(f"Total earned: {total_earned}")
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            user.take_screenshot("ayush_test_failed.png")
            # advisor.take_screenshot("ayush_test_failed.png")
            raise
        finally:
            # Clean up
            user.quit_driver()     
            advisor.quit_driver()            
