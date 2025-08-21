from selenium.webdriver.common.by import By
from locators.user.web_locators import UserWebLocators
from locators.MixPanel.MixPanel import MixPanelLocators
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
import random
import string

import time

class Modules:
    def login_in_with_user(self, web_user, test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        user = web_user
        user_web_locators = UserWebLocators()

        
        try:
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
            user.wait_for_element_visible(*user_web_locators.SIGN_IN)
            user.click(*user_web_locators.SIGN_IN)
            user.wait_for_element_visible(*user_web_locators.EMAIL)
            user.input_text(*user_web_locators.EMAIL, test_data['user']['valid_email'])
            user.wait_for_element_visible(*user_web_locators.PASSWORD)
            user.input_text(*user_web_locators.PASSWORD, test_data['user']['valid_password'])
            user.wait_for_element_visible(*user_web_locators.ACCEPT)
            user.click(*user_web_locators.ACCEPT)
            user.wait_for_element_visible(*user_web_locators.SIGN_IN_BUTTON)
            user.click(*user_web_locators.SIGN_IN_BUTTON)
            user.wait_for_page_load()
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            

    def login_in_with_advisor(self, web_advisor, test_data):
   
        advisor = web_advisor
        advisor_web_locators = AdvisorWebLocators()

        try:
            advisor.go_to_url("https://stg-expert.purpleocean.co/sign-in")
            advisor.wait_for_page_load()
            advisor.wait_for_element_visible(*advisor_web_locators.EMAIL_ADVISOR)
            advisor.input_text(*advisor_web_locators.EMAIL_ADVISOR, test_data['advisor']['valid_email'])
            advisor.wait_for_element_visible(*advisor_web_locators.PASSWORD_ADVISOR)
            advisor.input_text(*advisor_web_locators.PASSWORD_ADVISOR, test_data['advisor']['valid_password'])
            advisor.click(*advisor_web_locators.SIGN_IN_BUTTON_ADVISOR)
            # advisor.wait_for_element_visible(*locators.ALLOW_NOTIFICATIONS)
            # advisor.click(*locators.ALLOW_NOTIFICATIONS)
            # time.sleep(30)
            #advisor.switch_to.alert.accept()
            # advisor.handle_alert()
            advisor.wait_for_element_visible(*advisor_web_locators.PROFILE_ADVISOR)
            time.sleep(30)
            advisor.click(*advisor_web_locators.AWAY_ADVISOR)
            advisor.wait_for_element_visible(*advisor_web_locators.AVAILABLE_ADVISOR)
            advisor.click(*advisor_web_locators.AVAILABLE_ADVISOR)

        except Exception as e:
            print(f"Test failed: {e}")

    def send_message_in_live(self, web_user, web_advisor, test_data):
        user = web_user
        advisor = web_advisor
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        try:
            user.wait_for_element_visible(*user_web_locators.TYPE_MESSAGE)
            user.input_text(*user_web_locators.TYPE_MESSAGE, "Hello from user")
            user.click(*user_web_locators.SEND)
            user.wait_for_element_visible(*user_web_locators.MESSAGE_TEXT)
            user.assert_element_contains_text(*user_web_locators.MESSAGE_TEXT, "Hello from user")
            time.sleep(5)
            advisor.assert_element_contains_text(*advisor_web_locators.MESSAGE_TEXT_FROM_USER, "Hello from user")
            advisor.wait_for_element_visible(*advisor_web_locators.TYPE_MESSAGE)
            advisor.input_text(*advisor_web_locators.TYPE_MESSAGE, "Hello from advisor")
            advisor.click(*advisor_web_locators.SEND)
            advisor.wait_for_element_visible(*advisor_web_locators.MESSAGE_TEXT)
            advisor.assert_element_contains_text(*advisor_web_locators.MESSAGE_TEXT, "Hello from advisor")
            user.assert_element_contains_text(*user_web_locators.MESSAGE_TEXT_FROM_ADVISOR, "Hello from advisor")
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure

    def after_call_assertions(self, web_user, web_advisor):
        user = web_user
        advisor = web_advisor
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        try:
            user.click(*user_web_locators.HANG_UP_BUTTON)
            user.wait_for_element_visible(*user_web_locators.CLOSE_POPUP_BUTTON)
            user.click(*user_web_locators.CLOSE_POPUP_BUTTON)
            user.wait_for_element_visible(*user_web_locators.CONTINUE_BUTTON)
            user.click(*user_web_locators.CONTINUE_BUTTON)
            advisor.wait_for_element_visible(*advisor_web_locators.TOTAL_DURATION)
            total_duration =advisor.get_element_text(*advisor_web_locators.TOTAL_DURATION)
            your_rate = float(advisor.get_element_text(*advisor_web_locators.YOUR_RATE).split("$")[1].strip().split("/")[0])
            total_credit_charged = float(advisor.get_element_text(*advisor_web_locators.TOTAL_CREDIT_CHARGED).split("$")[1].strip())
            expected_total_earned = float(advisor.get_element_text(*advisor_web_locators.TOTAL_EARNED).split("$")[1].strip())
            expected_connection_fee = float(advisor.get_element_text(*advisor_web_locators.CONNECTION_FEE).split("$")[1].strip())
            expected_platform_fee = float(advisor.get_element_text(*advisor_web_locators.PLATFORM_FEE).split("$")[1].strip())


            minutes = int(total_duration.split(":")[1].strip())
            if total_duration.split(":")[2].strip().startswith("0"):
             seconds = int(total_duration.split(":")[2].strip()[-1])  # seconds = 7
            else:
                seconds = int(total_duration.split(":")[2].strip())
            total_seconds = (minutes * 60) + seconds

            # Calculate total cost
            total = total_seconds * your_rate / 60
            total_cost = "{:.2f}".format(int(total * 100) / 100)
            print(f"Calculated total_cost: {total_cost}")

            # Calculate connection fee
            connection = (0.36/60) * total_seconds
            connection_fee = "{:.2f}".format(int(connection * 100) / 100)
            print(f"Calculated connection_fee: {connection_fee}")

            # Calculate total earned
            total_calc = (((your_rate/60) * total_seconds) - (int(connection * 100) / 100)) * 0.36
            total_earned = "{:.2f}".format(int(total_calc * 100) / 100)
            print(f"Calculated total_earned: {total_earned}")

            # Calculate platform fee: (total_cost - connection_fee) - total_earned
            platform_fee_calc = (float(total_cost) - float(connection_fee)) - float(total_earned)
            platform_fee = "{:.2f}".format(int(platform_fee_calc * 100) / 100)
            print(f"Calculated platform_fee: {platform_fee}")
            
            print(f"Duration: {total_duration} ({total_seconds} seconds)")
            print(f"Rate: ${your_rate}/min")

            try:
                assert float(total_cost) == float(total_credit_charged)
            except AssertionError:
                print(f"Assertion failed for total_cost: expected {total_credit_charged}, found {total_cost}")
                raise
            
            try:
                assert float(connection_fee) == float(expected_connection_fee)
            except AssertionError:
                print(f"Assertion failed for connection_fee: expected {expected_connection_fee}, found {connection_fee}")
                raise
            
            try:
                assert float(total_earned) == float(expected_total_earned)
            except AssertionError:
                print(f"Assertion failed for total_earned: expected {expected_total_earned}, found {total_earned}")
                raise
            
            try:
                assert float(platform_fee) == float(expected_platform_fee)
            except AssertionError:
                print(f"Assertion failed for platform_fee: expected {expected_platform_fee}, found {platform_fee}")
                raise
            
            print("✅ All financial assertions passed in send_message_in_live!")
            # advisor.assert_element_contains_text(*advisor_web_locators.TOTAL_DURATION, total_duration)
            # advisor.assert_element_contains_text(*advisor_web_locators.YOUR_RATE, your_rate)
            # advisor.assert_element_contains_text(*advisor_web_locators.TOTAL_CREDIT_CHARGED, total_credit_charged)
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure


    def signup_with_user(self, web_user):
        """Test valid signup on Web user using LambdaTest"""
        user = web_user
        user_web_locators = UserWebLocators()
        
        
        try:
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


        except Exception as e:
                print(f"Test failed: {e}")
                # Take screenshot on failure