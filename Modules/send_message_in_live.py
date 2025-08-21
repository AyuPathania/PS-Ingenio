from selenium.webdriver.common.by import By
# from locators.test.ayush_locator import AyushLocator
from locators.MixPanel.MixPanel import MixPanelLocators
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
import random
import time

class send_message_in_live:
    def send_message_in_live(self, web_user, web_advisor, test_data):
        user = web_user
        advisor = web_advisor
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        try:
            user.wait_for_element_visible(*user_web_locators.TYPE_MESSAGE)
            special_chars = "!@#$%^&*()_+{}[]|:;<>?,./~`"
            emojis = ["😝", "😜", "🤪", "🤨", "🔥", "❤️", "🚀", "😂", "🌟"]
            random_text = ''.join(random.choices(special_chars, k=5)) + random.choice(emojis)
            emoji_text = random_text.encode('unicode_escape').decode('utf-8')
            print(f"Random text with special characters and emojis: {emoji_text}")

            user.input_text(*user_web_locators.TYPE_MESSAGE, emoji_text)
            user.click(*user_web_locators.SEND)
            user.wait_for_element_visible(*user_web_locators.MESSAGE_TEXT)
            user.assert_element_contains_text(*user_web_locators.MESSAGE_TEXT, emoji_text)
            time.sleep(5)
            advisor.assert_element_contains_text(*advisor_web_locators.MESSAGE_TEXT_FROM_USER, emoji_text)
            advisor.wait_for_element_visible(*advisor_web_locators.TYPE_MESSAGE)
            advisor.input_text(*advisor_web_locators.TYPE_MESSAGE, emoji_text)
            advisor.click(*advisor_web_locators.SEND)
            advisor.wait_for_element_visible(*advisor_web_locators.MESSAGE_TEXT)
            advisor.assert_element_contains_text(*advisor_web_locators.MESSAGE_TEXT, emoji_text)
            user.assert_element_contains_text(*user_web_locators.MESSAGE_TEXT_FROM_ADVISOR, emoji_text)
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure

    def after_call_assertions(self, web_user, web_advisor, test_data):
        user = web_user
        advisor = web_advisor
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        try:
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


            
            # print(f"total_seconds: {total_seconds}")
            # print(f"total_earned: {total_earned}")
            # print(f"connection_fee: {connection_fee}")
            # print(f"platform_fee: {platform_fee}")
            # print(f"total_credit_charged: {total_credit_charged}")
            # print(f"your_rate: {your_rate}")
            # print(f"total_duration: {total_duration}")

            # assert float(total_cost) == total_credit_charged
            # assert float(connection_fee) == expected_connection_fee
            # assert float(total_earned) == expected_total_earned
            # assert float(platform_fee) == expected_platform_fee
            # Fixed assertions: compare floats with floats (no int conversion)
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