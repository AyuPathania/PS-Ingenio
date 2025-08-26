import allure
from drivers.web_driver import WebDriver
from locators.MixPanel.MixPanel import MixPanelLocators
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
from Modules.signup import Signup
from Modules.login import Login
from Modules.send_message_in_live import SendMessage
from Modules.credit_card import CreditCard
from Modules.your_details_form import DetailsForm
import time
import re
import random
import string

@allure.epic("Ingenio Platform")
@allure.feature("Live Chat Functionality")
@allure.story("New User Live Chat Test")
class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    @allure.title("Test New User Live Chat with Message Types")
    @allure.description("Test complete flow from signup to live chat with various message types")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tc_01(self, web_user, web_advisor, test_data):
        
        """Test valid login on Web Advisor app using LambdaTest"""
        advisor = web_advisor
        user = web_user
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        signup = Signup()
        login = Login()
        send_message_in_live = SendMessage()
        credit_card = CreditCard()
        details_form = DetailsForm()
        status = "failed"

        with allure.step("Initialize test setup"):
            pass
        
        try:
            with allure.step("Perform user signup"):
                signup.signup_with_user(user)
                
            with allure.step("Login with advisor account"):
                login.login_in_with_advisor(advisor, test_data)
                time.sleep(10)

            with allure.step("Search and select advisor"):
                # add_credit_card details
                try:
                    user.wait_for_element_visible(*user_web_locators.FIND_ADVISOR)
                    user.input_text(*user_web_locators.SEARCH_ADVISOR, "tetsLanguageOrder")
                    user.click(*user_web_locators.FIND_ADVISOR)
                    formatted_locator = (user_web_locators.CLICK_ADVISOR[0], 
                            user_web_locators.CLICK_ADVISOR[1].format(advisor_name="tetsLanguageOrder"))
                    user.wait_for_element_visible(*formatted_locator)
                    user.click(*formatted_locator)
                except Exception as e:
                    allure.attach(f"Failed to find or click advisor element: {e}", "Error", allure.attachment_type.TEXT)
                    raise AssertionError(f"Advisor element not found or not clickable: {e}")
                
            with allure.step("Initiate chat session"):
                try:
                    user.click(*user_web_locators.CLICK_CHAT)
                    user.wait_for_element_visible(*user_web_locators.START_CHAT)
                    user.click(*user_web_locators.START_CHAT)
                    time.sleep(10)
                except Exception as e:
                    allure.attach(f"Failed to initiate chat session: {e}", "Error", allure.attachment_type.TEXT)
                    raise AssertionError(f"Chat session initiation failed: {e}")
                
            with allure.step("Add credit card details"):
                credit_card.add_credit_card(user, test_data)
                user.wait_for_element_visible(*user_web_locators.PAY_BUTTON)
                user.click(*user_web_locators.PAY_BUTTON)

            with allure.step("Start live chat"):
                user.wait_for_element_visible(*user_web_locators.START_LIVE_CHAT_BUTTON)
                user.click(*user_web_locators.START_LIVE_CHAT_BUTTON)

            with allure.step("Fill user details form"):
                details_form.your_details_form(user)

            with allure.step("Connect to live chat"):
                user.click(*user_web_locators.START_LIVE_CHAT_BUTTON)
                advisor.wait_for_element_visible(*advisor_web_locators.ACCEPT_CHAT)
                advisor.click(*advisor_web_locators.ACCEPT_CHAT)
                time.sleep(15)
                
            with allure.step("Test special character messages"):
                send_message_in_live.user_send_special_character_message_in_live(user)
                time.sleep(5)
                # special character assertion
                user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
                advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
                user_send_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
                result = re.sub(r'\n\d{1,2}:\d{2}', '', user_send_message)
                
                advisor_receive_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
                assert result == advisor_receive_message, f"Expected user message '{result}' to match advisor message '{advisor_receive_message}'"
                allure.attach(f"Special character message assertion passed. User: {result}, Advisor: {advisor_receive_message}", "Assertion Result", allure.attachment_type.TEXT)
                print("Special character message assertion passed.")
                
            with allure.step("Test advisor sending special character messages"):
                time.sleep(10)
                send_message_in_live.advisor_send_special_character_message_in_live(advisor)
                advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
                user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
                
                advisor_send_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
                user_receive_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
                result = re.sub(r'\n\d{1,2}:\d{2}', '', user_receive_message)
                assert advisor_send_message == result, f"Expected user message '{advisor_send_message}' to match advisor message '{result}'"
                allure.attach(f"Special character message assertion passed. Advisor: {advisor_send_message}, User: {result}", "Assertion Result", allure.attachment_type.TEXT)
                print("Special character message assertion passed.")

            with allure.step("Test short messages"):
                time.sleep(10)
                send_message_in_live.user_send_short_message_in_live(user)
                time.sleep(5)
                # short message assertion
                user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
                advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
                user_send_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
                result = re.sub(r'\n\d{1,2}:\d{2}', '', user_send_message)

                advisor_receive_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
                assert result == advisor_receive_message, f"Expected user message '{result}' to match advisor message '{advisor_receive_message}'"
                allure.attach(f"Short message assertion passed. User: {result}, Advisor: {advisor_receive_message}", "Assertion Result", allure.attachment_type.TEXT)
                print("Short message assertion passed.")

            with allure.step("Test advisor sending short messages"):
                time.sleep(10)
                send_message_in_live.advisor_send_short_message_in_live(advisor)
                time.sleep(5)
                advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
                user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
                
                advisor_send_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
                user_receive_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
                result = re.sub(r'\n\d{1,2}:\d{2}', '', user_receive_message)
                assert advisor_send_message == result, f"Expected user message '{advisor_send_message}' to match advisor message '{result}'"
                allure.attach(f"Short message assertion passed. Advisor: {advisor_send_message}, User: {result}", "Assertion Result", allure.attachment_type.TEXT)
                print("Short message assertion passed.")

            with allure.step("Test long messages"):
                time.sleep(10)
                send_message_in_live.user_send_Long_message_in_live(user)
                time.sleep(5)
                # long message assertion
                user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
                advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
                user_send_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
                result = re.sub(r'\n\d{1,2}:\d{2}', '', user_send_message)

                advisor_receive_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
                assert result == advisor_receive_message, f"Expected user message '{result}' to match advisor message '{advisor_receive_message}'"
                allure.attach(f"Long message assertion passed. User: {result}, Advisor: {advisor_receive_message}", "Assertion Result", allure.attachment_type.TEXT)
                print("Long message assertion passed.")

            with allure.step("Test advisor sending long messages"):
                time.sleep(10)
                send_message_in_live.advisor_send_Long_message_in_live(advisor)
                time.sleep(5)
                advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
                user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
                
                advisor_send_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
                user_receive_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
                result = re.sub(r'\n\d{1,2}:\d{2}', '', user_receive_message)
                assert advisor_send_message == result, f"Expected user message '{advisor_send_message}' to match advisor message '{result}'"
                allure.attach(f"Long message assertion passed. Advisor: {advisor_send_message}, User: {result}", "Assertion Result", allure.attachment_type.TEXT)
                print("Long message assertion passed.")

            with allure.step("Test emoji messages"):
                time.sleep(10)
                send_message_in_live.user_send_emojis_message_in_live(user)
                time.sleep(5)
                # emoji assertion
                user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
                advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
                user_send_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
                result = re.sub(r'\n\d{1,2}:\d{2}', '', user_send_message)
                
                advisor_receive_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
                assert result == advisor_receive_message, f"Expected user message '{result}' to match advisor message '{advisor_receive_message}'"
                allure.attach(f"Emoji message assertion passed. User: {result}, Advisor: {advisor_receive_message}", "Assertion Result", allure.attachment_type.TEXT)
                print("Emoji message assertion passed.")

            with allure.step("Test advisor sending emoji messages"):
                time.sleep(10)
                send_message_in_live.advisor_send_emojis_message_in_live(advisor)
                time.sleep(5)
                advisor.wait_for_element_visible(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
                user.wait_for_element_visible(*user_web_locators.USER_SEND_MESSAGE_TEXT)
                
                advisor_send_message = advisor.get_element_text(*advisor_web_locators.ADVISOR_SEND_MESSAGE_TEXT)
                user_receive_message = user.get_element_text(*user_web_locators.USER_SEND_MESSAGE_TEXT)
                result = re.sub(r'\n\d{1,2}:\d{2}', '', user_receive_message)
                assert advisor_send_message == result, f"Expected user message '{advisor_send_message}' to match advisor message '{result}'"
                allure.attach(f"Emoji message assertion passed. Advisor: {advisor_send_message}, User: {result}", "Assertion Result", allure.attachment_type.TEXT)
                print("Emoji message assertion passed.")

            with allure.step("Hang up the call from user side"):
                user.wait_for_element_clickable(*user_web_locators.HANG_UP_BUTTON)
                user.click(*user_web_locators.HANG_UP_BUTTON)

                if user.is_element_displayed(*user_web_locators.CLOSE_POPUP_BUTTON):
                    user.click(*user_web_locators.CLOSE_POPUP_BUTTON)


            with allure.step("Assertions after call"):
                send_message_in_live.after_call_assertions(advisor)
                status = "passed"

            with allure.step("Test completion"):
                # Wait a moment to see the result
                time.sleep(5)
                allure.attach("All message type tests completed successfully", "Test Status", allure.attachment_type.TEXT)
            
        except Exception as e:
            allure.attach(f"Test failed: {e}", "Error Details", allure.attachment_type.TEXT)
            print(f"Test failed: {e}")
            # Take screenshot on failure
            raise
        finally:
            with allure.step("Cleanup and driver quit"):
                user.execute_script(f"lambda-status={status}")
                advisor.execute_script(f"lambda-status={status}")                
                # Clean up
                user.quit_driver()
                advisor.quit_driver()

