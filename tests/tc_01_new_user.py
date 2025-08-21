from drivers.web_driver import WebDriver
from locators.MixPanel.MixPanel import MixPanelLocators
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
from Modules.signup import Signup
from Modules.login import Login
import time
import random
import string

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_valid_login_web(self, web_advisor, web_user, test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        advisor = web_advisor
        user = web_user
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        mixpanel_locators = MixPanelLocators()
        signup = Signup()
        login = Login()

        
        try:
        
            login.login_in_with_advisor(advisor, test_data)
            signup.signup_with_user(user)
            time.sleep(10)

            # add_credit_card details
            # user.wait_for_element_visible(*user_web_locators.FIND_ADVISOR)
            # user.input_text(*user_web_locators.SEARCH_ADVISOR, "Hubert Blaine")
            # user.click(*user_web_locators.FIND_ADVISOR)
            # time.sleep(10)
            # user.click(*user_web_locators.CLICK_ADVISOR)
            # user.click(*user_web_locators.CLICK_CHAT)
            # user.click(*user_web_locators.START_CHAT)

            # profile_element = user.get_element_text(*user_web_locators.PROFILE)
            # print(f"Profile element text: {profile_element}")
            user.wait_for_element_visible(*user_web_locators.SEARCH_ADVISOR)
            user.input_text(*user_web_locators.SEARCH_ADVISOR, "Hubert Blaine")
            user.wait_for_element_visible(*user_web_locators.FIND_ADVISOR)
            time.sleep(10)
            user.click(*user_web_locators.FIND_ADVISOR)
            time.sleep(3)
            # user.wait_for_element_visible(*user_web_locators.CLICK_ADVISOR)
            # user.click(*user_web_locators.CLICK_ADVISOR)
            formatted_locator = (user_web_locators.CLICK_ADVISOR[0], 
                    user_web_locators.CLICK_ADVISOR[1].format(advisor_name="Hubert Blaine"))
            user.wait_for_element_visible(*formatted_locator)
            user.click(*formatted_locator)
            time.sleep(2)
            user.wait_for_element_visible(*user_web_locators.CLICK_CHAT)
            user.click(*user_web_locators.CLICK_CHAT)
            user.wait_for_element_visible(*user_web_locators.START_CHAT)
            user.click(*user_web_locators.START_CHAT)
            time.sleep(10)
            user.wait_for_element_visible(*user_web_locators.ADD_NEW_CREDIT_DEBIT_CARD)
            user.click(*user_web_locators.ADD_NEW_CREDIT_DEBIT_CARD)
            # cardDetails_Fill
            user.wait_for_document_loaded()
            time.sleep(5)
            user.wait_for_element_visible(*user_web_locators.CARD_HOLDER_NAME)
            user.input_text(*user_web_locators.CARD_HOLDER_NAME, test_data['creditcard']['card_holder_name'])
            # user.switch_to_frame(*user_web_locators.CARD_NUMBER_FRAME)
            user.switch_to_frame(0)
            user.input_text(*user_web_locators.CARD_NUMBER, test_data['creditcard']['card_number'])
            user.switch_to_default_content()
            # user.switch_to_frame(user_web_locators.EXPIRE_DATE_FRAME)
            user.switch_to_frame(1)
            user.input_text(*user_web_locators.EXPIRE_DATE, test_data['creditcard']['card_expire'])
            user.switch_to_default_content()
            # user.switch_to_frame(user_web_locators.CVC_FRAME)
            user.switch_to_frame(2)
            user.input_text(*user_web_locators.CVV, test_data['creditcard']['card_security_code'])
            user.switch_to_default_content()
            user.input_text(*user_web_locators.ZIP_CODE, test_data['creditcard']['postcode'])
            user.click(*user_web_locators.ADD_CARD_BUTTON)
            time.sleep(5)
            user.wait_for_element_visible(*user_web_locators.ADD_MIN_BALANCE_BUTTON)
            user.click(*user_web_locators.ADD_MIN_BALANCE_BUTTON)
            time.sleep(30)
            user.wait_for_element_visible(*user_web_locators.START_LIVE_CHAT_BUTTON)
            user.click(*user_web_locators.START_LIVE_CHAT_BUTTON)
            user.wait_for_element_visible(*user_web_locators.NICKNAME)
            user.input_text(*user_web_locators.NICKNAME, "monu")
            user.click(*user_web_locators.MALE_RADIO_BUTTON)
            user.input_text(*user_web_locators.DOB, "07031999")
            user.click(*user_web_locators.START_LIVE_CHAT_BUTTON)
            
            # User_Live_Chat
            user.wait_for_element_visible(*user_web_locators.TYPE_MESSAGE)
            user.input_text(*user_web_locators.TYPE_MESSAGE, "!@#$%^&*()_+😝😜🤪🤨")
            user.click(*user_web_locators.SEND)
            user.wait_for_element_visible(*user_web_locators.MESSAGE_TEXT)
            user.assert_element_contains_text(*user_web_locators.MESSAGE_TEXT, "!@#$%^&*()_+😝😜🤪🤨")
            time.sleep(5)
            advisor.assert_element_contains_text(*advisor_web_locators.MESSAGE_TEXT_FROM_USER, "!@#$%^&*()_+😝😜🤪🤨")
            advisor.wait_for_element_visible(*advisor_web_locators.TYPE_MESSAGE)
            advisor.input_text(*advisor_web_locators.TYPE_MESSAGE, "!@#$%^&*()_+😝😜🤪🤨")
            advisor.click(*advisor_web_locators.SEND)
            advisor.wait_for_element_visible(*advisor_web_locators.MESSAGE_TEXT)
            advisor.assert_element_contains_text(*advisor_web_locators.MESSAGE_TEXT, "!@#$%^&*()_+😝😜🤪🤨")
            user.assert_element_contains_text(*user_web_locators.MESSAGE_TEXT_FROM_ADVISOR, "!@#$%^&*()_+😝😜🤪🤨")
            time.sleep(180)
            user.click(*user_web_locators.HANG_UP_BUTTON)
            user.wait_for_element_visible(*user_web_locators.CONTINUE_BUTTON)
            user.click(*user_web_locators.CONTINUE_BUTTON)
            advisor.wait_for_element_visible(*advisor_web_locators.TOTAL_DURATION)
            total_duration =advisor.get_element_text(*advisor_web_locators.TOTAL_DURATION)
            your_rate = float(advisor.get_element_text(*advisor_web_locators.YOUR_RATE).split("$")[1].strip().split("/")[0])
            total_credit_charged = float(advisor.get_element_text(*advisor_web_locators.TOTAL_CREDIT_CHARGED).split("$")[1].strip())
            expected_total_earned = float(advisor.get_element_text(*advisor_web_locators.TOTAL_EARNED).split("$")[1].strip())
            expected_connection_fee = float(advisor.get_element_text(*advisor_web_locators.CONNECTION_FEE).split("$")[1].strip())
            expected_platform_fee = float(advisor.get_element_text(*advisor_web_locators.PLATFORM_FEE).split("$")[1].strip())




            advisor.wait_for_element_visible(*advisor_web_locators.ACCEPT_CHAT)
            advisor.click(*advisor_web_locators.ACCEPT_CHAT)
            time.sleep(40)
            # Wait a moment to see the result
            time.sleep(5)
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            raise
        finally:
            # Clean up
            user.quit_driver()
