import pytest
import sys
import os
import subprocess
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from drivers.appium_driver import AppiumDriver
from drivers.web_driver import WebDriver
from config.config import Config
from faker import Faker

def pytest_sessionfinish(session, exitstatus):
    """Generate Allure report automatically after test session completes"""
    try:
        allure_results_dir = "./allure-results"
        allure_report_dir = "./allure-report"
        
        # Check if allure-results directory exists and has content
        if os.path.exists(allure_results_dir) and os.listdir(allure_results_dir):
            print("\n" + "="*80)
            print("🔄 GENERATING ALLURE REPORT...")
            print("="*80)
            
            # Try to use allure command if available
            try:
                # Generate the report
                result = subprocess.run(
                    ["allure", "generate", allure_results_dir, "--clean", "-o", allure_report_dir],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                
                if result.returncode == 0:
                    print("✅ Allure report generated successfully!")
                    print(f"📁 Report location: {os.path.abspath(allure_report_dir)}")
                    print(f"🌐 Open report: open {os.path.abspath(allure_report_dir)}/index.html")
                    
                    # Try to open the report automatically
                    try:
                        if sys.platform == "darwin":  # macOS
                            subprocess.run(["open", f"{allure_report_dir}/index.html"])
                        elif sys.platform == "win32":  # Windows
                            subprocess.run(["start", f"{allure_report_dir}/index.html"], shell=True)
                        elif sys.platform.startswith("linux"):  # Linux
                            subprocess.run(["xdg-open", f"{allure_report_dir}/index.html"])
                        print("🚀 Report opened in browser automatically!")
                    except Exception as e:
                        print(f"⚠️  Could not open report automatically: {e}")
                        print(f"📖 Please open manually: {allure_report_dir}/index.html")
                        
                else:
                    print("❌ Failed to generate Allure report")
                    print(f"Error: {result.stderr}")
                    
            except FileNotFoundError:
                print("⚠️  Allure command not found. Installing...")
                print("💡 Please install Allure first:")
                print("   macOS: brew install allure")
                print("   Windows: scoop install allure")
                print("   Linux: sudo apt-get install allure")
                print(f"📁 Results are available in: {os.path.abspath(allure_results_dir)}")
                
            except subprocess.TimeoutExpired:
                print("⏰ Allure report generation timed out")
                print(f"📁 Results are available in: {os.path.abspath(allure_results_dir)}")
                
        else:
            print("\n📝 No test results found to generate report")
            
        print("="*80)
        
    except Exception as e:
        print(f"❌ Error generating Allure report: {e}")
        print(f"📁 Results are available in: {os.path.abspath(allure_results_dir)}")

@pytest.fixture(scope="function")
def android_user_driver():
    """Fixture for Android User app driver"""
    driver = None
    try:
        driver = AppiumDriver(platform='android', user_type='user')
        driver.start_driver()
        yield driver
    finally:
        if driver and driver.driver:
            driver.quit_driver()

@pytest.fixture(scope="function")
def android_advisor_driver():
    """Fixture for Android Advisor app driver"""
    driver = None
    try:
        driver = AppiumDriver(platform='android', user_type='advisor')
        driver.start_driver()
        yield driver
    finally:
        if driver and driver.driver:
            driver.quit_driver()

@pytest.fixture(scope="function")
def ios_user_driver():
    """Fixture for iOS User app driver"""
    driver = None
    try:
        driver = AppiumDriver(platform='ios', user_type='user')
        driver.start_driver()
        yield driver
    finally:
        if driver and driver.driver:
            driver.quit_driver()

@pytest.fixture(scope="function")
def ios_advisor_driver():
    """Fixture for iOS Advisor app driver"""
    driver = None
    try:
        driver = AppiumDriver(platform='ios', user_type='advisor')
        driver.start_driver()
        yield driver
    finally:
        if driver and driver.driver:
            driver.quit_driver()

# @pytest.fixture(scope="function")
# def web_user_driver():
#     """Fixture for Web User driver"""
#     driver = None
#     try:
#         driver = AppiumDriver(platform='web', user_type='user')
#         driver.start_driver()
#         yield driver
#     finally:
#         if driver and driver.driver:
#             driver.quit_driver()

# @pytest.fixture(scope="function")
# def web_advisor_driver():
#     """Fixture for Web Advisor driver"""
#     driver = None
#     try:
#         driver = AppiumDriver(platform='web', user_type='advisor')
#         driver.start_driver()
#         yield driver
#     finally:
#         if driver and driver.driver:
#             driver.quit_driver()

@pytest.fixture(scope="function")
def web_advisor():
    """Fixture for Selenium WebDriver Advisor driver using LambdaTest"""
    driver = None
    try:
        driver = WebDriver(browser='Chrome', headless=False)
        driver.start_driver(user_type='advisor')
        yield driver
    finally:
        if driver and driver.driver:
            driver.quit_driver()

@pytest.fixture(scope="function")
def web_user():
    """Fixture for Selenium WebDriver User driver using LambdaTest"""
    driver = None
    try:
        driver = WebDriver(browser='Chrome', headless=False)
        driver.start_driver(user_type='user')
        yield driver
    finally:
        if driver and driver.driver:
            driver.quit_driver()

@pytest.fixture(scope="session")
def test_data():
    """Test data for all test cases"""
    from faker import Faker
    fake = Faker()
    
    return {
        'user': {
            'valid_email': 'ayushp@aa.com',
            'valid_password': 'test123',
            'advisor_name': 'Hubert Blaine',
            'invalid_email': 'invalid@example.com',
            'invalid_password': 'wrongpassword',
            'phone_number': '6666666666',
            'otp': '656565',
            'messageuser': 'Hello,@Hubert. I need your advice 2day!',
            'valid_email_mp': 'basithusain@lambdatest.com',
            'valid_password_mp': '360logica@09',
        },
        'advisor': {
            'valid_email': 'mykhailo.orban+0108001@bargestech.com',
            'valid_password': 'qwerty',
            'invalid_email': 'invalid@example.com',
            'invalid_password': 'wrongpassword',
            'phone_number': '6666666666',
            'otp': '656565',
            'messageadvisor': 'Hello, @Sweet what you want 2day!',
        },
        'creditcard': {
            'card_number': fake.credit_card_number(card_type="visa"),
            'card_expire': fake.credit_card_expire(),
            'card_security_code': fake.credit_card_security_code(card_type="visa"),
            'postcode': fake.postcode(),
            'card_holder_name': fake.name()
        }
    }



