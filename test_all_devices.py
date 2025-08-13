#!/usr/bin/env python3
"""
Test script to start all types of devices and quit after 10 seconds
This script tests Android, iOS, and Web devices for both User and Advisor
"""

import time
import signal
from core.appium_driver import AppiumDriver
from config.config import Config

# Global timeout for mobile devices (in seconds)
MOBILE_TIMEOUT = 120  # 2 minutes timeout for mobile devices

class TimeoutError(Exception):
    """Custom timeout exception"""
    pass

def timeout_handler(signum, frame):
    """Handle timeout signal"""
    raise TimeoutError("Mobile device initialization timed out")

def test_device(platform, user_type):
    """
    Test a specific device type and quit after 10 seconds
    
    Args:
        platform (str): 'android', 'ios', or 'web'
        user_type (str): 'user' or 'advisor'
    """
    print(f"\n🚀 Starting {platform.upper()} - {user_type.upper()} device...")
    
    try:
        # Create driver
        driver = AppiumDriver(platform=platform, user_type=user_type)
        
        # Set timeout for mobile devices
        if platform in ['android', 'ios']:
            print(f"⏰ Setting {MOBILE_TIMEOUT} second timeout for {platform} device...")
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(MOBILE_TIMEOUT)
        
        # Start driver
        driver.start_driver()
        
        # Cancel timeout for mobile devices
        if platform in ['android', 'ios']:
            signal.alarm(0)
        
        if driver.driver:
            print(f"✅ {platform.upper()} - {user_type.upper()} device started successfully!")
            print(f"⏰ Waiting 10 seconds before quitting...")
            
            # Wait for 10 seconds
            time.sleep(10)
            
            # Take a screenshot before quitting
            screenshot_path = driver.take_screenshot(f"test_{platform}_{user_type}.png")
            if screenshot_path:
                print(f"📸 Screenshot saved: {screenshot_path}")
            
            # Quit driver
            driver.quit_driver()
            print(f"🛑 {platform.upper()} - {user_type.upper()} device quit successfully!")
            
        else:
            print(f"❌ Failed to start {platform.upper()} - {user_type.upper()} device")
            
    except TimeoutError as e:
        print(f"⏰ {platform.upper()} - {user_type.upper()} device timed out after {MOBILE_TIMEOUT} seconds")
        print("This is normal for mobile devices on LambdaTest - they can take 1-3 minutes to initialize")
        return False
    except Exception as e:
        print(f"❌ Error with {platform.upper()} - {user_type.upper()}: {e}")
        return False
    
    return True

def test_all_devices():
    """Test all device types and user types"""
    print("🧪 Starting comprehensive device testing...")
    print("=" * 50)
    
    # Check if LambdaTest is available
    if Config.is_lambdatest_enabled():
        print("✅ LambdaTest credentials found - testing with LambdaTest")
    else:
        print("❌ LambdaTest credentials not found - cannot proceed")
        return
    
    # Test all combinations
    platforms = ['android', 'ios', 'web']
    user_types = ['user', 'advisor']
    
    results = {}
    
    for platform in platforms:
        for user_type in user_types:
            success = test_device(platform, user_type)
            results[f"{platform}_{user_type}"] = success
            time.sleep(2)  # Small delay between tests
    
    print("\n" + "=" * 50)
    print("🎉 All device tests completed!")
    
    # Print summary
    print("\n📊 Test Results Summary:")
    for test_name, success in results.items():
        status = "✅ PASS" if success else "⏰ TIMEOUT/FAIL"
        print(f"  {test_name}: {status}")

def test_specific_device(platform, user_type):
    """
    Test a specific device type
    
    Args:
        platform (str): 'android', 'ios', or 'web'
        user_type (str): 'user' or 'advisor'
    """
    print(f"🧪 Testing specific device: {platform.upper()} - {user_type.upper()}")
    test_device(platform, user_type)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 2:
        # Test specific device: python test_all_devices.py android user
        platform = sys.argv[1].lower()
        user_type = sys.argv[2].lower()
        
        if platform in ['android', 'ios', 'web'] and user_type in ['user', 'advisor']:
            test_specific_device(platform, user_type)
        else:
            print("❌ Invalid arguments. Use: android/ios/web user/advisor")
            print("Example: python test_all_devices.py android user")
    else:
        # Test all devices
        test_all_devices()
