import importlib
from dotenv import load_dotenv
from config.config import Config

# Load environment variables before importing config
load_dotenv()

class LocatorFactory:
    """Factory class for dynamically loading platform-specific web locators"""
    
    @classmethod
    def _get_platform_module_path(cls, platform, user_type):
        """Get the module path for the specified platform and user type"""
        # Normalize platform name for file paths
        if platform == 'purpelgarden':
            platform_path = 'PurpelGarden'
        elif platform == 'purpelocean':
            platform_path = 'PurpelOcean'
        else:
            platform_path = platform
            
        # Handle inconsistent file naming across platforms
        if platform == 'purpelgarden':
            file_name = 'web_locators.py'  # PurpelGarden uses plural
        else:
            file_name = 'web_locator.py'   # kasamba and PurpelOcean use singular
            
        # Remove .py extension for import
        module_name = file_name.replace('.py', '')
        return f"locators.{platform_path}.{user_type}.{module_name}"
    
    @classmethod
    def _get_locator_class_name(cls, platform, user_type):
        """Get the class name for the specified platform and user type"""
        # Normalize platform name for class names
        if platform == 'purpelgarden':
            platform_class = 'PurpelGarden'
        elif platform == 'purpelocean':
            platform_class = 'PurpelOcean'
        else:
            platform_class = platform.capitalize()
            
        # Normalize user type for class names
        user_type_class = user_type.capitalize()
        
        return f"{platform_class}{user_type_class}WebLocators"
    
    @classmethod
    def _import_locator_class(cls, platform, user_type):
        """Import the web locator class for the specified platform and user type"""
        try:
            module_path = cls._get_platform_module_path(platform, user_type)
            class_name = cls._get_locator_class_name(platform, user_type)
            
            # Import the module
            module = importlib.import_module(module_path)
            
            # Get the class from the module
            locator_class = getattr(module, class_name)
            
            return locator_class
            
        except (ImportError, AttributeError) as e:
            raise ImportError(
                f"Failed to import web locator class for {platform}/{user_type}: {e}"
            )
    
    @classmethod
    def get_advisor_web_locators(cls):
        """Get advisor web locators for the current platform"""
        platform = Config.get_platform()
        return cls._import_locator_class(platform, 'advisor')
    
    @classmethod
    def get_user_web_locators(cls):
        """Get user web locators for the current platform"""
        platform = Config.get_platform()
        return cls._import_locator_class(platform, 'user')
    
    @classmethod
    def get_platform_info(cls):
        """Get information about the current platform"""
        platform = Config.get_platform()
        
        info = {
            'current_platform': platform,
            'platform_uppercase': platform.upper(),
            'is_kasamba': Config.is_kasamba(),
            'is_purpelgarden': Config.is_purpelgarden(),
            'is_purpelocean': Config.is_purpelocean()
        }
        
        return info
