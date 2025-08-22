from drivers.web_driver import WebDriver
from locators.MixPanel.MixPanel import MixPanelLocators
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
from Modules.signup import Signup
from Modules.login import Login
from Modules.modules import Modules
from Modules.send_message_in_live import SendMessage
from Modules.credit_card import CreditCard
from Modules.your_details_form import DetailsForm
import time
import random
import string

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_valid_login_web(self, web_user, web_advisor, test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        advisor = web_advisor
        user = web_user
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        mixpanel_locators = MixPanelLocators()
        signup = Signup()
        login = Login()
        send_message_in_live = SendMessage()
        credit_card = CreditCard()
        details_form = DetailsForm()
        try:
            signup.signup_with_user(user)
            login.login_in_with_advisor(advisor, test_data)
            time.sleep(10)

            # add_credit_card details
            user.wait_for_element_visible(*user_web_locators.FIND_ADVISOR)
            user.input_text(*user_web_locators.SEARCH_ADVISOR, "tetsLanguageOrder")
            user.click(*user_web_locators.FIND_ADVISOR)
            formatted_locator = (user_web_locators.CLICK_ADVISOR[0], 
                    user_web_locators.CLICK_ADVISOR[1].format(advisor_name="tetsLanguageOrder"))
            user.wait_for_element_visible(*formatted_locator)
            user.click(*formatted_locator)
            user.wait_for_element_visible(*user_web_locators.CLICK_CHAT)
            user.click(*user_web_locators.CLICK_CHAT)
            user.wait_for_element_visible(*user_web_locators.START_CHAT)
            user.click(*user_web_locators.START_CHAT)
            time.sleep(10)
            credit_card.add_credit_card(user, test_data)


            user.wait_for_element_visible(*user_web_locators.START_LIVE_CHAT_BUTTON)
            user.click(*user_web_locators.START_LIVE_CHAT_BUTTON)

            details_form.your_details_form(user)
            
            user.click(*user_web_locators.START_LIVE_CHAT_BUTTON)
            advisor.wait_for_element_visible(*advisor_web_locators.ACCEPT_CHAT)
            advisor.click(*advisor_web_locators.ACCEPT_CHAT)
            time.sleep(250)
            #code for hang up
            user.wait_for_element_visible(*user_web_locators.HANG_UP_BUTTON)
            user.click(*user_web_locators.HANG_UP_BUTTON)      
            if user.is_element_displayed(*user_web_locators.CLOSE_POPUP_BUTTON):
                user.click(*user_web_locators.CLOSE_POPUP_BUTTON)
            if user.is_element_displayed(*user_web_locators.CLOSE_POPUP_AFTER_CALL):
                user.wait_for_element_visible(*user_web_locators.CLOSE_POPUP_AFTER_CALL)
                user.click(*user_web_locators.CLOSE_POPUP_AFTER_CALL)
            else:
                pass

            send_message_in_live.after_call_assertions(advisor)
            total_duration = user.get_element_text(*user_web_locators.TOTAL_DURATION)
            advisor_rate = float(user.get_element_text(*user_web_locators.ADVISOR_RATE).split("$")[1].strip().split("/")[0])
            total_credit_charged = float(user.get_element_text(*user_web_locators.TOTAL_CREDIT_CHARGED).split("$")[1].strip())

            minutes = int(total_duration.split(":")[1].strip())
            if total_duration.split(":")[2].strip().startswith("0"):
             seconds = int(total_duration.split(":")[2].strip()[-1])  # seconds = 7
            else:
                seconds = int(total_duration.split(":")[2].strip())
            total_seconds = (minutes * 60) + seconds

            total = total_seconds * advisor_rate / 60
            total_cost = "{:.2f}".format(int(total * 100) / 100)    

            try:
                assert float(total_cost) == float(total_credit_charged)
            except AssertionError:
                print(f"Assertion failed for total_cost: expected {total_credit_charged}, found {total_cost}")
                raise

            user.wait_for_element_visible(*user_web_locators.CONTINUE_BUTTON)
            user.click(*user_web_locators.CONTINUE_BUTTON)


            




        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            raise
        finally:
            # Clean up
            advisor.quit_driver()
            user.quit_driver()