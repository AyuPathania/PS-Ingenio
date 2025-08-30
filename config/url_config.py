import os
from dotenv import load_dotenv
from config.config import Config

# Load environment variables before importing config
load_dotenv()

class URLConfig:
    """Configuration class for platform-specific URLs"""
    
    # Platform-specific URL configurations
    PLATFORM_URLS = {
        'kasamba': {
            'user': {
                'base_url': 'https://st:purplestage@staging.purplegarden.co/',
                'login_url': 'https://staging.purplegarden.co/',
                'signup_url': 'https://kasamba.user.signupurl.com/'
            },
            'advisor': {
                'base_url': 'https://kasamba.advisor.baseurl.com/',
                'login_url': 'https://kasamba.advisor.loginurl.com/',
                'signup_url': 'https://kasamba.advisor.signupurl.com/'
            }
        },
        'purpelgarden': {
            'user': {
                'base_url': 'https://st:purplestage@staging.purplegarden.co/',
                'login_url': 'https://staging.purplegarden.co/',
                'signup_url': 'https://purplegarden.user.signupurl.com/'
            },
            'advisor': {
                'base_url': 'https://purplegarden.advisor.baseurl.com/',
                'login_url': 'https://stg-expert.purpleocean.co/sign-in',
                'signup_url': 'https://purplegarden.advisor.signupurl.com/'
            }
        },
        'purpelocean': {
            'user': {
                'base_url': 'https://purpleocean.user.baseurl.com/',
                'login_url': 'https://purpleocean.user.loginurl.com/',
                'signup_url': 'https://purpleocean.user.signupurl.com/'
            },
            'advisor': {
                'base_url': 'https://purpleocean.advisor.baseurl.com/',
                'login_url': 'https://purpleocean.advisor.loginurl.com/',
                'signup_url': 'https://purpleocean.advisor.signupurl.com/'
            }
        }
    }
    
    @classmethod
    def get_user_urls(cls):
        """Get user URLs for the current platform"""
        platform = Config.get_platform()
        return cls.PLATFORM_URLS.get(platform, cls.PLATFORM_URLS['kasamba'])['user']
    
    @classmethod
    def get_advisor_urls(cls):
        """Get advisor URLs for the current platform"""
        platform = Config.get_platform()
        return cls.PLATFORM_URLS.get(platform, cls.PLATFORM_URLS['kasamba'])['advisor']
    
    @classmethod
    def get_user_base_url(cls):
        """Get user base URL for the current platform"""
        return cls.get_user_urls()['base_url']
    
    @classmethod
    def get_user_login_url(cls):
        """Get user login URL for the current platform"""
        return cls.get_user_urls()['login_url']
    
    @classmethod
    def get_user_signup_url(cls):
        """Get user signup URL for the current platform"""
        return cls.get_user_urls()['signup_url']
    
    @classmethod
    def get_advisor_base_url(cls):
        """Get advisor base URL for the current platform"""
        return cls.get_advisor_urls()['base_url']
    
    @classmethod
    def get_advisor_login_url(cls):
        """Get advisor login URL for the current platform"""
        return cls.get_advisor_urls()['login_url']
    
    @classmethod
    def get_advisor_signup_url(cls):
        """Get advisor signup URL for the current platform"""
        return cls.get_advisor_urls()['signup_url']
    
    @classmethod
    def get_platform_info(cls):
        """Get information about the current platform URLs"""
        platform = Config.get_platform()
        
        info = {
            'current_platform': platform,
            'user_urls': cls.get_user_urls(),
            'advisor_urls': cls.get_advisor_urls()
        }
        
        return info
