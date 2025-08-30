import os
from dotenv import load_dotenv
from config.config import Config

# Load environment variables before importing config
load_dotenv()

class CredentialConfig:
    """Configuration class for platform-specific credentials"""
    
    @classmethod
    def get_platform(cls):
        """Get the current platform from environment variable"""
        return Config.get_platform()
    
    @classmethod
    def get_credentials(cls, platform, test_case, test_data):
        """Get credentials for a specific platform and test case"""
        try:
            return {
                'user': test_data[platform]['user'][test_case],
                'advisor': test_data[platform]['advisor']['Hubert']
            }
        except KeyError:
            return {}
    
    @classmethod
    def get_platform_credentials(cls, test_data):
        """Get all platform credentials using test_data from conftest"""
        platform = cls.get_platform()
        return {
            'kasamba': {
                'tc_01': cls.get_credentials(platform, 'tc_01', test_data),
                'tc_02': cls.get_credentials(platform, 'tc_02', test_data),
                'tc_03': cls.get_credentials(platform, 'tc_03', test_data),
            },
            'purpelgarden': {
                'tc_01': cls.get_credentials(platform, 'tc_01', test_data),
                'tc_02': cls.get_credentials(platform, 'tc_02', test_data),
                'tc_03': cls.get_credentials(platform, 'tc_03', test_data),
            },
            'purpelocean': {
                'tc_01': cls.get_credentials(platform, 'tc_01', test_data),
                'tc_02': cls.get_credentials(platform, 'tc_02', test_data),
                'tc_03': cls.get_credentials(platform, 'tc_03', test_data),
            },
        }

