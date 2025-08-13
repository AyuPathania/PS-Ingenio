#!/usr/bin/env python3
"""
Example script demonstrating the use of WebDriver and WebElements classes
for web browser automation.
"""

from core.web_driver import WebDriver
from core.web_elements import WebElements
from selenium.webdriver.common.by import By
import time

def example_chrome_test():
    """Example Chrome browser test"""
    print("=== Chrome Browser Test ===")
    
    # Create Chrome driver
    driver = WebDriver(browser='chrome', headless=False)
    
    try:
        # Start the driver
        driver.start_driver()
        
        # Create WebElements instance
        elements = WebElements(driver.driver)
        
        # Navigate to a website
        driver.go_to_url("https://www.google.com")
        
        # Wait for page to load
        elements.wait_for_page_load()
        
        # Find and interact with search box
        search_box = elements.find_element_by_name("q")
        if search_box:
            elements.input_text(By.NAME, "q", "Selenium WebDriver Python")
            print("Entered search text")
            
            # Press Enter to search
            elements.press_enter(By.NAME, "q")
            print("Pressed Enter to search")
            
            # Wait for results
            time.sleep(2)
            
            # Take screenshot
            driver.take_screenshot("google_search_results.png")
            
            # Get page title
            title = driver.get_title()
            print(f"Page title: {title}")
        
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        # Clean up
        driver.quit_driver()

def example_firefox_test():
    """Example Firefox browser test"""
    print("\n=== Firefox Browser Test ===")
    
    # Create Firefox driver
    driver = WebDriver(browser='firefox', headless=False)
    
    try:
        # Start the driver
        driver.start_driver()
        
        # Create WebElements instance
        elements = WebElements(driver.driver)
        
        # Navigate to a website
        driver.go_to_url("https://www.python.org")
        
        # Wait for page to load
        elements.wait_for_page_load()
        
        # Find and click on a link
        download_link = elements.find_element_by_link_text("Downloads")
        if download_link:
            elements.click(By.LINK_TEXT, "Downloads")
            print("Clicked on Downloads link")
            
            # Wait for page to load
            time.sleep(2)
            
            # Take screenshot
            driver.take_screenshot("python_downloads.png")
            
            # Get current URL
            current_url = driver.get_current_url()
            print(f"Current URL: {current_url}")
        
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        # Clean up
        driver.quit_driver()

def example_edge_test():
    """Example Edge browser test"""
    print("\n=== Edge Browser Test ===")
    
    # Create Edge driver
    driver = WebDriver(browser='edge', headless=False)
    
    try:
        # Start the driver
        driver.start_driver()
        
        # Create WebElements instance
        elements = WebElements(driver.driver)
        
        # Navigate to a website
        driver.go_to_url("https://www.github.com")
        
        # Wait for page to load
        elements.wait_for_page_load()
        
        # Maximize window
        driver.maximize_window()
        
        # Find search box and enter text
        search_box = elements.find_element_by_xpath("//input[@placeholder='Search or jump to...']")
        if search_box:
            elements.input_text(By.XPATH, "//input[@placeholder='Search or jump to...']", "selenium")
            print("Entered search text in GitHub")
            
            # Wait a moment
            time.sleep(2)
            
            # Take screenshot
            driver.take_screenshot("github_search.png")
        
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        # Clean up
        driver.quit_driver()

def example_headless_test():
    """Example headless Chrome test"""
    print("\n=== Headless Chrome Test ===")
    
    # Create headless Chrome driver
    driver = WebDriver(browser='chrome', headless=True)
    
    try:
        # Start the driver
        driver.start_driver()
        
        # Create WebElements instance
        elements = WebElements(driver.driver)
        
        # Navigate to a website
        driver.go_to_url("https://httpbin.org/headers")
        
        # Wait for page to load
        elements.wait_for_page_load()
        
        # Get page source
        page_source = driver.get_page_source()
        print("Page source retrieved successfully")
        
        # Get page title
        title = driver.get_title()
        print(f"Page title: {title}")
        
        # Take screenshot (will be blank in headless mode but still works)
        driver.take_screenshot("headless_test.png")
        
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        # Clean up
        driver.quit_driver()

def example_alert_handling():
    """Example of handling JavaScript alerts"""
    print("\n=== Alert Handling Test ===")
    
    # Create Chrome driver
    driver = WebDriver(browser='chrome', headless=False)
    
    try:
        # Start the driver
        driver.start_driver()
        
        # Create WebElements instance
        elements = WebElements(driver.driver)
        
        # Navigate to a test page with alerts
        driver.go_to_url("https://the-internet.herokuapp.com/javascript_alerts")
        
        # Wait for page to load
        elements.wait_for_page_load()
        
        # Click on button that shows alert
        alert_button = elements.find_element_by_xpath("//button[text()='Click for JS Alert']")
        if alert_button:
            elements.click(By.XPATH, "//button[text()='Click for JS Alert']")
            print("Clicked alert button")
            
            # Wait for alert
            time.sleep(1)
            
            # Handle the alert
            driver.handle_alert(action='accept')
            print("Alert handled successfully")
            
            # Take screenshot
            driver.take_screenshot("alert_handled.png")
        
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        # Clean up
        driver.quit_driver()

if __name__ == "__main__":
    print("Web Browser Automation Examples")
    print("=" * 40)
    
    # Run examples (comment out any that you don't want to run)
    try:
        example_chrome_test()
        example_firefox_test()
        example_edge_test()
        example_headless_test()
        example_alert_handling()
        
        print("\n" + "=" * 40)
        print("All examples completed successfully!")
        
    except Exception as e:
        print(f"\nError running examples: {e}")
        print("Make sure you have the required browsers installed and webdriver-manager is working.")
