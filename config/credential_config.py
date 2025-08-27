import os
from dotenv import load_dotenv
from config.config import Config

# Load environment variables before importing config
load_dotenv()

class CredentialConfig:
    """Configuration class for platform-specific credentials"""
    
    # Platform-specific credential configurations
    PLATFORM_CREDENTIALS = {
        'kasamba': {
            'user': {
                'valid_email': 'kasamba.user@aa.com',
                'valid_password': 'kasamba123',
                'advisor_name': 'Kasamba Advisor',
                'invalid_email': 'invalid@example.com',
                'invalid_password': 'wrongpassword',
                'phone_number': '1111111111',
                'otp': '111111',
                'messageuser': 'Hello, Kasamba Advisor! I need your advice today!',
                'valid_email_mp': 'kasamba.mp@lambdatest.com',
                'valid_password_mp': 'kasamba@09',
            },
            'advisor': {
                'valid_email': 'kasamba.advisor@ingenio.com',
                'valid_password': 'kasamba666',
                'invalid_email': 'invalid@example.com',
                'invalid_password': 'wrongpassword',
                'phone_number': '1111111111',
                'otp': '111111',
                'messageadvisor': 'Hello, Kasamba User! What can I help you with today?',
            }
        },
        'purpelgarden': {
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
                'valid_email': 'anna.benishai+0302@ingenio.com',
                'valid_password': 'test666',
                'invalid_email': 'invalid@example.com',
                'invalid_password': 'wrongpassword',
                'phone_number': '6666666666',
                'otp': '656565',
                'messageadvisor': 'Hello, @Sweet what you want 2day!',
            }
        },
        'purpelocean': {
            'user': {
                'valid_email': 'purpelocean.user@aa.com',
                'valid_password': 'purpelocean123',
                'advisor_name': 'PurpleOcean Advisor',
                'invalid_email': 'invalid@example.com',
                'invalid_password': 'wrongpassword',
                'phone_number': '9999999999',
                'otp': '999999',
                'messageuser': 'Hello, PurpleOcean Advisor! I need your advice today!',
                'valid_email_mp': 'purpelocean.mp@lambdatest.com',
                'valid_password_mp': 'purpelocean@09',
            },
            'advisor': {
                'valid_email': 'purpelocean.advisor@ingenio.com',
                'valid_password': 'purpelocean666',
                'invalid_email': 'invalid@example.com',
                'invalid_password': 'wrongpassword',
                'phone_number': '9999999999',
                'otp': '999999',
                'messageadvisor': 'Hello, PurpleOcean User! What can I help you with today?',
            }
        }
    }
    
    @classmethod
    def get_user_credentials(cls):
        """Get user credentials for the current platform"""
        platform = Config.get_platform()
        return cls.PLATFORM_CREDENTIALS.get(platform, cls.PLATFORM_CREDENTIALS['purpelgarden'])['user']
    
    @classmethod
    def get_advisor_credentials(cls):
        """Get advisor credentials for the current platform"""
        platform = Config.get_platform()
        return cls.PLATFORM_CREDENTIALS.get(platform, cls.PLATFORM_CREDENTIALS['purpelgarden'])['advisor']
    
    @classmethod
    def get_all_credentials(cls):
        """Get all credentials for the current platform"""
        platform = Config.get_platform()
        platform_creds = cls.PLATFORM_CREDENTIALS.get(platform, cls.PLATFORM_CREDENTIALS['purpelgarden'])
        
        return {
            'user': platform_creds['user'],
            'advisor': platform_creds['advisor']
        }
    
    @classmethod
    def get_platform_info(cls):
        """Get information about the current platform credentials"""
        platform = Config.get_platform()
        
        info = {
            'current_platform': platform,
            'user_credentials': cls.get_user_credentials(),
            'advisor_credentials': cls.get_advisor_credentials()
        }
        
        return info
    
    @classmethod
    def get_credential(cls, user_type, credential_key):
        """Get a specific credential for the current platform and user type"""
        if user_type == 'user':
            return cls.get_user_credentials().get(credential_key)
        elif user_type == 'advisor':
            return cls.get_advisor_credentials().get(credential_key)
        else:
            raise ValueError(f"Invalid user_type: {user_type}. Must be 'user' or 'advisor'")
    
    @classmethod
    def get_user_email(cls):
        """Get user email for the current platform"""
        return cls.get_user_credentials()['valid_email']
    
    @classmethod
    def get_user_password(cls):
        """Get user password for the current platform"""
        return cls.get_user_credentials()['valid_password']
    
    @classmethod
    def get_advisor_email(cls):
        """Get advisor email for the current platform"""
        return cls.get_advisor_credentials()['valid_email']
    
    @classmethod
    def get_advisor_password(cls):
        """Get advisor password for the current platform"""
        return cls.get_advisor_credentials()['valid_password']
