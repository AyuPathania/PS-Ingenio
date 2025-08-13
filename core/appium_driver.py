from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver

import time
import os
from config.config import Config

class AppiumDriver:
    def __init__(self, platform='android', user_type='user'):
        """
        Initialize Appium driver based on platform and user type
        
        Args:
            platform (str): 'android', 'ios', or 'web'
            user_type (str): 'user' or 'advisor'
        """
        self.platform = platform
        self.user_type = user_type
        self.driver = None
        self.wait = None
        
    def start_driver(self):
        """Start the Appium driver with LambdaTest capabilities using working structure"""
        capabilities = Config.get_lambdatest_capabilities(self.platform, self.user_type)
        server_url = Config.get_lambdatest_url(self.platform)
        print(f"Using LambdaTest hub for {self.platform} - {self.user_type}")
        
        try:
            print(f"Server URL: {server_url}")
            print(f"Capabilities: {capabilities}")
            
            if self.platform == 'android':
                # For Android, use UiAutomator2Options like working structure
                from appium.options.android import UiAutomator2Options
                
                # Create UiAutomator2Options object
                options = UiAutomator2Options()
                
                # Set capabilities EXACTLY like working file - directly on options
                options.set_capability("platformName", "Android")
                options.set_capability("automationName", "UiAutomator2")
                options.set_capability("newCommandTimeout", 86400)
                options.set_capability("idleTimeout", 1500)
                options.set_capability("useJSONSource", True)
                options.set_capability("w3c", True)
                options.set_capability("allowInvisibleElements", True)
                options.set_capability("ignoreUnimportantViews", True)
                options.set_capability("unicodeKeyboard", False)
                options.set_capability("autoGrantPermissions", True)
                options.set_capability("isRealMobile", True)
                options.set_capability("privateCloud", False)
                options.set_capability("autoAcceptAlerts", True)
                options.set_capability("visual", True)
                options.set_capability("video", True)
                
                # Set app-specific capabilities
                app_config = Config.USER_APP['android'] if self.user_type == 'user' else Config.ADVISOR_APP['android']
                options.set_capability("app", app_config['app'])
                options.set_capability("deviceName", app_config['deviceName'])
                options.set_capability("platformVersion", app_config['platformVersion'])
                
                # Set LT:Options exactly like working file
                options.set_capability("LT:Options", {
                    "name": f"Android {self.user_type.title()} Test",
                    "build": "WebAndMobile",
                    "user": Config.LAMBDATEST_USERNAME,
                    "accessKey": Config.LAMBDATEST_ACCESS_KEY,
                    "newCommandTimeout": 86400,
                    "idleTimeout": 1500,
                    "useJSONSource": True,
                    "w3c": True,
                    "allowInvisibleElements": True,
                    "ignoreUnimportantViews": True,
                    "unicodeKeyboard": False,
                    "autoGrantPermissions": True,
                    "isRealMobile": True,
                    "privateCloud": False,
                    "autoAcceptAlerts": True,
                    "visual": True,
                    "video": True,
                    "platformName": "Android",
                    "automationName": "UiAutomator2",
                    "app": app_config['app'],
                    "deviceName": app_config['deviceName'],
                    "platformVersion": app_config['platformVersion']
                })
                
                # Use webdriver.Remote with options (like working structure)
                self.driver = webdriver.Remote(
                    command_executor=server_url,
                    options=options
                )
                
            elif self.platform == 'ios':
                # For iOS, use UiAutomator2Options as base (can be used for iOS too)
                from appium.options.android import UiAutomator2Options
                
                # Create options object
                options = UiAutomator2Options()
                
                # Set capabilities EXACTLY like working file - directly on options
                options.set_capability("platformName", "iOS")
                options.set_capability("automationName", "XCUITest")
                options.set_capability("newCommandTimeout", 86400)
                options.set_capability("idleTimeout", 1500)
                options.set_capability("useJSONSource", True)
                options.set_capability("w3c", True)
                options.set_capability("allowInvisibleElements", True)
                options.set_capability("ignoreUnimportantViews", True)
                options.set_capability("unicodeKeyboard", False)
                options.set_capability("autoGrantPermissions", True)
                options.set_capability("isRealMobile", True)
                options.set_capability("privateCloud", False)
                options.set_capability("autoAcceptAlerts", True)
                options.set_capability("visual", True)
                options.set_capability("video", True)
                
                # Set app-specific capabilities
                app_config = Config.USER_APP['ios'] if self.user_type == 'user' else Config.ADVISOR_APP['ios']
                options.set_capability("app", app_config['app'])
                options.set_capability("deviceName", app_config['deviceName'])
                options.set_capability("platformVersion", app_config['platformVersion'])
                
                # Set LT:Options exactly like working file
                options.set_capability("LT:Options", {
                    "name": f"iOS {self.user_type.title()} Test",
                    "build": "WebAndMobile",
                    "user": Config.LAMBDATEST_USERNAME,
                    "accessKey": Config.LAMBDATEST_ACCESS_KEY,
                    "newCommandTimeout": 86400,
                    "idleTimeout": 1500,
                    "useJSONSource": True,
                    "w3c": True,
                    "allowInvisibleElements": True,
                    "ignoreUnimportantViews": True,
                    "unicodeKeyboard": False,
                    "autoGrantPermissions": True,
                    "isRealMobile": True,
                    "privateCloud": False,
                    "autoAcceptAlerts": True,
                    "visual": True,
                    "video": True,
                    "platformName": "iOS",
                    "automationName": "XCUITest",
                    "app": app_config['app'],
                    "deviceName": app_config['deviceName'],
                    "platformVersion": app_config['platformVersion']
                })
                
                # Use webdriver.Remote with options (like working structure)
                self.driver = webdriver.Remote(
                    command_executor=server_url,
                    options=options
                )
                
            else:  # Web
                # For web, create options object
                from selenium.webdriver.common.options import ArgOptions
                options = ArgOptions()
                options.set_capability('browserName', capabilities.get('browserName', 'chrome'))
                options.set_capability('platformName', capabilities.get('platformName', 'Windows 11'))
                
                # Add LT:Options
                if 'LT:Options' in capabilities:
                    for key, value in capabilities['LT:Options'].items():
                        options.set_capability(f'LT:{key}', value)
                
                self.driver = webdriver.Remote(server_url, options=options)
                
            self.driver.implicitly_wait(Config.IMPLICIT_WAIT)
            self.wait = WebDriverWait(self.driver, Config.EXPLICIT_WAIT)
            print(f"Driver started successfully for {self.platform} - {self.user_type}")
            return self.driver
        except Exception as e:
            print(f"Failed to start driver: {e}")
            print(f"Error type: {type(e)}")
            import traceback
            traceback.print_exc()
            raise
    

    
    def quit_driver(self):
        """Quit the driver"""
        if self.driver:
            self.driver.quit()
            print("Driver quit successfully")
    
    def go_to_url(self, url):
        """
        Navigate to the specified URL (for web testing).
        """
        if hasattr(self, 'driver') and self.driver:
            try:
                self.driver.get(url)
                print(f"Navigated to URL: {url}")
            except Exception as e:
                print(f"Failed to navigate to URL {url}: {e}")
                raise
        else:
            print("Driver not initialized. Cannot navigate to URL.")
    # Element Finding Methods
    def find_element(self, locator_type, locator_value, timeout=None):
        """Find element with explicit wait"""
        wait_time = timeout or Config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        
        try:
            element = wait.until(
                EC.presence_of_element_located((locator_type, locator_value))
            )
            return element
        except TimeoutException:
            print(f"Element not found: {locator_type} = {locator_value}")
            return None
    
    def find_elements(self, locator_type, locator_value, timeout=None):
        """Find multiple elements with explicit wait"""
        wait_time = timeout or Config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        
        try:
            elements = wait.until(
                EC.presence_of_all_elements_located((locator_type, locator_value))
            )
            return elements
        except TimeoutException:
            print(f"Elements not found: {locator_type} = {locator_type}")
            return []
    
    # Click Methods
    def click(self, locator_type, locator_value, timeout=None):
        """Click on element"""
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            element.click()
            return True
        return False
    
    def click_by_text(self, text, timeout=None):
        """Click element by text"""
        if self.platform == 'android':
            return self.click(AppiumBy.ANDROID_UIAUTOMATOR, f'text("{text}")', timeout)
        elif self.platform == 'ios':
            return self.click(AppiumBy.IOS_PREDICATE, f'label == "{text}"', timeout)
        else:
            return self.click(AppiumBy.XPATH, f'//*[text()="{text}"]', timeout)
    
    # Input Methods
    def input_text(self, locator_type, locator_value, text, timeout=None):
        """Input text into element"""
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            element.clear()
            element.send_keys(text)
            return True
        return False
    
    def clear_text(self, locator_type, locator_value, timeout=None):
        """Clear text from element"""
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            element.clear()
            return True
        return False
    
    # Wait Methods
    def wait_for_element(self, locator_type, locator_value, timeout=None):
        """Wait for element to be present"""
        return self.find_element(locator_type, locator_value, timeout)
    
    def wait_for_element_visible(self, locator_type, locator_value, timeout=None):
        """Wait for element to be visible"""
        wait_time = timeout or Config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        
        try:
            element = wait.until(
                EC.visibility_of_element_located((locator_type, locator_value))
            )
            return element
        except TimeoutException:
            print(f"Element not visible: {locator_type} = {locator_value}")
            return None
    
    def wait_for_element_clickable(self, locator_type, locator_value, timeout=None):
        """Wait for element to be clickable"""
        wait_time = timeout or Config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        
        try:
            element = wait.until(
                EC.element_to_be_clickable((locator_type, locator_value))
            )
            return element
        except TimeoutException:
            print(f"Element not clickable: {locator_type} = {locator_value}")
            return None
    
    # Navigation Methods
    def go_back(self):
        """Go back in app"""
        if self.platform in ['android', 'ios']:
            self.driver.back()
    
    def swipe(self, start_x, start_y, end_x, end_y, duration=1000):
        """Swipe gesture"""
        if self.platform in ['android', 'ios']:
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)
    
    def scroll_to_element(self, locator_type, locator_value, direction='down'):
        """Scroll to find element"""
        if self.platform == 'android':
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
                                   f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{locator_value}"))')
        elif self.platform == 'ios':
            # iOS scroll implementation
            pass
    
    # Verification Methods
    def is_element_present(self, locator_type, locator_value, timeout=5):
        """Check if element is present"""
        element = self.find_element(locator_type, locator_value, timeout)
        return element is not None
    
    def is_element_visible(self, locator_type, locator_value, timeout=5):
        """Check if element is visible"""
        element = self.wait_for_element_visible(locator_type, locator_value, timeout)
        return element is not None
    
    def get_element_text(self, locator_type, locator_value, timeout=None):
        """Get text from element"""
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            return element.text
        return None
    
    # Screenshot Methods
    def take_screenshot(self, filename=None):
        """Take screenshot"""
        if not filename:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{self.platform}_{self.user_type}_{timestamp}.png"
        
        screenshot_path = os.path.join(Config.SCREENSHOT_DIR, filename)
        os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True)
        
        try:
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")
            return screenshot_path
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
            return None
    
    # Platform-specific Methods
    def get_android_element_by_text(self, text):
        """Get Android element by text using UiAutomator"""
        return self.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'text("{text}")')
    
    def get_ios_element_by_text(self, text):
        """Get iOS element by text using predicate"""
        return self.find_element(AppiumBy.IOS_PREDICATE, f'label == "{text}"')
    
    def get_web_element_by_text(self, text):
        """Get web element by text using XPath"""
        return self.find_element(AppiumBy.XPATH, f'//*[contains(text(),"{text}")]')
    
    # LambdaTest Specific Methods
    def execute_lambdatest_script(self, script, args=None):
        """Execute LambdaTest specific script"""
        try:
            if args:
                result = self.driver.execute_script(script, args)
            else:
                result = self.driver.execute_script(script)
            return result
        except Exception as e:
            print(f"Failed to execute LambdaTest script: {e}")
            return None
    
    def set_lambdatest_status(self, status, reason=""):
        """Set test status in LambdaTest"""
        try:
            if status.lower() == 'passed':
                self.driver.execute_script("lambda-status=passed")
            elif status.lower() == 'failed':
                self.driver.execute_script(f"lambda-status=failed&lambda-reason={reason}")
            print(f"LambdaTest status set to: {status}")
        except Exception as e:
            print(f"Failed to set LambdaTest status: {e}")
    
    def handle_notification_alert(self, action='allow'):
        """Handle notification permission alert
        
        Args:
            action (str): 'allow' or 'block' notifications
        """
        try:
            # Wait a moment for the alert to appear
            time.sleep(2)
            
            # Switch to the alert
            alert = self.driver.switch_to.alert
            print("Going to alert")
            print(alert.text)
            
            if action.lower() == 'allow':
                # Accept the alert (this will allow notifications)
                alert.accept()
                print("Accepted notification alert (Allow)")
                return True
            elif action.lower() == 'block':
                # Dismiss the alert (this will block notifications)
                alert.dismiss()
                print("Dismissed notification alert (Block)")
                return True
                
        except Exception as e:
            print(f"Failed to handle notification alert: {e}")
            # Switch back to default content
            try:
                self.driver.switch_to.default_content()
            except:
                pass
            return False
        
    def start_driver(self):
        """Start the Appium driver with LambdaTest capabilities using working structure"""
        capabilities = Config.get_lambdatest_capabilities(self.platform, self.user_type)
        server_url = Config.get_lambdatest_url(self.platform)
        print(f"Using LambdaTest hub for {self.platform} - {self.user_type}")
        
        try:
            print(f"Server URL: {server_url}")
            print(f"Capabilities: {capabilities}")
            
            if self.platform == 'android':
                # For Android, use UiAutomator2Options like working structure
                from appium.options.android import UiAutomator2Options
                
                # Create UiAutomator2Options object
                options = UiAutomator2Options()
                
                # Set capabilities EXACTLY like working file - directly on options
                options.set_capability("platformName", "Android")
                options.set_capability("automationName", "UiAutomator2")
                options.set_capability("newCommandTimeout", 86400)
                options.set_capability("idleTimeout", 1500)
                options.set_capability("useJSONSource", True)
                options.set_capability("w3c", True)
                options.set_capability("allowInvisibleElements", True)
                options.set_capability("ignoreUnimportantViews", True)
                options.set_capability("unicodeKeyboard", False)
                options.set_capability("autoGrantPermissions", True)
                options.set_capability("isRealMobile", True)
                options.set_capability("privateCloud", False)
                options.set_capability("autoAcceptAlerts", True)
                options.set_capability("visual", True)
                options.set_capability("video", True)
                
                # Set app-specific capabilities
                app_config = Config.USER_APP['android'] if self.user_type == 'user' else Config.ADVISOR_APP['android']
                options.set_capability("app", app_config['app'])
                options.set_capability("deviceName", app_config['deviceName'])
                options.set_capability("platformVersion", app_config['platformVersion'])
                
                # Set LT:Options exactly like working file
                options.set_capability("LT:Options", {
                    "name": f"Android {self.user_type.title()} Test",
                    "build": "WebAndMobile",
                    "user": Config.LAMBDATEST_USERNAME,
                    "accessKey": Config.LAMBDATEST_ACCESS_KEY,
                    "newCommandTimeout": 86400,
                    "idleTimeout": 1500,
                    "useJSONSource": True,
                    "w3c": True,
                    "allowInvisibleElements": True,
                    "ignoreUnimportantViews": True,
                    "unicodeKeyboard": False,
                    "autoGrantPermissions": True,
                    "isRealMobile": True,
                    "privateCloud": False,
                    "autoAcceptAlerts": True,
                    "visual": True,
                    "video": True,
                    "platformName": "Android",
                    "automationName": "UiAutomator2",
                    "app": app_config['app'],
                    "deviceName": app_config['deviceName'],
                    "platformVersion": app_config['platformVersion']
                })
                
                # Use webdriver.Remote with options (like working structure)
                self.driver = webdriver.Remote(
                    command_executor=server_url,
                    options=options
                )
                
            elif self.platform == 'ios':
                # For iOS, use UiAutomator2Options as base (can be used for iOS too)
                from appium.options.android import UiAutomator2Options
                
                # Create options object
                options = UiAutomator2Options()
                
                # Set capabilities EXACTLY like working file - directly on options
                options.set_capability("platformName", "iOS")
                options.set_capability("automationName", "XCUITest")
                options.set_capability("newCommandTimeout", 86400)
                options.set_capability("idleTimeout", 1500)
                options.set_capability("useJSONSource", True)
                options.set_capability("w3c", True)
                options.set_capability("allowInvisibleElements", True)
                options.set_capability("ignoreUnimportantViews", True)
                options.set_capability("unicodeKeyboard", False)
                options.set_capability("autoGrantPermissions", True)
                options.set_capability("isRealMobile", True)
                options.set_capability("privateCloud", False)
                options.set_capability("autoAcceptAlerts", True)
                options.set_capability("visual", True)
                options.set_capability("video", True)
                
                # Set app-specific capabilities
                app_config = Config.USER_APP['ios'] if self.user_type == 'user' else Config.ADVISOR_APP['ios']
                options.set_capability("app", app_config['app'])
                options.set_capability("deviceName", app_config['deviceName'])
                options.set_capability("platformVersion", app_config['platformVersion'])
                
                # Set LT:Options exactly like working file
                options.set_capability("LT:Options", {
                    "name": f"iOS {self.user_type.title()} Test",
                    "build": "WebAndMobile",
                    "user": Config.LAMBDATEST_USERNAME,
                    "accessKey": Config.LAMBDATEST_ACCESS_KEY,
                    "newCommandTimeout": 86400,
                    "idleTimeout": 1500,
                    "useJSONSource": True,
                    "w3c": True,
                    "allowInvisibleElements": True,
                    "ignoreUnimportantViews": True,
                    "unicodeKeyboard": False,
                    "autoGrantPermissions": True,
                    "isRealMobile": True,
                    "privateCloud": False,
                    "autoAcceptAlerts": True,
                    "visual": True,
                    "video": True,
                    "platformName": "iOS",
                    "automationName": "XCUITest",
                    "app": app_config['app'],
                    "deviceName": app_config['deviceName'],
                    "platformVersion": app_config['platformVersion']
                })
                
                # Use webdriver.Remote with options (like working structure)
                self.driver = webdriver.Remote(
                    command_executor=server_url,
                    options=options
                )
                
            else:  # Web
                # For web, create options object
                from selenium.webdriver.common.options import ArgOptions
                options = ArgOptions()
                options.set_capability('browserName', capabilities.get('browserName', 'chrome'))
                options.set_capability('platformName', capabilities.get('platformName', 'Windows 11'))
                
                # Add LT:Options
                if 'LT:Options' in capabilities:
                    for key, value in capabilities['LT:Options'].items():
                        options.set_capability(f'LT:{key}', value)
                
                self.driver = webdriver.Remote(server_url, options=options)
                
            self.driver.implicitly_wait(Config.IMPLICIT_WAIT)
            self.wait = WebDriverWait(self.driver, Config.EXPLICIT_WAIT)
            print(f"Driver started successfully for {self.platform} - {self.user_type}")
            return self.driver
        except Exception as e:
            print(f"Failed to start driver: {e}")
            print(f"Error type: {type(e)}")
            import traceback
            traceback.print_exc()
            raise
    

    
    def quit_driver(self):
        """Quit the driver"""
        if self.driver:
            self.driver.quit()
            print("Driver quit successfully")
    
    # Element Finding Methods
    def find_element(self, locator_type, locator_value, timeout=None):
        """Find element with explicit wait"""
        wait_time = timeout or Config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        
        try:
            element = wait.until(
                EC.presence_of_element_located((locator_type, locator_value))
            )
            return element
        except TimeoutException:
            print(f"Element not found: {locator_type} = {locator_value}")
            return None
    
    def find_elements(self, locator_type, locator_value, timeout=None):
        """Find multiple elements with explicit wait"""
        wait_time = timeout or Config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        
        try:
            elements = wait.until(
                EC.presence_of_all_elements_located((locator_type, locator_value))
            )
            return elements
        except TimeoutException:
            print(f"Elements not found: {locator_type} = {locator_type}")
            return []
    
    # Click Methods
    def click(self, locator_type, locator_value, timeout=None):
        """Click on element"""
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            element.click()
            return True
        return False
    
    def click_by_text(self, text, timeout=None):
        """Click element by text"""
        if self.platform == 'android':
            return self.click(AppiumBy.ANDROID_UIAUTOMATOR, f'text("{text}")', timeout)
        elif self.platform == 'ios':
            return self.click(AppiumBy.IOS_PREDICATE, f'label == "{text}"', timeout)
        else:
            return self.click(AppiumBy.XPATH, f'//*[text()="{text}"]', timeout)
    
    # Input Methods
    def input_text(self, locator_type, locator_value, text, timeout=None):
        """Input text into element"""
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            element.clear()
            element.send_keys(text)
            return True
        return False
    
    def clear_text(self, locator_type, locator_value, timeout=None):
        """Clear text from element"""
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            element.clear()
            return True
        return False
    
    # Wait Methods
    def wait_for_element(self, locator_type, locator_value, timeout=None):
        """Wait for element to be present"""
        return self.find_element(locator_type, locator_value, timeout)
    
    def wait_for_element_visible(self, locator_type, locator_value, timeout=None):
        """Wait for element to be visible"""
        wait_time = timeout or Config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        
        try:
            element = wait.until(
                EC.visibility_of_element_located((locator_type, locator_value))
            )
            return element
        except TimeoutException:
            print(f"Element not visible: {locator_type} = {locator_value}")
            return None
    
    def wait_for_element_clickable(self, locator_type, locator_value, timeout=None):
        """Wait for element to be clickable"""
        wait_time = timeout or Config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        
        try:
            element = wait.until(
                EC.element_to_be_clickable((locator_type, locator_value))
            )
            return element
        except TimeoutException:
            print(f"Element not clickable: {locator_type} = {locator_value}")
            return None
    
    # Navigation Methods
    def go_back(self):
        """Go back in app"""
        if self.platform in ['android', 'ios']:
            self.driver.back()
    
    def swipe(self, start_x, start_y, end_x, end_y, duration=1000):
        """Swipe gesture"""
        if self.platform in ['android', 'ios']:
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)
    
    def scroll_to_element(self, locator_type, locator_value, direction='down'):
        """Scroll to find element"""
        if self.platform == 'android':
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
                                   f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{locator_value}"))')
        elif self.platform == 'ios':
            # iOS scroll implementation
            pass
    
    # Verification Methods
    def is_element_present(self, locator_type, locator_value, timeout=5):
        """Check if element is present"""
        element = self.find_element(locator_type, locator_value, timeout)
        return element is not None
    
    def is_element_visible(self, locator_type, locator_value, timeout=5):
        """Check if element is visible"""
        element = self.wait_for_element_visible(locator_type, locator_value, timeout)
        return element is not None
    
    def get_element_text(self, locator_type, locator_value, timeout=None):
        """Get text from element"""
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            return element.text
        return None
    
    # Screenshot Methods
    def take_screenshot(self, filename=None):
        """Take screenshot"""
        if not filename:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{self.platform}_{self.user_type}_{timestamp}.png"
        
        screenshot_path = os.path.join(Config.SCREENSHOT_DIR, filename)
        os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True)
        
        try:
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")
            return screenshot_path
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
            return None
    
    # Platform-specific Methods
    def get_android_element_by_text(self, text):
        """Get Android element by text using UiAutomator"""
        return self.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'text("{text}")')
    
    def get_ios_element_by_text(self, text):
        """Get iOS element by text using predicate"""
        return self.find_element(AppiumBy.IOS_PREDICATE, f'label == "{text}"')
    
    def get_web_element_by_text(self, text):
        """Get web element by text using XPath"""
        return self.find_element(AppiumBy.XPATH, f'//*[contains(text(),"{text}")]')
    
    # LambdaTest Specific Methods
    def execute_lambdatest_script(self, script, args=None):
        """Execute LambdaTest specific script"""
        try:
            if args:
                result = self.driver.execute_script(script, args)
            else:
                result = self.driver.execute_script(script)
            return result
        except Exception as e:
            print(f"Failed to execute LambdaTest script: {e}")
            return None
    
    def set_lambdatest_status(self, status, reason=""):
        """Set test status in LambdaTest"""
        try:
            if status.lower() == 'passed':
                self.driver.execute_script("lambda-status=passed")
            elif status.lower() == 'failed':
                self.driver.execute_script(f"lambda-status=failed&lambda-reason={reason}")
            print(f"LambdaTest status set to: {status}")
        except Exception as e:
            print(f"Failed to set LambdaTest status: {e}")
