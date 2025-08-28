from drivers.web_driver import WebDriver
from Modules.signup import Signup
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
from Modules.signup import Signup
from Modules.login import Login
from Modules.send_message_in_live import SendMessage
import time
import json
import re
import random
import string

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality using WebDriver"""
    
    def test_tc_08(self, web_user,web_advisor,test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        user = web_user
        advisor = web_advisor
        user_web_locators = UserWebLocators()
        send_message_in_live_chat = SendMessage()
        advisor_web_locators = AdvisorWebLocators()
        login = Login()
        status = "failed"
        
        

        
        try:
            
            login.login_in_with_user(user, "tc08@lt.com", "test123")
            login.login_in_with_advisor(advisor, test_data)

            user.wait_for_element_clickable(*user_web_locators.PROFILE)
            user.click(*user_web_locators.PROFILE)
            user.wait_for_element_clickable(*user_web_locators.SETTING_BUTTON_ON_PROFILE)
            user.click(*user_web_locators.SETTING_BUTTON_ON_PROFILE)
            user.wait_for_element_clickable(*user_web_locators.USER_ID)
            user_id = user.get_element_text(*user_web_locators.USER_ID)
            print(user_id)
            advisor.wait_for_element_clickable(*advisor_web_locators.SEARCH_USER_ID)
            advisor.input_text(*advisor_web_locators.SEARCH_USER_ID, user_id)
            advisor.press_enter(*advisor_web_locators.SEARCH_USER_ID)
            advisor.wait_for_element_clickable(*advisor_web_locators.SEARCH_RESULT_TEXT)
            advisor.wait_for_element_clickable(*advisor_web_locators.CLIENT_ID)
            client_id_on_advisor = advisor.get_element_text(*advisor_web_locators.CLIENT_ID)
            assert client_id_on_advisor == user_id, "User ID not found in the search results"
            advisor.wait_for_element_clickable(*advisor_web_locators.COUPON_BUTTON)
            advisor.click(*advisor_web_locators.COUPON_BUTTON)
            advisor.wait_for_element_clickable(*advisor_web_locators.SELECTED_COUPON)
            coupon_text = advisor.get_element_text(*advisor_web_locators.SELECTED_COUPON)
            print("coupon_text: ",coupon_text)
            coupon_discount = coupon_text.split("%")[0].strip()
            print("coupon_discount: ",coupon_discount)
            coupon_off = coupon_text.split("your next session")[0].strip()
            print("coupon_off: ",coupon_off)
            advisor.wait_for_element_clickable(*advisor_web_locators.SEND_COUPON_BUTTON)
            advisor.click(*advisor_web_locators.SEND_COUPON_BUTTON)
            user.wait_for_element_clickable(*user_web_locators.HOME_PAGE)
            user.click(*user_web_locators.HOME_PAGE)
            user.wait_for_element_clickable(*user_web_locators.PROFILE)
            user.click(*user_web_locators.PROFILE)
            user.wait_for_element_visible(*user_web_locators.FIND_ADVISOR)
            user.input_text(*user_web_locators.SEARCH_ADVISOR, "Hubert Blaine")
            user.click(*user_web_locators.FIND_ADVISOR)
            formatted_locator = (user_web_locators.CLICK_ADVISOR[0], 
                    user_web_locators.CLICK_ADVISOR[1].format(advisor_name="Hubert Blaine"))
            user.wait_for_element_visible(*formatted_locator)
            user.click(*formatted_locator)
            user.wait_for_element_visible(*user_web_locators.COUPON_TEXT_ON_USER_SIDE)
            coupon_text_on_user_side = user.get_element_text(*user_web_locators.COUPON_TEXT_ON_USER_SIDE)
            assert coupon_text_on_user_side == coupon_off, f"expected value is {coupon_off} but got {coupon_text_on_user_side}"
            user.wait_for_element_visible(*user_web_locators.ACTUAL_PRICE)
            actual_price = user.get_element_text(*user_web_locators.ACTUAL_PRICE)
            actual_price = float(actual_price.split("/")[0].strip().replace("$", ""))
            print("actual_price: ",actual_price)
            user.wait_for_element_visible(*user_web_locators.DISCOUNTED_PRICE)
            discounted_price = user.get_element_text(*user_web_locators.DISCOUNTED_PRICE)
            print("discounted_price: ",discounted_price)
            discount = float(coupon_discount)/100
            discounted_price_on_user_side = round(actual_price * (1 - discount), 2)
            discounted_price_on_user_side = f"${discounted_price_on_user_side:.2f}/min"
            assert discounted_price_on_user_side == discounted_price, f"expected value is {discounted_price} but got {discounted_price_on_user_side}"
            user.wait_for_element_visible(*user_web_locators.CLICK_CHAT)
            user.click(*user_web_locators.CLICK_CHAT)
            user.wait_for_element_visible(*user_web_locators.MINUTES_TEXT)
            while True:
                minute_text = user.get_element_text(*user_web_locators.MINUTES_TEXT)
                if minute_text == "1":
                    user.click(*user_web_locators.START_CHAT)
                    break
                else:
                    user.click(*user_web_locators.BACK_BUTTON)
                    user.get_element_text(*user_web_locators.MINUTES_TEXT)
            advisor.wait_for_element_visible(*advisor_web_locators.ACCEPT_CHAT)
            advisor.click(*advisor_web_locators.ACCEPT_CHAT)
            time.sleep(15)
            user.wait_for_element_visible(*user_web_locators.CHAT_DISCOUNT_TEXT)
            chat_discount_text = user.get_element_text(*user_web_locators.CHAT_DISCOUNT_TEXT)
            print("chat_discount_text: ",chat_discount_text)
            print("coupon_off: ",coupon_off)
            assert chat_discount_text.lower() == (f"Advisor special offer applied: {coupon_off}.").lower(), f"expected value is \"Advisor special offer applied: {coupon_off}.\" but got {chat_discount_text}"
            time.sleep(60)
            user.wait_for_element_clickable(*user_web_locators.ADD_CHAT_TIME)
            while True:
                minute_text = user.get_element_text(*user_web_locators.MINUTES_TEXT)
                if minute_text == "1":
                    user.click(*user_web_locators.ADD_CHAT_TIME)
                    break
                else:
                    user.click(*user_web_locators.BACK_BUTTON)
                    user.wait_for_element_visible(*user_web_locators.MINUTES_TEXT)
            assert chat_discount_text.lower() == f"Advisor special offer applied: {coupon_off}.".lower(), f"expected value is \"Advisor special offer applied: {coupon_off}.\" but got {chat_discount_text}"
            time.sleep(70)
            
            




            user.wait_for_element_clickable(*user_web_locators.CALL_END)
            user.click(*user_web_locators.CALL_END)
            user.wait_for_element_clickable(*user_web_locators.CLOSE_POPUP_AFTER_CALL)
            user.click(*user_web_locators.CLOSE_POPUP_AFTER_CALL)
            #assertions after call on user side
            user.wait_for_element_visible(*user_web_locators.YOUR_RATE)
            call_rate= user.get_element_text(*user_web_locators.YOUR_RATE)
            your_rate = float(call_rate.replace("$", ""))
            print("Advisor fee per minute is: ",your_rate)  # Output: 0.99
            user.wait_for_element_visible(*user_web_locators.TOTAL_DURATION)
            time_str = user.get_element_text(*user_web_locators.TOTAL_DURATION)
            # Split into hours, minutes, and seconds
            h, m, s = map(int, time_str.split(":"))
            # Convert to total seconds
            total_seconds_digit = h * 3600 + m * 60 + s
            # Assert to validate the conversion
            print("Duration of the call is: ",total_seconds_digit)
            user.wait_for_element_visible(*user_web_locators.SUBTOTAL_PRICE)
            subtotal_cost = user.get_element_text(*user_web_locators.SUBTOTAL_PRICE)
            total = total_seconds_digit * your_rate / 60
            total_cost = "{:.2f}".format(int(total * 100) / 100)
            print(f"Subtotal price is: {total_cost}")

            user.wait_for_element_visible(*user_web_locators.TOTAL_PAY)
            final_pay = user.get_element_text(*user_web_locators.TOTAL_PAY)
            changed_value= float(total_cost)
            user.wait_for_element_visible(*user_web_locators.DISCOUNT_ON_COUPON_TEXT)
            discount_on_coupon_text = user.get_element_text(*user_web_locators.DISCOUNT_ON_COUPON_TEXT)
            discounted_pay = "{:.2f}".format((changed_value * (1 - discount)))
            discount = changed_value - float(discounted_pay)
            discount = round(discount, 2)
            total = user.get_element_text(*user_web_locators.TOTAL_CREDIT_CHARGED).split("$")[1]
            expected_total = round(round(float(total_cost), 2) - discount, 2)
            assert total == str(expected_total), f"expected value is {expected_total} but got {total}"
            assert discount_on_coupon_text == f"-${discount}", f"expected value is {discount} but got {discount_on_coupon_text}"
            expected_credit_charged_from_advisor = advisor.get_element_text(*advisor_web_locators.TOTAL_CREDIT_CHARGED)
            assert expected_credit_charged_from_advisor == final_pay, f"expected value is for final pay is {final_pay} but got {expected_credit_charged_from_advisor}"
            send_message_in_live_chat.after_call_assertions(advisor)







            status = "passed"







            




        except Exception as e:
            print(f"Test failed: {e}")
            user.wait_for_element_clickable(*user_web_locators.HANG_UP_BUTTON)
            user.click(*user_web_locators.HANG_UP_BUTTON)
            # Take screenshot on failure
            
            raise
        finally:
            user.execute_script(f"lambda-status={status}")
            advisor.execute_script(f"lambda-status={status}")             
            # Clean up
            user.quit_driver()
            advisor.quit_driver()
