from appium.webdriver.common.appiumby import AppiumBy

class UserIOSLocators:
    """iOS locators for User app"""
    
    # Login Screen
    LOGIN_EMAIL_FIELD = (AppiumBy.ACCESSIBILITY_ID, "email_field")
    LOGIN_PASSWORD_FIELD = (AppiumBy.ACCESSIBILITY_ID, "password_field")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "login_button")
    FORGOT_PASSWORD_LINK = (AppiumBy.ACCESSIBILITY_ID, "forgot_password")
    SIGNUP_LINK = (AppiumBy.ACCESSIBILITY_ID, "signup_link")
    
    # Home Screen
    HOME_WELCOME_TEXT = (AppiumBy.ACCESSIBILITY_ID, "welcome_text")
    HOME_MENU_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "menu_button")
    HOME_SEARCH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "search_button")
    HOME_NOTIFICATION_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "notification_button")
    
    # Navigation
    BOTTOM_NAV_HOME = (AppiumBy.ACCESSIBILITY_ID, "nav_home")
    BOTTOM_NAV_PROFILE = (AppiumBy.ACCESSIBILITY_ID, "nav_profile")
    BOTTOM_NAV_BOOKINGS = (AppiumBy.ACCESSIBILITY_ID, "nav_bookings")
    BOTTOM_NAV_MESSAGES = (AppiumBy.ACCESSIBILITY_ID, "nav_messages")
    
    # Profile Screen
    PROFILE_AVATAR = (AppiumBy.ACCESSIBILITY_ID, "profile_avatar")
    PROFILE_NAME = (AppiumBy.ACCESSIBILITY_ID, "profile_name")
    PROFILE_EMAIL = (AppiumBy.ACCESSIBILITY_ID, "profile_email")
    PROFILE_EDIT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "profile_edit_button")
    PROFILE_LOGOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "profile_logout_button")
    
    # Bookings Screen
    BOOKINGS_LIST = (AppiumBy.ACCESSIBILITY_ID, "bookings_list")
    BOOKING_ITEM = (AppiumBy.ACCESSIBILITY_ID, "booking_item")
    NEW_BOOKING_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "new_booking_button")
    
    # Messages Screen
    MESSAGES_LIST = (AppiumBy.ACCESSIBILITY_ID, "messages_list")
    MESSAGE_ITEM = (AppiumBy.ACCESSIBILITY_ID, "message_item")
    NEW_MESSAGE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "new_message_button")
    
    # Common Elements
    LOADING_SPINNER = (AppiumBy.ACCESSIBILITY_ID, "loading_spinner")
    ERROR_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "error_message")
    SUCCESS_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "success_message")
    CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "confirm_button")
    CANCEL_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "cancel_button")
    
    # iOS Specific Elements
    ALERT_TITLE = (AppiumBy.IOS_PREDICATE, "type == 'XCUIElementTypeAlert'")
    ALERT_MESSAGE = (AppiumBy.IOS_PREDICATE, "type == 'XCUIElementTypeStaticText'")
    ALERT_BUTTON = (AppiumBy.IOS_PREDICATE, "type == 'XCUIElementTypeButton'")
