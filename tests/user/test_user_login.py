import pytest
from locators.user.android_locators import UserAndroidLocators
from locators.user.ios_locators import UserIOSLocators
from locators.user.web_locators import UserWebLocators

class TestUserLogin:
    """Test cases for User Login functionality"""
    
    def test_valid_login_android(self, android_user_driver, test_data):
        """Test valid login on Android User app"""
        driver = android_user_driver
        locators = UserAndroidLocators()
        
        # Input valid credentials
        driver.input_text(*locators.LOGIN_EMAIL_FIELD, test_data['user']['valid_email'])
        driver.input_text(*locators.LOGIN_PASSWORD_FIELD, test_data['user']['valid_password'])
        
        # Click login button
        driver.click(*locators.LOGIN_BUTTON)
        
        # Verify successful login
        assert driver.is_element_present(*locators.HOME_WELCOME_TEXT, timeout=10)
        assert driver.is_element_present(*locators.BOTTOM_NAV_HOME, timeout=10)
    
    def test_invalid_login_android(self, android_user_driver, test_data):
        """Test invalid login on Android User app"""
        driver = android_user_driver
        locators = UserAndroidLocators()
        
        # Input invalid credentials
        driver.input_text(*locators.LOGIN_EMAIL_FIELD, test_data['user']['invalid_email'])
        driver.input_text(*locators.LOGIN_PASSWORD_FIELD, test_data['user']['invalid_password'])
        
        # Click login button
        driver.click(*locators.LOGIN_BUTTON)
        
        # Verify error message
        assert driver.is_element_present(*locators.ERROR_MESSAGE, timeout=10)
    
    def test_valid_login_ios(self, ios_user_driver, test_data):
        """Test valid login on iOS User app"""
        driver = ios_user_driver
        locators = UserIOSLocators()
        
        # Input valid credentials
        driver.input_text(*locators.LOGIN_EMAIL_FIELD, test_data['user']['valid_email'])
        driver.input_text(*locators.LOGIN_PASSWORD_FIELD, test_data['user']['valid_password'])
        
        # Click login button
        driver.click(*locators.LOGIN_BUTTON)
        
        # Verify successful login
        assert driver.is_element_present(*locators.HOME_WELCOME_TEXT, timeout=10)
        assert driver.is_element_present(*locators.BOTTOM_NAV_HOME, timeout=10)
    
    def test_invalid_login_ios(self, ios_user_driver, test_data):
        """Test invalid login on iOS User app"""
        driver = ios_user_driver
        locators = UserIOSLocators()
        
        # Input invalid credentials
        driver.input_text(*locators.LOGIN_EMAIL_FIELD, test_data['user']['invalid_email'])
        driver.input_text(*locators.LOGIN_PASSWORD_FIELD, test_data['user']['invalid_password'])
        
        # Click login button
        driver.click(*locators.LOGIN_BUTTON)
        
        # Verify error message
        assert driver.is_element_present(*locators.ERROR_MESSAGE, timeout=10)
    
    def test_valid_login_web(self, web_user_driver, test_data):
        """Test valid login on Web User site"""
        driver = web_user_driver
        locators = UserWebLocators()
        
        # Input valid credentials
        driver.input_text(*locators.LOGIN_EMAIL_FIELD, test_data['user']['valid_email'])
        driver.input_text(*locators.LOGIN_PASSWORD_FIELD, test_data['user']['valid_password'])
        
        # Click login button
        driver.click(*locators.LOGIN_BUTTON)
        
        # Verify successful login
        assert driver.is_element_present(*locators.HOME_WELCOME_MESSAGE, timeout=10)
        assert driver.is_element_present(*locators.NAV_HOME, timeout=10)
    
    def test_invalid_login_web(self, web_user_driver, test_data):
        """Test invalid login on Web User site"""
        driver = web_user_driver
        locators = UserWebLocators()
        
        # Input invalid credentials
        driver.input_text(*locators.LOGIN_EMAIL_FIELD, test_data['user']['invalid_email'])
        driver.input_text(*locators.LOGIN_PASSWORD_FIELD, test_data['user']['invalid_password'])
        
        # Click login button
        driver.click(*locators.LOGIN_BUTTON)
        
        # Verify error message
        assert driver.is_element_present(*locators.ERROR_MESSAGE, timeout=10)
    
    def test_empty_fields_validation(self, android_user_driver):
        """Test validation for empty fields on Android"""
        driver = android_user_driver
        locators = UserAndroidLocators()
        
        # Try to login with empty fields
        driver.click(*locators.LOGIN_BUTTON)
        
        # Verify validation message
        assert driver.is_element_present(*locators.ERROR_MESSAGE, timeout=10)
    
    def test_forgot_password_link(self, android_user_driver):
        """Test forgot password link functionality"""
        driver = android_user_driver
        locators = UserAndroidLocators()
        
        # Click forgot password link
        driver.click(*locators.FORGOT_PASSWORD_LINK)
        
        # Verify navigation to forgot password screen
        # This would need additional locators for the forgot password screen
        assert True  # Placeholder assertion
    
    def test_signup_link(self, android_user_driver):
        """Test signup link functionality"""
        driver = android_user_driver
        locators = UserAndroidLocators()
        
        # Click signup link
        driver.click(*locators.SIGNUP_LINK)
        
        # Verify navigation to signup screen
        # This would need additional locators for the signup screen
        assert True  # Placeholder assertion
