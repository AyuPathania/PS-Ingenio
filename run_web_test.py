#!/usr/bin/env python3
"""
Simple test runner for the web automation test
"""

import sys
import os

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from tests.test import TestAdvisorLogin, TestUserLogin
from tests.conftest import test_data

def run_web_test():
    """Run the web login tests for both advisor and user"""
    print("Starting Web Login Tests on LambdaTest...")
    print("Make sure you have configured your .env file with LambdaTest credentials!")
    print("=" * 50)
    
    try:
        # Test Advisor Login
        print("🧑‍💼 Testing Advisor Login...")
        print("-" * 30)
        
        advisor_test = TestAdvisorLogin()
        data = test_data()
        
        # Create a mock driver for standalone execution
        from core.web_driver import WebDriver
        mock_driver = WebDriver(browser='Chrome', headless=False)
        mock_driver.start_driver(user_type='advisor')
        
        try:
            advisor_test.test_valid_login_web(mock_driver, data)
            print("✅ Advisor Login Test completed successfully!")
        finally:
            mock_driver.quit_driver()
        
        print("\n" + "=" * 50 + "\n")
        
        # Test User Login
        print("👤 Testing User Login...")
        print("-" * 30)
        
        user_test = TestUserLogin()
        
        # Create a mock driver for standalone execution
        mock_driver = WebDriver(browser='Chrome', headless=False)
        mock_driver.start_driver(user_type='user')
        
        try:
            user_test.test_valid_login_web(mock_driver, data)
            print("✅ User Login Test completed successfully!")
        finally:
            mock_driver.quit_driver()
        
        print("=" * 50)
        print("🎉 All tests completed successfully!")
        
    except Exception as e:
        print("=" * 50)
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == "__main__":
    success = run_web_test()
    sys.exit(0 if success else 1)
