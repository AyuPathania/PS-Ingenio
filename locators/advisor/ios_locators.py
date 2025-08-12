from appium.webdriver.common.appiumby import AppiumBy

class AdvisorIOSLocators:
    """iOS locators for Advisor app"""
    
    # Login Screen
    LOGIN_EMAIL_FIELD = (AppiumBy.ACCESSIBILITY_ID, "email_field")
    LOGIN_PASSWORD_FIELD = (AppiumBy.ACCESSIBILITY_ID, "password_field")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "login_button")
    FORGOT_PASSWORD_LINK = (AppiumBy.ACCESSIBILITY_ID, "forgot_password")
    SIGNUP_LINK = (AppiumBy.ACCESSIBILITY_ID, "signup_link")
    
    # Dashboard Screen
    DASHBOARD_WELCOME_TEXT = (AppiumBy.ACCESSIBILITY_ID, "welcome_text")
    DASHBOARD_MENU_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "menu_button")
    DASHBOARD_NOTIFICATION_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "notification_button")
    DASHBOARD_STATS_CONTAINER = (AppiumBy.ACCESSIBILITY_ID, "stats_container")
    
    # Navigation
    BOTTOM_NAV_DASHBOARD = (AppiumBy.ACCESSIBILITY_ID, "nav_dashboard")
    BOTTOM_NAV_APPOINTMENTS = (AppiumBy.ACCESSIBILITY_ID, "nav_appointments")
    BOTTOM_NAV_CLIENTS = (AppiumBy.ACCESSIBILITY_ID, "nav_clients")
    BOTTOM_NAV_MESSAGES = (AppiumBy.ACCESSIBILITY_ID, "nav_messages")
    BOTTOM_NAV_PROFILE = (AppiumBy.ACCESSIBILITY_ID, "nav_profile")
    
    # Appointments Screen
    APPOINTMENTS_LIST = (AppiumBy.ACCESSIBILITY_ID, "appointments_list")
    APPOINTMENT_ITEM = (AppiumBy.ACCESSIBILITY_ID, "appointment_item")
    NEW_APPOINTMENT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "new_appointment_button")
    APPOINTMENT_DATE_PICKER = (AppiumBy.ACCESSIBILITY_ID, "date_picker")
    APPOINTMENT_TIME_PICKER = (AppiumBy.ACCESSIBILITY_ID, "time_picker")
    
    # Clients Screen
    CLIENTS_LIST = (AppiumBy.ACCESSIBILITY_ID, "clients_list")
    CLIENT_ITEM = (AppiumBy.ACCESSIBILITY_ID, "client_item")
    CLIENT_SEARCH_BAR = (AppiumBy.ACCESSIBILITY_ID, "client_search")
    ADD_CLIENT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "add_client_button")
    
    # Messages Screen
    MESSAGES_LIST = (AppiumBy.ACCESSIBILITY_ID, "messages_list")
    MESSAGE_ITEM = (AppiumBy.ACCESSIBILITY_ID, "message_item")
    NEW_MESSAGE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "new_message_button")
    MESSAGE_INPUT_FIELD = (AppiumBy.ACCESSIBILITY_ID, "message_input")
    MESSAGE_SEND_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "send_message_button")
    
    # Profile Screen
    PROFILE_AVATAR = (AppiumBy.ACCESSIBILITY_ID, "profile_avatar")
    PROFILE_NAME = (AppiumBy.ACCESSIBILITY_ID, "profile_name")
    PROFILE_EMAIL = (AppiumBy.ACCESSIBILITY_ID, "profile_email")
    PROFILE_SPECIALIZATION = (AppiumBy.ACCESSIBILITY_ID, "profile_specialization")
    PROFILE_EDIT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "profile_edit_button")
    PROFILE_LOGOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "profile_logout_button")
    
    # Settings Screen
    SETTINGS_LIST = (AppiumBy.ACCESSIBILITY_ID, "settings_list")
    NOTIFICATION_SETTINGS = (AppiumBy.ACCESSIBILITY_ID, "notification_settings")
    PRIVACY_SETTINGS = (AppiumBy.ACCESSIBILITY_ID, "privacy_settings")
    ABOUT_SECTION = (AppiumBy.ACCESSIBILITY_ID, "about_section")
    
    # Common Elements
    LOADING_SPINNER = (AppiumBy.ACCESSIBILITY_ID, "loading_spinner")
    ERROR_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "error_message")
    SUCCESS_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "success_message")
    CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "confirm_button")
    CANCEL_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "cancel_button")
    SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "save_button")
    
    # iOS Specific Elements
    ALERT_TITLE = (AppiumBy.IOS_PREDICATE, "type == 'XCUIElementTypeAlert'")
    ALERT_MESSAGE = (AppiumBy.IOS_PREDICATE, "type == 'XCUIElementTypeStaticText'")
    ALERT_BUTTON = (AppiumBy.IOS_PREDICATE, "type == 'XCUIElementTypeButton'")
    PICKER_WHEEL = (AppiumBy.CLASS_NAME, "XCUIElementTypePickerWheel")
