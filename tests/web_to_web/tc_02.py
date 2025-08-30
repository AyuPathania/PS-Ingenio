from drivers.web_driver import WebDriver
from locators.MixPanel.MixPanel import MixPanelLocators
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
from Modules.login import Login
import allure
import time

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    @allure.title("Test Existing User Live Chat")
    @allure.description("Test complete flow from login to live chat")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tc_02(self, web_advisor, web_user, test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        advisor = web_advisor
        user = web_user
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        mixpanel_locators = MixPanelLocators()
        login = Login()   
        status = "failed"
        advisor_name = test_data['advisor']['Hubert']['name']
        advisor_email = test_data['advisor']['Hubert']['email']
        advisor_password = test_data['advisor']['Hubert']['password']
        user_email = test_data['user']['tc_02']['email']
        user_password = test_data['user']['tc_02']['password']
        
        with allure.step("Initialize test setup"):
            pass
        
        try:
            with allure.step("Login with advisor account"):
                login.login_in_with_advisor(advisor, advisor_email, advisor_password)
                time.sleep(10)

            with allure.step("Login with user account"):
                login.login_in_with_user(user, user_email, user_password)
                time.sleep(10)
            
            with allure.step("Search and select advisor"):
                try:
                    user.wait_for_element_visible(*user_web_locators.SEARCH_ADVISOR)
                    user.wait_for_element_visible(*user_web_locators.FIND_ADVISOR)
                    user.input_text(*user_web_locators.SEARCH_ADVISOR, advisor_name)
                    user.click(*user_web_locators.FIND_ADVISOR)
                    formatted_locator = (user_web_locators.CLICK_ADVISOR[0], 
                            user_web_locators.CLICK_ADVISOR[1].format(advisor_name=advisor_name))
                    user.wait_for_element_visible(*formatted_locator)
                    user.click(*formatted_locator)
                    user.wait_for_element_visible(*user_web_locators.CLICK_CHAT)
                    user.click(*user_web_locators.CLICK_CHAT)
                except Exception as e:
                    allure.attach(f"Failed to search and select advisor: {e}", "Error", allure.attachment_type.TEXT)
                    raise AssertionError(f"Failed to search and select advisor: {e}")

            with allure.step("Verify amount before payment"):
                try:
                    time.sleep(5)
                    if  user.is_element_displayed(*user_web_locators.AMOUNT_BEFORE_PAYMENT_PRICE):
                        amount_before_payment=user.get_element_text(*user_web_locators.AMOUNT_BEFORE_PAYMENT_PRICE)
                    elif user.is_element_displayed(*user_web_locators.AMOUNT_BEFORE_PAYMENT_PRICE_ON_CHAT):
                        user.click(*user_web_locators.FORWARD_BUTTON)
                        time.sleep(5)
                    else:
                        amount_before_payment=user.get_element_text(*user_web_locators.AMOUNT_BEFORE_PAYMENT_SALES)
                except Exception as e:
                    allure.attach(f"Failed to verify amount before payment: {e}", "Error", allure.attachment_type.TEXT)
                    raise AssertionError(f"Failed to verify amount before payment: {e}")

            with allure.step("Start chat"):
                try:
                    user.wait_for_element_visible(*user_web_locators.START_CHAT)
                    user.click(*user_web_locators.START_CHAT)
                except Exception as e:
                    allure.attach(f"Failed to start chat: {e}", "Error", allure.attachment_type.TEXT)
                    raise AssertionError(f"Failed to start chat: {e}")

            with allure.step("Verify amount before payment"):
                try:
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
                    status = "passed"
                except Exception as e:
                    allure.attach(f"Failed to verify amount before payment: {e}", "Error", allure.attachment_type.TEXT)
                    raise AssertionError(f"Failed to verify amount before payment: {e}")

        except Exception as e:
            allure.attach(f"Test failed: {e}", "Error Details", allure.attachment_type.TEXT)
            print(f"Test failed: {e}")
            # Take screenshot on failure

        finally:
            with allure.step("Cleanup and driver quit"):
                advisor.execute_script(f"lambda-status={status}")
                user.execute_script(f"lambda-status={status}")                
                # Clean up
                advisor.quit_driver()
                user.quit_driver()
