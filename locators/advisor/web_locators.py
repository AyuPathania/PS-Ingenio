from selenium.webdriver.common.by import By

class AdvisorWebLocators:
    """Web locators for Advisor website"""
    
    # Login Page
    LOGIN_EMAIL_FIELD = (By.ID, "advisor-email")
    LOGIN_PASSWORD_FIELD = (By.ID, "advisor-password")
    LOGIN_BUTTON = (By.ID, "login-submit")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot Password?")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign Up")
    REMEMBER_ME_CHECKBOX = (By.ID, "remember-me")
    
    # Dashboard Page
    DASHBOARD_HEADER = (By.TAG_NAME, "h1")
    DASHBOARD_WELCOME_MESSAGE = (By.CLASS_NAME, "welcome-message")
    DASHBOARD_STATS_CONTAINER = (By.CLASS_NAME, "stats-container")
    DASHBOARD_NOTIFICATION_ICON = (By.CLASS_NAME, "notification-icon")
    DASHBOARD_MENU_BUTTON = (By.CLASS_NAME, "menu-button")
    
    # Navigation
    NAV_DASHBOARD = (By.LINK_TEXT, "Dashboard")
    NAV_APPOINTMENTS = (By.LINK_TEXT, "Appointments")
    NAV_CLIENTS = (By.LINK_TEXT, "Clients")
    NAV_MESSAGES = (By.LINK_TEXT, "Messages")
    NAV_PROFILE = (By.LINK_TEXT, "Profile")
    NAV_SETTINGS = (By.LINK_TEXT, "Settings")
    NAV_LOGOUT = (By.LINK_TEXT, "Logout")
    
    # Appointments Page
    APPOINTMENTS_CONTAINER = (By.CLASS_NAME, "appointments-container")
    APPOINTMENT_CARD = (By.CLASS_NAME, "appointment-card")
    NEW_APPOINTMENT_BUTTON = (By.ID, "new-appointment-btn")
    APPOINTMENT_DATE_FIELD = (By.ID, "appointment-date")
    APPOINTMENT_TIME_FIELD = (By.ID, "appointment-time")
    APPOINTMENT_CLIENT_FIELD = (By.ID, "appointment-client")
    APPOINTMENT_SUBMIT_BUTTON = (By.ID, "submit-appointment-btn")
    
    # Clients Page
    CLIENTS_CONTAINER = (By.CLASS_NAME, "clients-container")
    CLIENT_CARD = (By.CLASS_NAME, "client-card")
    CLIENT_SEARCH_BAR = (By.ID, "client-search")
    ADD_CLIENT_BUTTON = (By.ID, "add-client-btn")
    CLIENT_NAME_FIELD = (By.ID, "client-name")
    CLIENT_EMAIL_FIELD = (By.ID, "client-email")
    CLIENT_PHONE_FIELD = (By.ID, "client-phone")
    CLIENT_SAVE_BUTTON = (By.ID, "save-client-btn")
    
    # Messages Page
    MESSAGES_CONTAINER = (By.CLASS_NAME, "messages-container")
    MESSAGE_THREAD = (By.CLASS_NAME, "message-thread")
    NEW_MESSAGE_BUTTON = (By.ID, "new-message-btn")
    MESSAGE_INPUT_FIELD = (By.ID, "message-input")
    MESSAGE_SEND_BUTTON = (By.ID, "send-message-btn")
    MESSAGE_RECIPIENT_FIELD = (By.ID, "message-recipient")
    
    # Profile Page
    PROFILE_AVATAR = (By.CLASS_NAME, "profile-avatar")
    PROFILE_NAME = (By.ID, "profile-name")
    PROFILE_EMAIL = (By.ID, "profile-email")
    PROFILE_PHONE = (By.ID, "profile-phone")
    PROFILE_SPECIALIZATION = (By.ID, "profile-specialization")
    PROFILE_BIO = (By.ID, "profile-bio")
    PROFILE_EDIT_BUTTON = (By.ID, "edit-profile-btn")
    PROFILE_SAVE_BUTTON = (By.ID, "save-profile-btn")
    PROFILE_CANCEL_BUTTON = (By.ID, "cancel-profile-btn")
    
    # Settings Page
    SETTINGS_CONTAINER = (By.CLASS_NAME, "settings-container")
    NOTIFICATION_SETTINGS = (By.ID, "notification-settings")
    PRIVACY_SETTINGS = (By.ID, "privacy-settings")
    ABOUT_SECTION = (By.ID, "about-section")
    SETTINGS_SAVE_BUTTON = (By.ID, "save-settings-btn")
    
    # Common Elements
    LOADING_SPINNER = (By.CLASS_NAME, "loading-spinner")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "success-message")
    CONFIRM_BUTTON = (By.CLASS_NAME, "confirm-btn")
    CANCEL_BUTTON = (By.CLASS_NAME, "cancel-btn")
    CLOSE_BUTTON = (By.CLASS_NAME, "close-btn")
    SAVE_BUTTON = (By.CLASS_NAME, "save-btn")
    
    # Modal/Dialog Elements
    MODAL_OVERLAY = (By.CLASS_NAME, "modal-overlay")
    MODAL_CONTENT = (By.CLASS_NAME, "modal-content")
    MODAL_TITLE = (By.CLASS_NAME, "modal-title")
    MODAL_BODY = (By.CLASS_NAME, "modal-body")
    
    # Form Elements
    FORM_SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    FORM_RESET = (By.CSS_SELECTOR, "button[type='reset']")
    REQUIRED_FIELD_INDICATOR = (By.CSS_SELECTOR, ".required-field")
    
    # Responsive Elements
    MOBILE_MENU_TOGGLE = (By.CLASS_NAME, "mobile-menu-toggle")
    MOBILE_NAV_MENU = (By.CLASS_NAME, "mobile-nav-menu")
    DESKTOP_NAV_MENU = (By.CLASS_NAME, "desktop-nav-menu")
    
    # Calendar/Date Picker Elements
    CALENDAR_CONTAINER = (By.CLASS_NAME, "calendar-container")
    CALENDAR_DAY = (By.CLASS_NAME, "calendar-day")
    CALENDAR_MONTH = (By.CLASS_NAME, "calendar-month")
    CALENDAR_YEAR = (By.CLASS_NAME, "calendar-year")
    CALENDAR_NAV_PREV = (By.CLASS_NAME, "calendar-nav-prev")
    CALENDAR_NAV_NEXT = (By.CLASS_NAME, "calendar-nav-next")
