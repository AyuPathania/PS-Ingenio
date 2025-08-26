from selenium.webdriver.common.by import By
# from locators.test.ayush_locator import AyushLocator
# from locators.MixPanel.MixPanel import MixPanelLocators
from locators.locator_factory import LocatorFactory

import time

class CreditCard:
    
    def add_credit_card(self, web_user, test_data):
        """Test valid login on Web Advisor app using LambdaTest"""
        user = web_user
        user_web_locators = LocatorFactory.get_user_web_locators()

        
        try:
            user.wait_for_element_visible(*user_web_locators.ADD_NEW_CREDIT_DEBIT_CARD)
            user.click(*user_web_locators.ADD_NEW_CREDIT_DEBIT_CARD)
            
            time.sleep(10)
            # Wait for card holder name field to be clickable (not just visible)
            user.wait_for_element_clickable(*user_web_locators.CARD_HOLDER_NAME)
            user.input_text(*user_web_locators.CARD_HOLDER_NAME, test_data['creditcard']['card_holder_name'])
            
            # Switch to card number iframe and input card number
            card_number_frame = user.find_element(*user_web_locators.CARD_NUMBER_FRAME)
            user.switch_to_frame(card_number_frame)
            user.input_text(*user_web_locators.CARD_NUMBER, test_data['creditcard']['card_number'])
            user.switch_to_default_content()
            
            # Switch to expire date iframe and input expiry date
            expire_date_frame = user.find_element(*user_web_locators.EXPIRE_DATE_FRAME)
            user.switch_to_frame(expire_date_frame)
            user.input_text(*user_web_locators.EXPIRE_DATE, test_data['creditcard']['card_expire'])
            user.switch_to_default_content()
            
            # Switch to CVC iframe and input CVC
            cvc_frame = user.find_element(*user_web_locators.CVC_FRAME)
            user.switch_to_frame(cvc_frame)
            user.input_text(*user_web_locators.CVV, test_data['creditcard']['card_security_code'])
            user.switch_to_default_content()
            
            user.input_text(*user_web_locators.ZIP_CODE, test_data['creditcard']['postcode'])            
            user.click(*user_web_locators.ADD_CARD_BUTTON)
            # user.wait_for_element_visible(*user_web_locators.PAY_BUTTON)
            # user.click(*user_web_locators.PAY_BUTTON)
           
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure

            
            
