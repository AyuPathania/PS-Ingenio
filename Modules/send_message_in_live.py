from selenium.webdriver.common.by import By
# from locators.test.ayush_locator import AyushLocator
from locators.MixPanel.MixPanel import MixPanelLocators
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
import random
import time

class SendMessage:
    def send_special_character_message_in_live(self, web_user, web_advisor):
        user = web_user
        advisor = web_advisor
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        try:
            user.wait_for_element_visible(*user_web_locators.TYPE_MESSAGE)

            # user.input_text(*user_web_locators.TYPE_MESSAGE, random_text)
            user.execute_script("""
    try {
        var special_chars = "!@#$%^&*()_+[]|:;<>?,./~";
        var textarea = document.evaluate(
            "//textarea[@class='chatSendArea--vzCQ5']",
            document,
            null,
            XPathResult.FIRST_ORDERED_NODE_TYPE,
            null
        ).singleNodeValue;
        if (textarea) {
            // Create a native setter for value so React/Angular detects it
            var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
            nativeInputValueSetter.call(textarea, special_chars);
            // Dispatch input & change events
            textarea.dispatchEvent(new Event('input', { bubbles: true }));
            textarea.dispatchEvent(new Event('change', { bubbles: true }));
            console.log("✅ Text inserted properly:", special_chars);
        } else {
            console.log("❌ Textarea not found!");
        }
    } catch(e) {
        console.log("⚠️ Error:", e);
    }
""")
            user.input_text_without_clear(*user_web_locators.TYPE_MESSAGE, "ab")
            time.sleep(5)
            user.click(*user_web_locators.SEND)

            user.wait_for_element_visible(*user_web_locators.MESSAGE_TEXT)
            user.assert_element_contains_text(*user_web_locators.MESSAGE_TEXT, "!@#$%^&*()_+[]|:;<>?,./~ab")
            time.sleep(5)
            advisor.assert_element_contains_text(*advisor_web_locators.MESSAGE_TEXT_FROM_USER, "!@#$%^&*()_+[]|:;<>?,./~ab")
            advisor.wait_for_element_visible(*advisor_web_locators.TYPE_MESSAGE)

            advisor.execute_script("""
    try {
        var special_chars = "!@#$%^&*()_+[]|:;<>?,./~";
        // Locate textarea by its class using XPath
        var textarea = document.evaluate(
            "//textarea[contains(@class,'input-expert-message')]",
            document,
            null,
            XPathResult.FIRST_ORDERED_NODE_TYPE,
            null
        ).singleNodeValue;
        if (textarea) {
            // Use the native setter so React/Angular/Vue detect the change
            var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
            nativeInputValueSetter.call(textarea, special_chars);
            // Trigger input and change events to notify the framework
            textarea.dispatchEvent(new Event('input', { bubbles: true }));
            textarea.dispatchEvent(new Event('change', { bubbles: true }));
            console.log("✅ Text inserted properly:", special_chars);
        } else {
            console.log("❌ Textarea not found!");
        }
    } catch(e) {
        console.log("⚠️ Error inserting text:", e);
    }
""")
            advisor.input_text_without_clear(*advisor_web_locators.TYPE_MESSAGE, "abcd")
            advisor.click(*advisor_web_locators.SEND)
            advisor.wait_for_element_visible(*advisor_web_locators.MESSAGE_TEXT)
            advisor.assert_element_contains_text(*advisor_web_locators.MESSAGE_TEXT, "!@#$%^&*()_+[]|:;<>?,./~abcd")
            user.assert_element_contains_text(*user_web_locators.MESSAGE_TEXT_FROM_ADVISOR, "!@#$%^&*()_+[]|:;<>?,./~abcd")
        except Exception as e:
            print(f"Test failed: {e}")

            # send short_message
    def send_short_message_in_live(self, web_user, web_advisor):
        user = web_user
        advisor = web_advisor
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        try:
            user.wait_for_element_visible(*user_web_locators.TYPE_MESSAGE)

            # user.input_text(*user_web_locators.TYPE_MESSAGE, random_text)
            short_message = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."
            user.input_text(*user_web_locators.TYPE_MESSAGE, short_message)
            time.sleep(5)
            user.click(*user_web_locators.SEND)

            user.wait_for_element_visible(*user_web_locators.MESSAGE_TEXT)
            user.assert_element_contains_text(*user_web_locators.MESSAGE_TEXT, short_message)
            time.sleep(5)
            advisor.assert_element_contains_text(*advisor_web_locators.MESSAGE_TEXT_FROM_USER, short_message)
            advisor.wait_for_element_visible(*advisor_web_locators.TYPE_MESSAGE)


            advisor.input_text(*advisor_web_locators.TYPE_MESSAGE, short_message)
            advisor.click(*advisor_web_locators.SEND)
            advisor.wait_for_element_visible(*advisor_web_locators.MESSAGE_TEXT)
            advisor.assert_element_contains_text(*advisor_web_locators.MESSAGE_TEXT, short_message)
            user.assert_element_contains_text(*user_web_locators.MESSAGE_TEXT_FROM_ADVISOR, short_message)
        except Exception as e:
            print(f"Test failed: {e}")

            # send long_message
    def send_Long_message_in_live(self, web_user, web_advisor):
        user = web_user
        advisor = web_advisor
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        try:
            user.wait_for_element_visible(*user_web_locators.TYPE_MESSAGE)

            # user.input_text(*user_web_locators.TYPE_MESSAGE, random_text)
            long_message = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32."
            user.input_text(*user_web_locators.TYPE_MESSAGE, long_message)
            time.sleep(5)
            user.click(*user_web_locators.SEND)

            user.wait_for_element_visible(*user_web_locators.MESSAGE_TEXT)
            user.assert_element_contains_text(*user_web_locators.MESSAGE_TEXT, long_message)
            time.sleep(5)
            advisor.assert_element_contains_text(*advisor_web_locators.MESSAGE_TEXT_FROM_USER, long_message)
            advisor.wait_for_element_visible(*advisor_web_locators.TYPE_MESSAGE)

            
            advisor.input_text(*advisor_web_locators.TYPE_MESSAGE, long_message)
            advisor.click(*advisor_web_locators.SEND)
            advisor.wait_for_element_visible(*advisor_web_locators.MESSAGE_TEXT)
            advisor.assert_element_contains_text(*advisor_web_locators.MESSAGE_TEXT, long_message)
            user.assert_element_contains_text(*user_web_locators.MESSAGE_TEXT_FROM_ADVISOR, long_message)
        except Exception as e:
            print(f"Test failed: {e}")

            # send emojis
    def send_emojis_message_in_live(self, web_user, web_advisor):
        user = web_user
        advisor = web_advisor
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        try:
            user.wait_for_element_visible(*user_web_locators.TYPE_MESSAGE)

            # user.input_text(*user_web_locators.TYPE_MESSAGE, random_text)
            user.execute_script("""
    try {
        var special_chars = "😝😜🦄🐍🐙🦊🐼";
        var textarea = document.evaluate(
            "//textarea[@class='chatSendArea--vzCQ5']",
            document,
            null,
            XPathResult.FIRST_ORDERED_NODE_TYPE,
            null
        ).singleNodeValue;
        if (textarea) {
            // Create a native setter for value so React/Angular detects it
            var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
            nativeInputValueSetter.call(textarea, special_chars);
            // Dispatch input & change events
            textarea.dispatchEvent(new Event('input', { bubbles: true }));
            textarea.dispatchEvent(new Event('change', { bubbles: true }));
            console.log("✅ Text inserted properly:", special_chars);
        } else {
            console.log("❌ Textarea not found!");
        }
    } catch(e) {
        console.log("⚠️ Error:", e);
    }
""")
            user.input_text_without_clear(*user_web_locators.TYPE_MESSAGE, "ab")
            time.sleep(5)
            user.click(*user_web_locators.SEND)

            user.wait_for_element_visible(*user_web_locators.MESSAGE_TEXT)
            user.assert_element_contains_text(*user_web_locators.MESSAGE_TEXT, "😝😜🦄🐍🐙🦊🐼ab")
            time.sleep(5)
            advisor.assert_element_contains_text(*advisor_web_locators.MESSAGE_TEXT_FROM_USER, "😝😜🦄🐍🐙🦊🐼ab")
            advisor.wait_for_element_visible(*advisor_web_locators.TYPE_MESSAGE)

            advisor.execute_script("""
    try {
        var special_chars = "😝😜🦄🐍🐙🦊🐼";
        // Locate textarea by its class using XPath
        var textarea = document.evaluate(
            "//textarea[contains(@class,'input-expert-message')]",
            document,
            null,
            XPathResult.FIRST_ORDERED_NODE_TYPE,
            null
        ).singleNodeValue;
        if (textarea) {
            // Use the native setter so React/Angular/Vue detect the change
            var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
            nativeInputValueSetter.call(textarea, special_chars);
            // Trigger input and change events to notify the framework
            textarea.dispatchEvent(new Event('input', { bubbles: true }));
            textarea.dispatchEvent(new Event('change', { bubbles: true }));
            console.log("✅ Text inserted properly:", special_chars);
        } else {
            console.log("❌ Textarea not found!");
        }
    } catch(e) {
        console.log("⚠️ Error inserting text:", e);
    }
""")
            advisor.input_text_without_clear(*advisor_web_locators.TYPE_MESSAGE, "abcd")
            advisor.click(*advisor_web_locators.SEND)
            advisor.wait_for_element_visible(*advisor_web_locators.MESSAGE_TEXT)
            advisor.assert_element_contains_text(*advisor_web_locators.MESSAGE_TEXT, "😝😜🦄🐍🐙🦊🐼abcd")
            user.assert_element_contains_text(*user_web_locators.MESSAGE_TEXT_FROM_ADVISOR, "😝😜🦄🐍🐙🦊🐼abcd")
        except Exception as e:
            print(f"Test failed: {e}")


            # Take screenshot on failure
    def after_call_assertions(self, web_user, web_advisor):
        user = web_user
        advisor = web_advisor
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        try:

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