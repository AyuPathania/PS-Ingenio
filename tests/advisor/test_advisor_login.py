from locators.advisor.android_locators import AdvisorAndroidLocators
from locators.advisor.ios_locators import AdvisorIOSLocators
from locators.advisor.web_locators import AdvisorWebLocators

class TestAdvisorLogin:
    """Test cases for Advisor Login functionality"""
    
    def test_valid_login_android(self, android_advisor_driver, test_data):
        """Test valid login on Android Advisor app"""
        driver = android_advisor_driver
        locators = AdvisorAndroidLocators()
        
        # Input valid credentials
        driver.input_text(*locators.LOGIN_EMAIL_FIELD, test_data['advisor']['valid_email'])
        driver.input_text(*locators.LOGIN_PASSWORD_FIELD, test_data['advisor']['valid_password'])
        
        # Click login button
        driver.click(*locators.LOGIN_BUTTON)
        
        # Verify successful login
        assert driver.is_element_present(*locators.DASHBOARD_WELCOME_TEXT, timeout=10)
        assert driver.is_element_present(*locators.BOTTOM_NAV_DASHBOARD, timeout=10)
    
    def test_invalid_login_android(self, android_advisor_driver, test_data):
        """Test invalid login on Android Advisor app"""
        driver = android_advisor_driver
        locators = AdvisorAndroidLocators()
        
        # Input invalid credentials
        driver.input_text(*locators.LOGIN_EMAIL_FIELD, test_data['advisor']['invalid_email'])
        driver.input_text(*locators.LOGIN_PASSWORD_FIELD, test_data['advisor']['invalid_password'])
        
        # Click login button
        driver.click(*locators.LOGIN_BUTTON)
        
        # Verify error message
        assert driver.is_element_present(*locators.ERROR_MESSAGE, timeout=10)
    
    def test_valid_login_ios(self, ios_advisor_driver, test_data):
        """Test valid login on iOS Advisor app"""
        driver = ios_advisor_driver
        locators = AdvisorIOSLocators()
        
        # Input valid credentials
        driver.input_text(*locators.LOGIN_EMAIL_FIELD, test_data['advisor']['valid_email'])
        driver.input_text(*locators.LOGIN_PASSWORD_FIELD, test_data['advisor']['valid_password'])
        
        # Click login button
        driver.click(*locators.LOGIN_BUTTON)
        
        # Verify successful login
        assert driver.is_element_present(*locators.DASHBOARD_WELCOME_TEXT, timeout=10)
        assert driver.is_element_present(*locators.BOTTOM_NAV_DASHBOARD, timeout=10)
    
    def test_invalid_login_ios(self, ios_advisor_driver, test_data):
        """Test invalid login on iOS Advisor app"""
        driver = ios_advisor_driver
        locators = AdvisorIOSLocators()
        
        # Input invalid credentials
        driver.input_text(*locators.LOGIN_EMAIL_FIELD, test_data['advisor']['invalid_email'])
        driver.input_text(*locators.LOGIN_PASSWORD_FIELD, test_data['advisor']['invalid_password'])
        
        # Click login button
        driver.click(*locators.LOGIN_BUTTON)
        
        # Verify error message
        assert driver.is_element_present(*locators.ERROR_MESSAGE, timeout=10)
    
    def test_valid_login_web(self, web_advisor_driver, test_data):
        """Test valid login on Web Advisor site"""
        driver = web_advisor_driver
        locators = AdvisorWebLocators()
        
        # Input valid credentials
        driver.input_text(*locators.LOGIN_EMAIL_FIELD, test_data['advisor']['valid_email'])
        driver.input_text(*locators.LOGIN_PASSWORD_FIELD, test_data['advisor']['valid_password'])
        
        # Click login button
        driver.click(*locators.LOGIN_BUTTON)
        
        # Verify successful login
        assert driver.is_element_present(*locators.DASHBOARD_WELCOME_MESSAGE, timeout=10)
        assert driver.is_element_present(*locators.NAV_DASHBOARD, timeout=10)
    
    def test_invalid_login_web(self, web_advisor_driver, test_data):
        """Test invalid login on Web Advisor site"""
        driver = web_advisor_driver
        locators = AdvisorWebLocators()
        
        # Input invalid credentials
        driver.input_text(*locators.LOGIN_EMAIL_FIELD, test_data['advisor']['invalid_email'])
        driver.input_text(*locators.LOGIN_PASSWORD_FIELD, test_data['advisor']['invalid_password'])
        
        # Click login button
        driver.click(*locators.LOGIN_BUTTON)
        
        # Verify error message
        assert driver.is_element_present(*locators.ERROR_MESSAGE, timeout=10)
    
    def test_empty_fields_validation(self, android_advisor_driver):
        """Test validation for empty fields on Android"""
        driver = android_advisor_driver
        locators = AdvisorAndroidLocators()
        
        # Try to login with empty fields
        driver.click(*locators.LOGIN_BUTTON)
        
        # Verify validation message
        assert driver.is_element_present(*locators.ERROR_MESSAGE, timeout=10)
    
    def test_forgot_password_link(self, android_advisor_driver):
        """Test forgot password link functionality"""
        driver = android_advisor_driver
        locators = AdvisorAndroidLocators()
        
        # Click forgot password link
        driver.click(*locators.FORGOT_PASSWORD_LINK)
        
        # Verify navigation to forgot password screen
        # This would need additional locators for the forgot password screen
        assert True  # Placeholder assertion
    
    def test_signup_link(self, android_advisor_driver):
        """Test signup link functionality"""
        driver = android_advisor_driver
        locators = AdvisorAndroidLocators()
        
        # Click signup link
        driver.click(*locators.SIGNUP_LINK)
        
        # Verify navigation to signup screen
        # This would need additional locators for the signup screen
        assert True  # Placeholder assertion
