import pytest
from core.appium_driver import AppiumDriver
from config.config import Config

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

@pytest.fixture(scope="function")
def web_user_driver():
    """Fixture for Web User driver"""
    driver = None
    try:
        driver = AppiumDriver(platform='web', user_type='user')
        driver.start_driver()
        yield driver
    finally:
        if driver and driver.driver:
            driver.quit_driver()

@pytest.fixture(scope="function")
def web_advisor_driver():
    """Fixture for Web Advisor driver"""
    driver = None
    try:
        driver = AppiumDriver(platform='web', user_type='advisor')
        driver.start_driver()
        yield driver
    finally:
        if driver and driver.driver:
            driver.quit_driver()

@pytest.fixture(scope="session")
def test_data():
    """Test data for all test cases"""
    return {
        'user': {
            'valid_email': 'user@example.com',
            'valid_password': 'password123',
            'invalid_email': 'invalid@example.com',
            'invalid_password': 'wrongpassword',
            'phone_number': '6666666666',
            'otp': '656565'
        },
        'advisor': {
            'valid_email': 'advisor@example.com',
            'valid_password': 'advisor123',
            'invalid_email': 'invalid@example.com',
            'invalid_password': 'wrongpassword',
            'phone_number': '6666666666',
            'otp': '656565'
        }
    }


