import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from drivers.appium_driver import AppiumDriver
from drivers.web_driver import WebDriver
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
    return {
        'user': {
            'valid_email': 'anna.benishai+2705qa@ingenio.com',
            'valid_password': 'test123',
            'invalid_email': 'invalid@example.com',
            'invalid_password': 'wrongpassword',
            'phone_number': '6666666666',
            'otp': '656565',
            'messageuser': 'Hello, I need your advice!',
            'valid_email_mp': 'basithusain@lambdatest.com',
            'valid_password_mp': '360logica@09',
        },
        'advisor': {
            'valid_email': 'anna.benishai+0302@ingenio.com',
            'valid_password': 'test666',
            'invalid_email': 'invalid@example.com',
            'invalid_password': 'wrongpassword',
            'phone_number': '6666666666',
            'otp': '656565',
            'messageadvisor': 'Hello, what you want!',
        },
        'gmail': {
            'email': 'ayushlambdatest',
            'password': '@Ayush0703',
            
        }
    }


