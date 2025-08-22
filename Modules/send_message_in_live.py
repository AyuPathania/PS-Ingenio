from selenium.webdriver.common.by import By
# from locators.test.ayush_locator import AyushLocator
from locators.MixPanel.MixPanel import MixPanelLocators
from locators.user.web_locators import UserWebLocators
from locators.advisor.web_locators import AdvisorWebLocators
import random
import time

class SendMessage:
    def send_message_in_live(self, web_user, web_advisor):
        user = web_user
        advisor = web_advisor
        user_web_locators = UserWebLocators()
        advisor_web_locators = AdvisorWebLocators()
        try:
            user.wait_for_element_visible(*user_web_locators.TYPE_MESSAGE)

            # user.input_text(*user_web_locators.TYPE_MESSAGE, random_text)
            user.execute_script("""
    try {
        var special_chars = "!@#$%^&*()_+[]|:;<>?,./~😝😜a";
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
            user.input_text_without_clear(*user_web_locators.TYPE_MESSAGE, "bc")
            time.sleep(5)
            user.click(*user_web_locators.SEND)

            user.wait_for_element_visible(*user_web_locators.MESSAGE_TEXT)
            user.assert_element_contains_text(*user_web_locators.MESSAGE_TEXT, "!@#$%^&*()_+[]|:;<>?,./~😝😜abc")
            time.sleep(5)
            advisor.assert_element_contains_text(*advisor_web_locators.MESSAGE_TEXT_FROM_USER, "!@#$%^&*()_+[]|:;<>?,./~😝😜abc")
            advisor.wait_for_element_visible(*advisor_web_locators.TYPE_MESSAGE)

            advisor.execute_script("""
    try {
        var special_chars = "!@#$%^&*()_+[]|:;<>?,./~😝😜a";
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
            advisor.input_text_without_clear(*advisor_web_locators.TYPE_MESSAGE, "bcd")
            advisor.click(*advisor_web_locators.SEND)
            advisor.wait_for_element_visible(*advisor_web_locators.MESSAGE_TEXT)
            advisor.assert_element_contains_text(*advisor_web_locators.MESSAGE_TEXT, "!@#$%^&*()_+[]|:;<>?,./~😝😜abcd")
            user.assert_element_contains_text(*user_web_locators.MESSAGE_TEXT_FROM_ADVISOR, "!@#$%^&*()_+[]|:;<>?,./~😝😜abcd")
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure