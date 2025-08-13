from appium.webdriver.common.appiumby import AppiumBy

class UserAndroidLocators:
    """Android locators for User app"""
    
    # Login Screen
    LOGIN_EMAIL_FIELD = (AppiumBy.ID, "com.example.userapp:id/email_field")
    LOGIN_PASSWORD_FIELD = (AppiumBy.ID, "com.example.userapp:id/password_field")
    LOGIN_BUTTON = (AppiumBy.ID, "com.example.userapp:id/login_button")
    FORGOT_PASSWORD_LINK = (AppiumBy.ID, "com.example.userapp:id/forgot_password")
    SIGNUP_LINK = (AppiumBy.ID, "com.example.userapp:id/signup_link")
    
    
    # Home Screen
    HOME_WELCOME_TEXT = (AppiumBy.ID, "com.example.userapp:id/welcome_text")
    HOME_MENU_BUTTON = (AppiumBy.ID, "com.example.userapp:id/menu_button")
    HOME_SEARCH_BUTTON = (AppiumBy.ID, "com.example.userapp:id/search_button")
    HOME_NOTIFICATION_BUTTON = (AppiumBy.ID, "com.example.userapp:id/notification_button")
    
    # Navigation
    BOTTOM_NAV_HOME = (AppiumBy.ID, "com.example.userapp:id/nav_home")
    BOTTOM_NAV_PROFILE = (AppiumBy.ID, "com.example.userapp:id/nav_profile")
    BOTTOM_NAV_BOOKINGS = (AppiumBy.ID, "com.example.userapp:id/nav_bookings")
    BOTTOM_NAV_MESSAGES = (AppiumBy.ID, "com.example.userapp:id/nav_messages")
    
    # Profile Screen
    PROFILE_AVATAR = (AppiumBy.ID, "com.example.userapp:id/profile_avatar")
    PROFILE_NAME = (AppiumBy.ID, "com.example.userapp:id/profile_name")
    PROFILE_EMAIL = (AppiumBy.ID, "com.example.userapp:id/profile_email")
    PROFILE_EDIT_BUTTON = (AppiumBy.ID, "com.example.userapp:id/profile_edit_button")
    PROFILE_LOGOUT_BUTTON = (AppiumBy.ID, "com.example.userapp:id/profile_logout_button")
    
    # Bookings Screen
    BOOKINGS_LIST = (AppiumBy.ID, "com.example.userapp:id/bookings_list")
    BOOKING_ITEM = (AppiumBy.ID, "com.example.userapp:id/booking_item")
    NEW_BOOKING_BUTTON = (AppiumBy.ID, "com.example.userapp:id/new_booking_button")
    
    # Messages Screen
    MESSAGES_LIST = (AppiumBy.ID, "com.example.userapp:id/messages_list")
    MESSAGE_ITEM = (AppiumBy.ID, "com.example.userapp:id/message_item")
    NEW_MESSAGE_BUTTON = (AppiumBy.ID, "com.example.userapp:id/new_message_button")
    
    # Common Elements
    LOADING_SPINNER = (AppiumBy.ID, "com.example.userapp:id/loading_spinner")
    ERROR_MESSAGE = (AppiumBy.ID, "com.example.userapp:id/error_message")
    SUCCESS_MESSAGE = (AppiumBy.ID, "com.example.userapp:id/success_message")
    CONFIRM_BUTTON = (AppiumBy.ID, "com.example.userapp:id/confirm_button")
    CANCEL_BUTTON = (AppiumBy.ID, "com.example.userapp:id/cancel_button")
