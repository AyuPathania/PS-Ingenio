from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.ie.options import Options as IEOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager
import time
import os

class WebDriver:
    """WebDriver class for web browser automation"""
    
    def __init__(self, browser='chrome', headless=False, implicit_wait=10, explicit_wait=20):
        """
        Initialize WebDriver
        
        Args:
            browser (str): 'chrome', 'firefox', 'edge', 'safari', 'ie'
            headless (bool): Run in headless mode
            implicit_wait (int): Implicit wait time in seconds
            explicit_wait (int): Explicit wait time in seconds
        """
        self.browser = browser  # Keep original case for capabilities
        self.browser_lower = browser.lower()  # Lowercase for internal use
        self.headless = headless
        self.implicit_wait = implicit_wait
        self.explicit_wait = explicit_wait
        self.driver = None
        self.wait = None
        
    def start_driver(self, user_type='advisor'):
        """Start the web driver using LambdaTest with exact capabilities structure"""
        try:
            from config.config import Config

            if not Config.is_lambdatest_enabled():
                raise Exception("LambdaTest credentials not configured. Please check your .env file.")

            print(f"Using LambdaTest hub for web browser: {self.browser}")

            from selenium.webdriver.common.options import ArgOptions
            web_caps = ArgOptions()

            # Base browser setup
            web_caps.set_capability("browserName", self.browser)   # e.g. "Chrome"
            web_caps.set_capability("platformName", "Windows 10")
            web_caps.set_capability("browserVersion", "latest")

            # LT:Options (this is where browserProfile goes)
            lt_options_web = {
                "username": Config.LAMBDATEST_USERNAME,
                #"browserProfile": "https://prod-magicleap-user-files-us-east-1-v1.s3.amazonaws.com/profile/chrome/orgId-2148160/Profile_4.zip",
                "accessKey": Config.LAMBDATEST_ACCESS_KEY,
                "build": "WebAndMobileChat",
                "name": f"Web {user_type.title()} Test",
                "platform": "Windows 10",
                "region": "ap",
                "version": "latest",
                "selenium_version": "4.0.0",
                "region": "ap",
                "w3c": True,
                "commandLog": True,
                "console": True,
                "idleTimeout": 300,
                "isRealMobile": False,
                "maxDuration": 20,
                "queueTimeout": "900",
                "systemLog": True,
                "visual": True,
                "network": True,
                "enableNetworkThrottling": True,

                # 👇 load your uploaded Chrome profile
                # "browserProfile": "https://prod-magicleap-user-files-us-east-1-v1.s3.amazonaws.com/profile/chrome/orgId-1666889/Profile"

                # 👇 pass chrome options inside LT:Options
                "goog:chromeOptions": {
                    "prefs": {
                        "profile.default_content_setting_values.notifications": 1
                    }
                }
            }

            # Attach LT options
            web_caps.set_capability("LT:Options", lt_options_web)

            # Hub URL
            server_url = f"https://{Config.LAMBDATEST_USERNAME}:{Config.LAMBDATEST_ACCESS_KEY}@hub.lambdatest.com/wd/hub"

            print(f"Server URL: {server_url}")
            print(f"Capabilities: {web_caps.capabilities}")

            # Start driver
            self.driver = webdriver.Remote(server_url, options=web_caps)

            if self.driver:
                self.driver.implicitly_wait(self.implicit_wait)
                self.wait = WebDriverWait(self.driver, self.explicit_wait)
                print(f"{self.browser} driver started successfully on LambdaTest")
                return self.driver
            else:
                raise Exception("Failed to create driver")
                
        except Exception as e:
            print(f"Failed to start {self.browser} driver: {e}")
            print(f"Error type: {type(e)}")
            import traceback
            traceback.print_exc()
            raise
    

    def _create_chrome_driver(self):
        """Create Chrome driver with options"""
        options = ChromeOptions()
        
        # Basic options
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        
        # Headless mode
        if self.headless:
            options.add_argument("--headless")
        
        # Performance options
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-plugins")
        
        # User agent
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        # Download ChromeDriver automatically
        service = ChromeService(ChromeDriverManager().install())
        
        return webdriver.Chrome(service=service, options=options)
    
    def _create_firefox_driver(self):
        """Create Firefox driver with options"""
        options = FirefoxOptions()
        
        # Basic options
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        
        # Headless mode
        if self.headless:
            options.add_argument("--headless")
        
        # Performance options
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-plugins")
        
        # Download GeckoDriver automatically
        service = FirefoxService(GeckoDriverManager().install())
        
        return webdriver.Firefox(service=service, options=options)
    
    def _create_edge_driver(self):
        """Create Edge driver with options"""
        options = EdgeOptions()
        
        # Basic options
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        
        # Headless mode
        if self.headless:
            options.add_argument("--headless")
        
        # Performance options
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-plugins")
        
        # Download EdgeDriver automatically
        service = EdgeService(EdgeChromiumDriverManager().install())
        
        return webdriver.Edge(service=service, options=options)
    
    def _create_safari_driver(self):
        """Create Safari driver (macOS only)"""
        options = SafariOptions()
        service = SafariService()
        
        return webdriver.Safari(service=service, options=options)
    
    def _create_ie_driver(self):
        """Create Internet Explorer driver (Windows only)"""
        options = IEOptions()
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-plugins")
        
        service = IEService(IEDriverManager().install())
        
        return webdriver.Ie(service=service, options=options)
    
    def quit_driver(self):
        """Quit the driver"""
        if self.driver:
            self.driver.quit()
            print(f"{self.browser.title()} driver quit successfully")
    
    def get_session_id(self):
        """Get the current session ID of the driver"""
        if self.driver:
            try:
                return self.driver.session_id
            except Exception as e:
                print(f"Failed to get session ID: {e}")
                return None
        return None
    
    def handle_alert(self, action='accept'):
        """Handle browser alerts and permission dialogs
        
        Args:
            action (str): 'accept' or 'dismiss'
        """
        try:
            # Wait a moment for any alert to appear
            time.sleep(2)
            
            # Try to switch to alert first (for JavaScript alerts)
            try:
                alert = self.driver.switch_to.alert
                print(f"Found alert: {alert.text}")
                
                if action.lower() == 'accept':
                    alert.accept()
                    print("Accepted alert")
                else:
                    alert.dismiss()
                    print("Dismissed alert")
                return True
                
            except:
                # No JavaScript alert, try to handle notification permission dialog
                print("No JavaScript alert found, checking for notification permission dialog...")
                
                # Look for notification permission buttons
                if action.lower() == 'accept':
                    # Try to find and click Allow button
                    allow_selectors = [
                        "//button[text()='Allow']",
                        "//button[contains(text(), 'Allow')]",
                        "//button[contains(text(), 'Allow notifications')]",
                        "//button[@data-testid='allow-notifications']",
                        "//button[contains(@class, 'allow')]"
                    ]
                    
                    for selector in allow_selectors:
                        try:
                            allow_button = self.driver.find_element("xpath", selector)
                            if allow_button and allow_button.is_displayed():
                                allow_button.click()
                                print(f"Clicked Allow notifications using selector: {selector}")
                                return True
                        except:
                            continue
                    
                    # If no button found, try using JavaScript to grant permissions
                    try:
                        self.driver.execute_script("Notification.requestPermission().then(permission => console.log('Permission:', permission))")
                        print("Attempted to grant notification permissions via JavaScript")
                        return True
                    except:
                        pass
                        
                elif action.lower() == 'dismiss':
                    # Try to find and click Block button
                    block_selectors = [
                        "//button[text()='Block']",
                        "//button[contains(text(), 'Block')]",
                        "//button[contains(text(), 'Block notifications')]",
                        "//button[@data-testid='block-notifications']"
                    ]
                    
                    for selector in block_selectors:
                        try:
                            block_button = self.driver.find_element("xpath", selector)
                            if block_button and block_button.is_displayed():
                                block_button.click()
                                print(f"Clicked Block notifications using selector: {selector}")
                                return True
                        except:
                            continue
                
                print("No notification permission dialog found or handled")
                return False
                    
        except Exception as e:
            print(f"Failed to handle alert: {e}")
            # Switch back to default content
            try:
                self.driver.switch_to.default_content()
            except:
                pass
            return False
    
    def go_to_url(self, url):
        """Navigate to URL"""
        try:
            self.driver.get(url)
            print(f"Navigated to: {url}")
        except Exception as e:
            print(f"Failed to navigate to {url}: {e}")
            raise
    
    def get_current_url(self):
        """Get current URL"""
        return self.driver.current_url
    
    def get_title(self):
        """Get page title"""
        return self.driver.title
    
    def refresh_page(self):
        """Refresh the current page"""
        self.driver.refresh()
        print("Page refreshed")
    
    def go_back(self):
        """Go back in browser history"""
        self.driver.back()
        print("Went back in browser history")
    
    def go_forward(self):
        """Go forward in browser history"""
        self.driver.forward()
        print("Went forward in browser history")
    
    def maximize_window(self):
        """Maximize browser window"""
        self.driver.maximize_window()
        print("Window maximized")
    
    def set_window_size(self, width, height):
        """Set window size"""
        self.driver.set_window_size(width, height)
        print(f"Window size set to {width}x{height}")
    
    def take_screenshot(self, filename=None):
        """Take screenshot"""
        if not filename:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{self.browser}_{timestamp}.png"
        
        screenshot_path = os.path.join("screenshots", filename)
        os.makedirs("screenshots", exist_ok=True)
        
        try:
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")
            return screenshot_path
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
            return None
    
    def execute_script(self, script, *args):
        """Execute JavaScript"""
        try:
            result = self.driver.execute_script(script, *args)
            return result
        except Exception as e:
            print(f"Failed to execute script: {e}")
            return None
    
    def get_page_source(self):
        """Get page source"""
        return self.driver.page_source
    
    def get_cookies(self):
        """Get all cookies"""
        return self.driver.get_cookies()
    
    def add_cookie(self, cookie_dict):
        """Add a cookie"""
        self.driver.add_cookie(cookie_dict)
        print("Cookie added")
    
    def delete_cookie(self, name):
        """Delete a cookie by name"""
        self.driver.delete_cookie(name)
        print(f"Cookie '{name}' deleted")
    
    def delete_all_cookies(self):
        """Delete all cookies"""
        self.driver.delete_all_cookies()
        print("All cookies deleted")
    
    def switch_to_frame(self, frame_reference):
        """Switch to frame"""
        self.driver.switch_to.frame(frame_reference)
        print("Switched to frame")
    
    def switch_to_default_content(self):
        """Switch to default content"""
        self.driver.switch_to.default_content()
        print("Switched to default content")
    
    def switch_to_window(self, window_handle):
        """Switch to window"""
        self.driver.switch_to.window(window_handle)
        print("Switched to window")
    
    def get_window_handles(self):
        """Get all window handles"""
        return self.driver.window_handles
    
    def get_current_window_handle(self):
        """Get current window handle"""
        return self.driver.current_window_handle
    
    def close_current_window(self):
        """Close current window"""
        self.driver.close()
        print("Current window closed")
    
    def handle_alert(self, action='accept'):
        """Handle JavaScript alert
        
        Args:
            action (str): 'accept' or 'dismiss'
        """
        try:
            alert = self.driver.switch_to.alert
            
            if action.lower() == 'accept':
                alert.accept()
                print("Alert accepted")
            elif action.lower() == 'dismiss':
                alert.dismiss()
                print("Alert dismissed")
            
            return True
        except Exception as e:
            print(f"Failed to handle alert: {e}")
            return False
    
    def get_alert_text(self):
        """Get alert text"""
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except Exception as e:
            print(f"Failed to get alert text: {e}")
            return None
    
    def send_keys_to_alert(self, text):
        """Send keys to prompt alert"""
        try:
            alert = self.driver.switch_to.alert
            alert.send_keys(text)
            print(f"Sent keys to alert: {text}")
            return True
        except Exception as e:
            print(f"Failed to send keys to alert: {e}")
            return False
    
    def wait_for_page_load(self, timeout=30):
        """Wait for page to fully load"""
        try:
            # Wait for document ready state
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            print("Page loaded completely")
            return True
        except TimeoutException:
            print(f"Page load timeout after {timeout} seconds")
            return False
        except Exception as e:
            print(f"Error waiting for page load: {e}")
            return False
    
    def wait_for_element_visible(self, locator_type, locator_value, timeout=None):
        """Wait for element to be visible"""
        wait_time = timeout or self.explicit_wait
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((locator_type, locator_value))
            )
            print(f"Element visible: {locator_type} = {locator_value}")
            return element
        except TimeoutException:
            print(f"Element not visible after {wait_time} seconds: {locator_type} = {locator_value}")
            return None
        except Exception as e:
            print(f"Error waiting for element visibility: {e}")
            return None
    
    def wait_for_element_present(self, locator_type, locator_value, timeout=10):
        """Wait for element to be present in DOM"""
        wait_time = timeout or self.explicit_wait
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((locator_type, locator_value))
            )
            print(f"Element present: {locator_type} = {locator_value}")
            return element
        except TimeoutException:
            print(f"Element not present after {wait_time} seconds: {locator_type} = {locator_value}")
            return None
        except Exception as e:
            print(f"Error waiting for element presence: {e}")
            return None
    
    def wait_for_element_clickable(self, locator_type, locator_value, timeout=10):
        """Wait for element to be clickable"""
        wait_time = timeout or self.explicit_wait
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.element_to_be_clickable((locator_type, locator_value))
            )
            print(f"Element clickable: {locator_type} = {locator_value}")
            return element
        except TimeoutException:
            print(f"Element not clickable after {wait_time} seconds: {locator_type} = {locator_value}")
            return False
        except Exception as e:
            print(f"Error waiting for element clickability: {e}")
            return False
    
    def click(self, locator_type, locator_value, timeout=None):
        """Click on element"""
        try:
            element = self.wait_for_element_clickable(locator_type, locator_value, timeout)
            if element:
                element.click()
                print(f"Clicked element: {locator_type} = {locator_value}")
                return True
            else:
                print(f"Failed to click element: {locator_type} = {locator_value}")
                return False
        except Exception as e:
            print(f"Error clicking element: {e}")
            return False
    
    def input_text(self, locator_type, locator_value, text, timeout=None):
        """Input text into element"""
        try:
            element = self.wait_for_element_visible(locator_type, locator_value, timeout)
            if element:
                element.clear()
                element.send_keys(text)
                print(f"Input text '{text}' into element: {locator_type} = {locator_value}")
                return True
            else:
                print(f"Failed to input text into element: {locator_type} = {locator_value}")
                return False
        except Exception as e:
            print(f"Error inputting text: {e}")
            return False


    def get_element_text(self, locator_type, locator_value, timeout=None):
        """Get text from element"""
        try:
            element = self.wait_for_element_visible(locator_type, locator_value, timeout)
            if element:
                text = element.text
                print(f"Got text '{text}' from element: {locator_type} = {locator_value}")
                return text
            else:
                print(f"Failed to get text from element: {locator_type} = {locator_value}")
                return None
        except Exception as e:
            print(f"Error getting element text: {e}")
            return None
    
    def get_element_attribute(self, locator_type, locator_value, attribute, timeout=None):
        """Get attribute value from element"""
        try:
            element = self.wait_for_element_present(locator_type, locator_value, timeout)
            if element:
                value = element.get_attribute(attribute)
                print(f"Got attribute '{attribute}' = '{value}' from element: {locator_type} = {locator_value}")
                return value
            else:
                print(f"Failed to get attribute from element: {locator_type} = {locator_value}")
                return None
        except Exception as e:
            print(f"Error getting element attribute: {e}")
            return None
    
    def is_element_displayed(self, locator_type, locator_value, timeout=None):
        """Check if element is displayed"""
        try:
            element = self.wait_for_element_visible(locator_type, locator_value, timeout)
            if element:
                is_displayed = element.is_displayed()
                print(f"Element displayed: {is_displayed} - {locator_type} = {locator_value}")
                return is_displayed
            else:
                print(f"Failed to check element display: {locator_type} = {locator_value}")
                return False
        except Exception as e:
            print(f"Error checking element display: {e}")
            return False

    def is_element_not_displayed(self, locator_type, locator_value, timeout=None):
        """Check if element is not displayed"""
        try:
            element = self.wait_for_element_visible(locator_type, locator_value, timeout)
            if element:
                is_displayed = not element.is_displayed()
                print(f"Element not displayed: {is_displayed} - {locator_type} = {locator_value}")
                return is_displayed
            else:
                print(f"Failed to check element display: {locator_type} = {locator_value}")
                return False
        except Exception as e:
            print(f"Error checking element display: {e}")
            return False
    
    def is_element_enabled(self, locator_type, locator_value, timeout=None):
        """Check if element is enabled"""
        try:
            element = self.wait_for_element_present(locator_type, locator_value, timeout)
            if element:
                is_enabled = element.is_enabled()
                print(f"Element enabled: {is_enabled} - {locator_type} = {locator_value}")
                return is_enabled
            else:
                print(f"Failed to check element enabled: {locator_type} = {locator_value}")
                return False
        except Exception as e:
            print(f"Error checking element enabled: {e}")
            return False
    
    def find_element(self, locator_type, locator_value, timeout=None):
        """Find element with explicit wait"""
        return self.wait_for_element_present(locator_type, locator_value, timeout)
    
    def find_elements(self, locator_type, locator_value, timeout=None):
        """Find multiple elements with explicit wait"""
        wait_time = timeout or self.explicit_wait
        try:
            elements = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_all_elements_located((locator_type, locator_value))
            )
            print(f"Found {len(elements)} elements: {locator_type} = {locator_value}")
            return elements
        except TimeoutException:
            print(f"No elements found after {wait_time} seconds: {locator_type} = {locator_value}")
            return []
        except Exception as e:
            print(f"Error finding elements: {e}")
            return []
    
    def scroll_to_element(self, locator_type, locator_value, timeout=None):
        """Scroll to element"""
        try:
            element = self.wait_for_element_present(locator_type, locator_value, timeout)
            if element:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                print(f"Scrolled to element: {locator_type} = {locator_value}")
                return True
            else:
                print(f"Failed to scroll to element: {locator_type} = {locator_value}")
                return False
        except Exception as e:
            print(f"Error scrolling to element: {e}")
            return False
    
    def scroll_to_top(self):
        """Scroll to top of page"""
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            print("Scrolled to top of page")
            return True
        except Exception as e:
            print(f"Error scrolling to top: {e}")
            return False
    
    def scroll_to_bottom(self):
        """Scroll to bottom of page"""
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print("Scrolled to bottom of page")
            return True
        except Exception as e:
            print(f"Error scrolling to bottom: {e}")
            return False
    
    def wait_for_text_present(self, text, timeout=None):
        """Wait for text to be present on page"""
        wait_time = timeout or self.explicit_wait
        try:
            WebDriverWait(self.driver, wait_time).until(
                lambda driver: text in driver.page_source
            )
            print(f"Text '{text}' found on page")
            return True
        except TimeoutException:
            print(f"Text '{text}' not found after {wait_time} seconds")
            return False
        except Exception as e:
            print(f"Error waiting for text: {e}")
            return False
    
    def wait_for_url_contains(self, url_part, timeout=None):
        """Wait for URL to contain specific text"""
        wait_time = timeout or self.explicit_wait
        try:
            WebDriverWait(self.driver, wait_time).until(
                lambda driver: url_part in driver.current_url
            )
            print(f"URL contains '{url_part}'")
            return True
        except TimeoutException:
            print(f"URL does not contain '{url_part}' after {wait_time} seconds")
            return False
        except Exception as e:
            print(f"Error waiting for URL: {e}")
            return False
    
    def wait_for_title_contains(self, title_part, timeout=None):
        """Wait for page title to contain specific text"""
        wait_time = timeout or self.explicit_wait
        try:
            WebDriverWait(self.driver, wait_time).until(
                lambda driver: title_part in driver.title
            )
            print(f"Title contains '{title_part}'")
            return True
        except TimeoutException:
            print(f"Title does not contain '{title_part}' after {wait_time} seconds")
            return False
        except Exception as e:
            print(f"Error waiting for title: {e}")
            return False
        
    def input_text_advisor(self, locator_type, locator_value, text, timeout=None):
        """Input text into element and send ENTER (advisor style)"""
        from selenium.webdriver.common.keys import Keys
        wait_time = timeout or self.explicit_wait
        try:
            wait = WebDriverWait(self.driver, wait_time)
            element = wait.until(EC.presence_of_element_located((locator_type, locator_value)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

            element = wait.until(EC.element_to_be_clickable((locator_type, locator_value)))
            element.click()
            element.send_keys(text, Keys.ENTER)

            print("✅ Message typed and sent.")
            return True
        except Exception as e:
            print(f"❌ Failed to type message: {e}")
            return False
        
    def input_text_user(self, locator_type, locator_value, text, timeout=None):
        """Input text into element (user style), scrolling into view first"""
        from selenium.webdriver.common.keys import Keys
        wait_time = timeout or self.explicit_wait
        try:
            wait = WebDriverWait(self.driver, wait_time)
            element = wait.until(EC.presence_of_element_located((locator_type, locator_value)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

            element = wait.until(EC.element_to_be_clickable((locator_type, locator_value)))
            element.click()
            element.send_keys(text)

            print(f"✅ Text '{text}' typed into element: {locator_type} = {locator_value}")
            return True
        except Exception as e:
            print(f"❌ Failed to type text: {e}")
            return False
        

    def go_offline(self):
            """Disable network connection"""
            try:
                self.driver.execute_script("lambda-throttle-network","Offline")
                print("🔌 Network disabled")

                return True
            except Exception as e:
                print(f"❌ Failed to Disable network: {e}")
                return False

    def go_online(self):
            """Enable network connection"""
            try:
                self.driver.execute_script("lambda-throttle-network","Reset")
                print("� Network re-enabled")

                return True
            except Exception as e:
                print(f"❌ Failed to Enable network: {e}")
                return False



    # Assertion Methods
    def assert_element_text_equals(self, locator_type, locator_value, expected_text, timeout=None):
        """Assert that element text equals expected text"""
        actual_text = self.get_element_text(locator_type, locator_value, timeout)
        assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}' for element {locator_type} = {locator_value}"
        print(f"✓ Assertion passed: Element text equals '{expected_text}'")
        return True
    
    def assert_element_contains_text(self, locator_type, locator_value, expected_text, timeout=None):
        """Assert that element contains expected text"""
        actual_text = self.get_element_text(locator_type, locator_value, timeout)
        assert expected_text in actual_text, f"Text '{expected_text}' not found in '{actual_text}' for element {locator_type} = {locator_value}"
        print(f"✓ Assertion passed: Element contains text '{expected_text}'")
        return True
    
    def assert_element_is_displayed(self, locator_type, locator_value, timeout=None):
        """Assert that element is displayed"""
        is_displayed = self.is_element_displayed(locator_type, locator_value, timeout)
        assert is_displayed, f"Element {locator_type} = {locator_value} is not displayed"
        print(f"✓ Assertion passed: Element is displayed")
        return True
    
    def assert_element_is_enabled(self, locator_type, locator_value, timeout=None):
        """Assert that element is enabled"""
        is_enabled = self.is_element_enabled(locator_type, locator_value, timeout)
        assert is_enabled, f"Element {locator_type} = {locator_value} is not enabled"
        print(f"✓ Assertion passed: Element is enabled")
        return True
    
    def assert_element_is_not_displayed(self, locator_type, locator_value, timeout=None):
        """Assert that element is not displayed"""
        is_displayed = self.is_element_displayed(locator_type, locator_value, timeout)
        assert not is_displayed, f"Element {locator_type} = {locator_value} is displayed but should not be"
        print(f"✓ Assertion passed: Element is not displayed")
        return True
    
    def assert_element_is_not_enabled(self, locator_type, locator_value, timeout=None):
        """Assert that element is not enabled"""
        is_enabled = self.is_element_enabled(locator_type, locator_value, timeout)
        assert not is_enabled, f"Element {locator_type} = {locator_value} is enabled but should not be"
        print(f"✓ Assertion passed: Element is not enabled")
        return True
    
    def assert_url_contains(self, expected_url_part):
        """Assert that current URL contains expected text"""
        current_url = self.get_current_url()
        assert expected_url_part in current_url, f"URL '{current_url}' does not contain '{expected_url_part}'"
        print(f"✓ Assertion passed: URL contains '{expected_url_part}'")
        return True
    
    def assert_url_equals(self, expected_url):
        """Assert that current URL equals expected URL"""
        current_url = self.get_current_url()
        assert current_url == expected_url, f"Expected URL '{expected_url}', but got '{current_url}'"
        print(f"✓ Assertion passed: URL equals '{expected_url}'")
        return True
    
    def assert_title_contains(self, expected_title_part):
        """Assert that page title contains expected text"""
        current_title = self.get_title()
        assert expected_title_part in current_title, f"Title '{current_title}' does not contain '{expected_title_part}'"
        print(f"✓ Assertion passed: Title contains '{expected_title_part}'")
        return True
    
    def assert_title_equals(self, expected_title):
        """Assert that page title equals expected title"""
        current_title = self.get_title()
        assert current_title == expected_title, f"Expected title '{expected_title}', but got '{current_title}'"
        print(f"✓ Assertion passed: Title equals '{expected_title}'")
        return True
    
    def assert_element_attribute_equals(self, locator_type, locator_value, attribute, expected_value, timeout=None):
        """Assert that element attribute equals expected value"""
        actual_value = self.get_element_attribute(locator_type, locator_value, attribute, timeout)
        assert actual_value == expected_value, f"Expected attribute '{attribute}' = '{expected_value}', but got '{actual_value}' for element {locator_type} = {locator_value}"
        print(f"✓ Assertion passed: Attribute '{attribute}' equals '{expected_value}'")
        return True
    
    def assert_element_attribute_contains(self, locator_type, locator_value, attribute, expected_value, timeout=None):
        """Assert that element attribute contains expected value"""
        actual_value = self.get_element_attribute(locator_type, locator_value, attribute, timeout)
        assert expected_value in actual_value, f"Attribute '{attribute}' = '{actual_value}' does not contain '{expected_value}' for element {locator_type} = {locator_value}"
        print(f"✓ Assertion passed: Attribute '{attribute}' contains '{expected_value}'")
        return True
    
    def assert_element_count_equals(self, locator_type, locator_value, expected_count, timeout=None):
        """Assert that number of elements equals expected count"""
        elements = self.find_elements(locator_type, locator_value, timeout)
        actual_count = len(elements)
        assert actual_count == expected_count, f"Expected {expected_count} elements, but found {actual_count} for {locator_type} = {locator_value}"
        print(f"✓ Assertion passed: Found {actual_count} elements as expected")
        return True
    
    def assert_element_count_greater_than(self, locator_type, locator_value, min_count, timeout=None):
        """Assert that number of elements is greater than minimum count"""
        elements = self.find_elements(locator_type, locator_value, timeout)
        actual_count = len(elements)
        assert actual_count > min_count, f"Expected more than {min_count} elements, but found {actual_count} for {locator_type} = {locator_value}"
        print(f"✓ Assertion passed: Found {actual_count} elements (greater than {min_count})")
        return True
    
    def assert_text_present_on_page(self, expected_text, timeout=None):
        """Assert that text is present anywhere on the page"""
        text_found = self.wait_for_text_present(expected_text, timeout)
        assert text_found, f"Text '{expected_text}' not found on page after timeout"
        print(f"✓ Assertion passed: Text '{expected_text}' found on page")
        return True
    
    def assert_text_not_present_on_page(self, unexpected_text, timeout=None):
        """Assert that text is not present anywhere on the page"""
        text_found = self.wait_for_text_present(unexpected_text, timeout)
        assert not text_found, f"Text '{unexpected_text}' found on page but should not be present"
        print(f"✓ Assertion passed: Text '{unexpected_text}' not found on page")
        return True
    
    def wait_for_document_loaded(self, timeout=30):
        """Wait until document.readyState is 'complete'."""
        start_time = time.time()
        while True:
            ready_state = self.driver.execute_script("return document.readyState")
            if ready_state == "complete":
                print("Document loaded")
                return
            if time.time() - start_time > timeout:
                raise TimeoutException("Timed out waiting for document to load.")
            time.sleep(0.5)