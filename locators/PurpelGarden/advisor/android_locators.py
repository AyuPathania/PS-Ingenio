from appium.webdriver.common.appiumby import AppiumBy

class AdvisorAndroidLocators:
    """Android locators for Advisor app"""
    
    # Login Screen
    LOGIN_EMAIL_FIELD = (AppiumBy.ID, "com.example.advisorapp:id/email_field")
    LOGIN_PASSWORD_FIELD = (AppiumBy.ID, "com.example.advisorapp:id/password_field")
    LOGIN_BUTTON = (AppiumBy.ID, "com.example.advisorapp:id/login_button")
    FORGOT_PASSWORD_LINK = (AppiumBy.ID, "com.example.advisorapp:id/forgot_password")
    SIGNUP_LINK = (AppiumBy.ID, "com.example.advisorapp:id/signup_link")
    
    # Dashboard Screen
    DASHBOARD_WELCOME_TEXT = (AppiumBy.ID, "com.example.advisorapp:id/welcome_text")
    DASHBOARD_MENU_BUTTON = (AppiumBy.ID, "com.example.advisorapp:id/menu_button")
    DASHBOARD_NOTIFICATION_BUTTON = (AppiumBy.ID, "com.example.advisorapp:id/notification_button")
    DASHBOARD_STATS_CONTAINER = (AppiumBy.ID, "com.example.advisorapp:id/stats_container")
    
    # Navigation
    BOTTOM_NAV_DASHBOARD = (AppiumBy.ID, "com.example.advisorapp:id/nav_dashboard")
    BOTTOM_NAV_APPOINTMENTS = (AppiumBy.ID, "com.example.advisorapp:id/nav_appointments")
    BOTTOM_NAV_CLIENTS = (AppiumBy.ID, "com.example.advisorapp:id/nav_clients")
    BOTTOM_NAV_MESSAGES = (AppiumBy.ID, "com.example.advisorapp:id/nav_messages")
    BOTTOM_NAV_PROFILE = (AppiumBy.ID, "com.example.advisorapp:id/nav_profile")
    
    # Appointments Screen
    APPOINTMENTS_LIST = (AppiumBy.ID, "com.example.advisorapp:id/appointments_list")
    APPOINTMENT_ITEM = (AppiumBy.ID, "com.example.advisorapp:id/appointment_item")
    NEW_APPOINTMENT_BUTTON = (AppiumBy.ID, "com.example.advisorapp:id/new_appointment_button")
    APPOINTMENT_DATE_PICKER = (AppiumBy.ID, "com.example.advisorapp:id/date_picker")
    APPOINTMENT_TIME_PICKER = (AppiumBy.ID, "com.example.advisorapp:id/time_picker")
    
    # Clients Screen
    CLIENTS_LIST = (AppiumBy.XPATH, "com.example.advisorapp:id/clients_list")
    CLIENT_ITEM = (AppiumBy.ID, "com.example.advisorapp:id/client_item")
    CLIENT_SEARCH_BAR = (AppiumBy.ID, "com.example.advisorapp:id/client_search")
    ADD_CLIENT_BUTTON = (AppiumBy.ID, "com.example.advisorapp:id/add_client_button")
    
    # Messages Screen
    MESSAGES_LIST = (AppiumBy.ID, "com.example.advisorapp:id/messages_list")
    MESSAGE_ITEM = (AppiumBy.ID, "com.example.advisorapp:id/message_item")
    NEW_MESSAGE_BUTTON = (AppiumBy.ID, "com.example.advisorapp:id/new_message_button")
    MESSAGE_INPUT_FIELD = (AppiumBy.ID, "com.example.advisorapp:id/message_input")
    MESSAGE_SEND_BUTTON = (AppiumBy.ID, "com.example.advisorapp:id/send_message_button")
    
    # Profile Screen
    PROFILE_AVATAR = (AppiumBy.ID, "com.example.advisorapp:id/profile_avatar")
    PROFILE_NAME = (AppiumBy.ID, "com.example.advisorapp:id/profile_name")
    PROFILE_EMAIL = (AppiumBy.ID, "com.example.advisorapp:id/profile_email")
    PROFILE_SPECIALIZATION = (AppiumBy.ID, "com.example.advisorapp:id/profile_specialization")
    PROFILE_EDIT_BUTTON = (AppiumBy.ID, "com.example.advisorapp:id/profile_edit_button")
    PROFILE_LOGOUT_BUTTON = (AppiumBy.ID, "com.example.advisorapp:id/profile_logout_button")
    
    # Settings Screen
    SETTINGS_LIST = (AppiumBy.ID, "com.example.advisorapp:id/settings_list")
    NOTIFICATION_SETTINGS = (AppiumBy.ID, "com.example.advisorapp:id/notification_settings")
    PRIVACY_SETTINGS = (AppiumBy.ID, "com.example.advisorapp:id/privacy_settings")
    ABOUT_SECTION = (AppiumBy.ID, "com.example.advisorapp:id/about_section")
    
    # Common Elements
    LOADING_SPINNER = (AppiumBy.ID, "com.example.advisorapp:id/loading_spinner")
    ERROR_MESSAGE = (AppiumBy.ID, "com.example.advisorapp:id/error_message")
    SUCCESS_MESSAGE = (AppiumBy.ID, "com.example.advisorapp:id/success_message")
    CONFIRM_BUTTON = (AppiumBy.ID, "com.example.advisorapp:id/confirm_button")
    CANCEL_BUTTON = (AppiumBy.ID, "com.example.advisorapp:id/cancel_button")
    SAVE_BUTTON = (AppiumBy.ID, "com.example.advisorapp:id/save_button")
