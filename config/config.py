import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # LambdaTest Configuration
    LAMBDATEST_USERNAME = os.getenv('LT_USERNAME')
    LAMBDATEST_ACCESS_KEY = os.getenv('LT_ACCESS_KEY')
    LAMBDATEST_HUB_URL = os.getenv('LT_HUB_URL', 'mobile-hub.lambdatest.com')
    LAMBDATEST_WEB_HUB_URL = "hub.lambdatest.com"
    
    # Appium Server Configuration (LambdaTest only)
    APPIUM_HOST = 'localhost'  # Not used for LambdaTest
    APPIUM_PORT = 4723  # Not used for LambdaTest
    
    # Platform Configuration (LambdaTest only)
    PLATFORMS = {
        'android': {
            'platformName': 'Android',
            'automationName': 'UiAutomator2'
        },
        'ios': {
            'platformName': 'iOS',
            'automationName': 'XCUITest'
        },
        'web': {
            'browserName': 'Chrome',
            'platformName': 'Windows 11'
        }
    }
    
    # Test Configuration
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    SCREENSHOT_DIR = 'screenshots'
    REPORT_DIR = 'reports'
    
    # User and Advisor App Configuration
    USER_APP = {
        'android': {
            'app': os.getenv('USER_ANDROID_APP_URL', 'lt://APP1234567890'),  # LambdaTest app URL
            'deviceName': os.getenv('USER_ANDROID_DEVICE', 'Galaxy S21'),
            'platformVersion': os.getenv('USER_ANDROID_VERSION', '11.0')
        },
        'ios': {
            'app': os.getenv('USER_IOS_APP_URL', 'lt://APP1234567890'),  # LambdaTest app URL
            'deviceName': os.getenv('USER_IOS_DEVICE', 'iPhone 14'),
            'platformVersion': os.getenv('USER_IOS_VERSION', '16.0')
        },
        'web': {
            'url': os.getenv('USER_WEB_URL', 'https://user.example.com'),
            'browserName': 'chrome',
            'platformName': 'Windows 11'
        }
    }
    
    ADVISOR_APP = {
        'android': {
            'app': os.getenv('ADVISOR_ANDROID_APP_URL', 'lt://APP1234567890'),  # LambdaTest app URL
            'deviceName': os.getenv('ADVISOR_ANDROID_DEVICE', 'Galaxy S22'),
            'platformVersion': os.getenv('ADVISOR_ANDROID_VERSION', '12.0')
        },
        'ios': {
            'app': os.getenv('ADVISOR_IOS_APP_URL', 'lt://APP1234567890'),  # LambdaTest app URL
            'deviceName': os.getenv('ADVISOR_IOS_DEVICE', 'iPhone 14'),
            'platformVersion': os.getenv('ADVISOR_IOS_VERSION', '16.0')
        },
        'web': {
            'url': os.getenv('ADVISOR_WEB_URL', 'https://advisor.example.com'),
            'browserName': 'chrome',
            'platformName': 'Windows 11'
        }
    }
    
    @classmethod
    def get_lambdatest_capabilities(cls, platform, user_type='user'):
        """
        Get LambdaTest capabilities for specific platform and user type
        Using the working structure that was proven successful
        
        Args:
            platform (str): 'android', 'ios', or 'web'
            user_type (str): 'user' or 'advisor'
            
        Returns:
            dict: Complete capabilities dictionary matching working structure
        """
        # Base capabilities that go directly to options object
        capabilities = {}
        
        # Platform-specific capabilities at root level
        if platform in ['android', 'ios']:
            capabilities.update({
                'platformName': cls.PLATFORMS[platform]['platformName'],
                'automationName': cls.PLATFORMS[platform]['automationName']
            })
        else:  # Web
            capabilities.update({
                'browserName': cls.PLATFORMS[platform]['browserName'],
                'platformName': cls.PLATFORMS[platform]['platformName']
            })
        
        # LT:Options with all the detailed capabilities (like working structure)
        lt_options = {
            'name': f'{platform.title()} {user_type.title()} Test',
            'build': 'WebAndMobile',
            'user': cls.LAMBDATEST_USERNAME,
            'accessKey': cls.LAMBDATEST_ACCESS_KEY,
            'newCommandTimeout': 86400,
            'idleTimeout': 1500,
            'useJSONSource': True,
            'w3c': True,
            'allowInvisibleElements': True,
            'ignoreUnimportantViews': True,
            'unicodeKeyboard': False,
            'autoGrantPermissions': True,
            'isRealMobile': True,
            'privateCloud': False,
            'autoAcceptAlerts': True,
            'visual': True,
            'video': True
        }
        
        # Add platform-specific capabilities to LT:Options
        if platform in ['android', 'ios']:
            # Add app-specific capabilities
            app_config = cls.USER_APP[platform] if user_type == 'user' else cls.ADVISOR_APP[platform]
            lt_options.update(app_config)
            
            # Add platform capabilities to LT:Options as well
            lt_options.update({
                'platformName': cls.PLATFORMS[platform]['platformName'],
                'automationName': cls.PLATFORMS[platform]['automationName']
            })
        else:  # Web
            # For web, add browser capabilities to LT:Options
            lt_options.update({
                'browserName': cls.PLATFORMS[platform]['browserName'],
                'platformName': cls.PLATFORMS[platform]['platformName']
            })
        
        # Add LT:Options to capabilities
        capabilities['LT:Options'] = lt_options
        
        return capabilities
    
    @classmethod
    def get_lambdatest_url(cls, platform='mobile'):
        """Get LambdaTest hub URL with credentials"""
        if platform == 'web':
            hub_url = cls.LAMBDATEST_WEB_HUB_URL
        else:
            hub_url = cls.LAMBDATEST_HUB_URL
            
        return "https://{}:{}@{}/wd/hub".format(
            cls.LAMBDATEST_USERNAME, 
            cls.LAMBDATEST_ACCESS_KEY, 
            hub_url
        )
    
    @classmethod
    def get_local_appium_url(cls):
        """Get local Appium server URL (not used for LambdaTest)"""
        return f"http://{cls.APPIUM_HOST}:{cls.APPIUM_PORT}/wd/hub"
    
    @classmethod
    def is_lambdatest_enabled(cls):
        """Check if LambdaTest is enabled (has credentials)"""
        return (cls.LAMBDATEST_USERNAME is not None and 
                cls.LAMBDATEST_ACCESS_KEY is not None)
