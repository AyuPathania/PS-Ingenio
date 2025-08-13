from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class WebElements:
    """Web element interaction methods for web browsers"""
    
    def __init__(self, driver, explicit_wait=20):
        """
        Initialize WebElements
        
        Args:
            driver: Selenium WebDriver instance
            explicit_wait (int): Explicit wait time in seconds
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, explicit_wait)
    
    # Element Finding Methods
    def find_element(self, locator_type, locator_value, timeout=None):
        """Find element with explicit wait"""
        wait_time = timeout or 20  # Default timeout of 20 seconds
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
        wait_time = timeout or 20  # Default timeout of 20 seconds
        wait = WebDriverWait(self.driver, wait_time)
        
        try:
            elements = wait.until(
                EC.presence_of_all_elements_located((locator_type, locator_value))
            )
            return elements
        except TimeoutException:
            print(f"Elements not found: {locator_type} = {locator_value}")
            return []
    
    def find_element_by_id(self, element_id, timeout=None):
        """Find element by ID"""
        return self.find_element(By.ID, element_id, timeout)
    
    def find_element_by_name(self, name, timeout=None):
        """Find element by name attribute"""
        return self.find_element(By.NAME, name, timeout)
    
    def find_element_by_class_name(self, class_name, timeout=None):
        """Find element by class name"""
        return self.find_element(By.CLASS_NAME, class_name, timeout)
    
    def find_element_by_tag_name(self, tag_name, timeout=None):
        """Find element by tag name"""
        return self.find_element(By.TAG_NAME, tag_name, timeout)
    
    def find_element_by_link_text(self, link_text, timeout=None):
        """Find element by exact link text"""
        return self.find_element(By.LINK_TEXT, link_text, timeout)
    
    def find_element_by_partial_link_text(self, partial_link_text, timeout=None):
        """Find element by partial link text"""
        return self.find_element(By.PARTIAL_LINK_TEXT, partial_link_text, timeout)
    
    def find_element_by_xpath(self, xpath, timeout=None):
        """Find element by XPath"""
        return self.find_element(By.XPATH, xpath, timeout)
    
    def find_element_by_css_selector(self, css_selector, timeout=None):
        """Find element by CSS selector"""
        return self.find_element(By.CSS_SELECTOR, css_selector, timeout)
    
    # Click Methods
    def click(self, locator_type, locator_value, timeout=None):
        """Click on element"""
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            element.click()
            return True
        return False
    
    def click_by_id(self, element_id, timeout=None):
        """Click element by ID"""
        return self.click(By.ID, element_id, timeout)
    
    def click_by_name(self, name, timeout=None):
        """Click element by name"""
        return self.click(By.NAME, name, timeout)
    
    def click_by_xpath(self, xpath, timeout=None):
        """Click element by XPath"""
        return self.click(By.XPATH, xpath, timeout)
    
    def click_by_css_selector(self, css_selector, timeout=None):
        """Click element by CSS selector"""
        return self.click(By.CSS_SELECTOR, css_selector, timeout)
    
    def click_by_text(self, text, timeout=None):
        """Click element by text content"""
        return self.click(By.XPATH, f"//*[text()='{text}']", timeout)
    
    def click_by_partial_text(self, partial_text, timeout=None):
        """Click element by partial text content"""
        return self.click(By.XPATH, f"//*[contains(text(),'{partial_text}')]", timeout)
    
    # Input Methods
    def input_text(self, locator_type, locator_value, text, timeout=None):
        """Input text into element"""
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            element.clear()
            element.send_keys(text)
            return True
        return False
    
    def input_text_by_id(self, element_id, text, timeout=None):
        """Input text into element by ID"""
        return self.input_text(By.ID, element_id, text, timeout)
    
    def input_text_by_name(self, name, text, timeout=None):
        """Input text into element by name"""
        return self.input_text(By.NAME, name, text, timeout)
    
    def input_text_by_xpath(self, xpath, text, timeout=None):
        """Input text into element by XPath"""
        return self.input_text(By.XPATH, xpath, text, timeout)
    
    def input_text_by_css_selector(self, css_selector, text, timeout=None):
        """Input text into element by CSS selector"""
        return self.input_text(By.CSS_SELECTOR, css_selector, text, timeout)
    
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
        wait_time = timeout or 20  # Default timeout of 20 seconds
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
        wait_time = timeout or 20  # Default timeout of 20 seconds
        wait = WebDriverWait(self.driver, wait_time)
        
        try:
            element = wait.until(
                EC.element_to_be_clickable((locator_type, locator_value))
            )
            return element
        except TimeoutException:
            print(f"Element not clickable: {locator_type} = {locator_value}")
            return None
    
    def wait_for_element_present(self, locator_type, locator_value, timeout=None):
        """Wait for element to be present in DOM"""
        wait_time = timeout or 20  # Default timeout of 20 seconds
        wait = WebDriverWait(self.driver, wait_time)
        
        try:
            element = wait.until(
                EC.presence_of_element_located((locator_type, locator_value))
            )
            return element
        except TimeoutException:
            print(f"Element not present: {locator_type} = {locator_value}")
            return None
    
    def wait_for_text_present(self, locator_type, locator_value, text, timeout=None):
        """Wait for specific text to be present in element"""
        wait_time = timeout or 20  # Default timeout of 20 seconds
        wait = WebDriverWait(self.driver, wait_time)
        
        try:
            element = wait.until(
                EC.text_to_be_present_in_element((locator_type, locator_value), text)
            )
            return True
        except TimeoutException:
            print(f"Text '{text}' not present in element: {locator_type} = {locator_value}")
            return False
    
    # Verification Methods
    def is_element_present(self, locator_type, locator_value, timeout=5):
        """Check if element is present"""
        element = self.find_element(locator_type, locator_value, timeout)
        return element is not None
    
    def is_element_visible(self, locator_type, locator_value, timeout=5):
        """Check if element is visible"""
        element = self.wait_for_element_visible(locator_type, locator_value, timeout)
        return element is not None
    
    def is_element_clickable(self, locator_type, locator_value, timeout=5):
        """Check if element is clickable"""
        element = self.wait_for_element_clickable(locator_type, locator_value, timeout)
        return element is not None
    
    def get_element_text(self, locator_type, locator_value, timeout=None):
        """Get text from element"""
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            return element.text
        return None
    
    def get_element_attribute(self, locator_type, locator_value, attribute_name, timeout=None):
        """Get attribute value from element"""
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            return element.get_attribute(attribute_name)
        return None
    
    def get_element_value(self, locator_type, locator_value, timeout=None):
        """Get value attribute from element"""
        return self.get_element_attribute(locator_type, locator_value, "value", timeout)
    
    def handle_alert(self, action='accept'):
        """Handle browser alerts through the driver
        
        Args:
            action (str): 'accept' or 'dismiss'
        """
        try:
            # Access the driver's switch_to.alert
            if action.lower() == 'accept':
                self.driver.switch_to.alert.accept()
                print("Alert accepted")
                return True
            else:
                self.driver.switch_to.alert.dismiss()
                print("Alert dismissed")
                return True
        except Exception as e:
            print(f"No alert to handle: {e}")
            return False
    
    def is_alert_present(self):
        """Check if an alert is present"""
        try:
            alert = self.driver.switch_to.alert
            return True
        except:
            return False
    
    # Dropdown Methods
    def select_by_value(self, locator_type, locator_value, value, timeout=None):
        """Select dropdown option by value"""
        from selenium.webdriver.support.ui import Select
        
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            select = Select(element)
            select.select_by_value(value)
            return True
        return False
    
    def select_by_visible_text(self, locator_type, locator_value, text, timeout=None):
        """Select dropdown option by visible text"""
        from selenium.webdriver.support.ui import Select
        
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            select = Select(element)
            select.select_by_visible_text(text)
            return True
        return False
    
    def select_by_index(self, locator_type, locator_value, index, timeout=None):
        """Select dropdown option by index"""
        from selenium.webdriver.support.ui import Select
        
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            select = Select(element)
            select.select_by_index(index)
            return True
        return False
    
    # Hover Methods
    def hover_over_element(self, locator_type, locator_value, timeout=None):
        """Hover over element"""
        from selenium.webdriver.common.action_chains import ActionChains
        
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            return True
        return False
    
    # Keyboard Methods
    def press_enter(self, locator_type, locator_value, timeout=None):
        """Press Enter key on element"""
        from selenium.webdriver.common.keys import Keys
        
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            element.send_keys(Keys.ENTER)
            return True
        return False
    
    def press_tab(self, locator_type, locator_value, timeout=None):
        """Press Tab key on element"""
        from selenium.webdriver.common.keys import Keys
        
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            element.send_keys(Keys.TAB)
            return True
        return False
    
    def press_escape(self, locator_type, locator_value, timeout=None):
        """Press Escape key on element"""
        from selenium.webdriver.common.keys import Keys
        
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            element.send_keys(Keys.ESCAPE)
            return True
        return False
    
    # Utility Methods
    def scroll_to_element(self, locator_type, locator_value, timeout=None):
        """Scroll to element"""
        element = self.find_element(locator_type, locator_value, timeout)
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(0.5)  # Small delay for smooth scrolling
            return True
        return False
    
    def scroll_to_bottom(self):
        """Scroll to bottom of page"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
    
    def scroll_to_top(self):
        """Scroll to top of page"""
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(0.5)
    
    def wait_for_page_load(self, timeout=30):
        """Wait for page to load completely"""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            return True
        except TimeoutException:
            print("Page load timeout")
            return False
