from drivers.web_driver import WebDriver
from Modules.signup import Signup
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
from Modules.signup import Signup
from Modules.login import Login
from Modules.credit_card import CreditCard
import time
import json
import re
import random
import string

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_valid_login_web(self, web_user,web_advisor,test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        user = web_user
        advisor = web_advisor
        user_web_locators = UserWebLocators()
        # web_user_web_locators = AdvisorWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        login = Login()
        signup = Signup()
        credit_card = CreditCard()
        data = json.load(open('test_data.json'))
        promo_code = data['promocode'][0]

        
        try:
            
            signup.signup_with_user(user)
            login.login_in_with_advisor(advisor, test_data)
            user.wait_for_element_visible(*user_web_locators.SIDEMENU)
            user.wait_for_element_clickable(*user_web_locators.SIDEMENU)
            user.click(*user_web_locators.SIDEMENU)
            user.wait_for_element_clickable(*user_web_locators.SIDE_MENU_PAYMENT_METHOD)
            user.click(*user_web_locators.SIDE_MENU_PAYMENT_METHOD)
            
            credit_card.add_credit_card(user, test_data)
            # user.click(*user_web_locators.PAY_BUTTON)

            # apply_Promocode
            # user.click(*user_web_locators.HOME_PAGE)
            user.wait_for_page_load()
            user.wait_for_document_loaded()
            user.wait_for_element_visible(*user_web_locators.ADD_ANOTHER_PAYMENT_METHOD)
            user.wait_for_element_clickable(*user_web_locators.SIDEMENU)
            user.click(*user_web_locators.SIDEMENU)
            user.wait_for_element_clickable(*user_web_locators.SIDEMENU_APPLY_PROMOCODE)
            user.click(*user_web_locators.SIDEMENU_APPLY_PROMOCODE)
            user.input_text(*user_web_locators.SIDEMENU_PROMOCODE, promo_code)
            data['promocode'].pop(0)
            json.dump(data, open('test_data.json', 'w'), indent=2)
            user.wait_for_element_clickable(*user_web_locators.SIDEMENU_SUBMIT_BUTTON)
            user.click(*user_web_locators.SIDEMENU_SUBMIT_BUTTON)
            
            user.wait_for_element_visible(*user_web_locators.PROMOCODE_SUCCESS_MESSAGE)
            user.click(*user_web_locators.PROMOCODE_SUCCESS_MESSAGE)

            # add funds
            user.wait_for_element_clickable(*user_web_locators.SIDEMENU)
            user.click(*user_web_locators.SIDEMENU)
            user.wait_for_element_clickable(*user_web_locators.SIDE_MENU_ADD_FUNDS)
            user.click(*user_web_locators.SIDE_MENU_ADD_FUNDS)

            user.wait_for_element_visible(*user_web_locators.GET_20_CREDIT)
            Get_20_credit = user.get_element_text(*user_web_locators.GET_20_CREDIT)
            split_20_credit = re.search(r"\d+", Get_20_credit).group()
            print(split_20_credit)  # Output: 20

            # make this 20 to $20.00
            formatted_20_credit = "{:.2f}".format(float(split_20_credit))
            add_dollar_20 = (f"${formatted_20_credit}")  # Output: $20.00
            print(add_dollar_20)
            
            user.wait_for_element_clickable(*user_web_locators.GET_20_CREDIT)
            user.click(*user_web_locators.GET_20_CREDIT)
            
            # user.click(*user_web_locators.ACTUAL_AMOUNT)
            user.wait_for_element_visible(*user_web_locators.ACTUAL_AMOUNT)
            Actual_amount_text=user.get_element_text(*user_web_locators.ACTUAL_AMOUNT)

            


            try:
                assert add_dollar_20 == Actual_amount_text
            except AssertionError:
                print(f"Assertion failed for purchase credit: expected {Actual_amount_text}, found {add_dollar_20}")
                raise

            # make this $20.00 to Pay ($20.00)
            pay_20_credit = f"Pay (${formatted_20_credit})"
            print(pay_20_credit)  # Output: Pay ($20.00)
            # Output: Pay ($20.00)
            user.wait_for_element_visible(*user_web_locators.PAY_TEXT)
            Pay_Button_Text = user.get_element_text(*user_web_locators.PAY_TEXT)

            try:
                assert pay_20_credit == Pay_Button_Text
            except AssertionError:
                print(f"Assertion failed for pay button text: expected {Pay_Button_Text}, found {pay_20_credit}")
                raise

            user.wait_for_element_visible(*user_web_locators.PAY_BUTTON)
            user.click(*user_web_locators.PAY_BUTTON)
            user.wait_for_element_clickable(*user_web_locators.CONFIRM_BONUS_MESSAGE)
            user.click(*user_web_locators.CONFIRM_BONUS_MESSAGE)
            
            # Convert to float and add 10
            final_amount = float(split_20_credit) + 10
            # Format to 2 decimal places
            formatted_amount = "{:.2f}".format(final_amount)
            print(formatted_amount)  # Output: 30.00

            # add "$" sign in 30.00
            add_doller_sign=f"${formatted_amount}"
            print(add_doller_sign)

            user.wait_for_element_visible(*user_web_locators.CURRENT_BALANCE_TEXT)
            get_current_balance_text = user.get_element_text(*user_web_locators.CURRENT_BALANCE_TEXT)

            try:
                assert add_doller_sign == get_current_balance_text
            except AssertionError:
                print(f"Assertion failed for current balance: expected {add_doller_sign}, found {get_current_balance_text}")
                raise


                
            
            # Wait a moment to see the result
            time.sleep(5)
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            
            raise
        finally:
            # Clean up
            user.quit_driver()
