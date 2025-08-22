import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from drivers.appium_driver import AppiumDriver
from drivers.web_driver import WebDriver
from config.config import Config
from faker import Faker

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
            'advisor_name': 'tetsLanguageOrder',
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


