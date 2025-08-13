#!/usr/bin/env python3
"""
Simple test runner for the user login test only
"""

import sys
import os

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from tests.test import TestUserLogin
from tests.conftest import test_data

def run_user_test():
    """Run only the user login test"""
    print("👤 Starting User Login Test on LambdaTest...")
    print("Make sure you have configured your .env file with LambdaTest credentials!")
    print("=" * 50)
    
    try:
        # Create test instance
        test_instance = TestUserLogin()
        
        # Get test data
        data = test_data()
        
        # Create a mock driver for standalone execution
        from core.web_driver import WebDriver
        mock_driver = WebDriver(browser='Chrome', headless=False)
        mock_driver.start_driver(user_type='user')
        
        try:
            # Run the test
            test_instance.test_valid_login_web(mock_driver, data)
            
            print("=" * 50)
            print("✅ User Login Test completed successfully!")
            
        finally:
            mock_driver.quit_driver()
        
    except Exception as e:
        print("=" * 50)
        print(f"❌ User Login Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == "__main__":
    success = run_user_test()
    sys.exit(0 if success else 1)
