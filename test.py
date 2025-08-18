from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# Path to your extracted profile folder on Desktop (not the ZIP file)
profile_path = os.path.expanduser("~/Desktop/Profileayush")

chrome_options = Options()

# Check if profile directory exists and use it
if os.path.isdir(profile_path):
    # Use absolute path and add more specific profile options
    abs_profile_path = os.path.abspath(profile_path)
    chrome_options.add_argument(f"user-data-dir={abs_profile_path}")
    chrome_options.add_argument("--profile-directory=Default")
    print(f"✅ Using Chrome profile: {abs_profile_path}")
    
    # List contents of profile directory to verify
    try:
        profile_contents = os.listdir(abs_profile_path)
        print(f"📁 Profile directory contains: {profile_contents[:5]}...")  # Show first 5 items
    except Exception as e:
        print(f"⚠️ Could not read profile directory: {e}")
else:
    print(f"❌ Profile directory not found: {profile_path}")
    print("💡 To fix this:")
    print("   1. Extract Profileayush.zip to ~/Desktop/Profileayush")
    print("   2. Make sure it's a folder, not a ZIP file")
    print("   3. Run this script again")
    print("Starting Chrome without profile...")

# Add Chrome options to avoid conflicts and ensure profile loading
chrome_options.add_argument("--no-first-run")
chrome_options.add_argument("--no-default-browser-check")
chrome_options.add_argument("--disable-background-timer-throttling")
chrome_options.add_argument("--disable-backgrounding-occluded-windows")
chrome_options.add_argument("--disable-renderer-backgrounding")
chrome_options.add_argument("--disable-extensions-except")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--disable-default-apps")

# Download ChromeDriver and get the correct path
base_path = ChromeDriverManager().install()
# Fix the path to point to the actual chromedriver executable
driver_path = base_path.replace("THIRD_PARTY_NOTICES.chromedriver", "chromedriver")

# Verify the driver path is correct
if not os.path.exists(driver_path):
    print(f"❌ Driver not found: {driver_path}")
    exit(1)

print(f"✅ Using ChromeDriver: {driver_path}")

driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

# Wait a moment for Chrome to fully load with profile
time.sleep(3)

driver.get("https://mail.google.com")
time.sleep(10)
