from selenium.webdriver.common.by import By

class UserWebLocators:
    """Web locators for User website"""
    
    # Login Page
    LOGIN_EMAIL_FIELD = (By.ID, "user-email")
    LOGIN_PASSWORD_FIELD = (By.ID, "user-password")
    LOGIN_BUTTON = (By.ID, "login-submit")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot Password?")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign Up")
    REMEMBER_ME_CHECKBOX = (By.ID, "remember-me")
    
    # Home Page
    HOME_HEADER = (By.TAG_NAME, "h1")
    HOME_WELCOME_MESSAGE = (By.CLASS_NAME, "welcome-message")
    HOME_SEARCH_BAR = (By.ID, "search-input")
    HOME_SEARCH_BUTTON = (By.ID, "search-button")
    HOME_NOTIFICATION_ICON = (By.CLASS_NAME, "notification-icon")
    
    # Navigation
    NAV_HOME = (By.LINK_TEXT, "Home")
    NAV_PROFILE = (By.LINK_TEXT, "Profile")
    NAV_BOOKINGS = (By.LINK_TEXT, "Bookings")
    NAV_MESSAGES = (By.LINK_TEXT, "Messages")
    NAV_LOGOUT = (By.LINK_TEXT, "Logout")
    
    # Profile Page
    PROFILE_AVATAR = (By.CLASS_NAME, "profile-avatar")
    PROFILE_NAME = (By.ID, "profile-name")
    PROFILE_EMAIL = (By.ID, "profile-email")
    PROFILE_PHONE = (By.ID, "profile-phone")
    PROFILE_EDIT_BUTTON = (By.ID, "edit-profile-btn")
    PROFILE_SAVE_BUTTON = (By.ID, "save-profile-btn")
    PROFILE_CANCEL_BUTTON = (By.ID, "cancel-profile-btn")
    
    # Bookings Page
    BOOKINGS_CONTAINER = (By.CLASS_NAME, "bookings-container")
    BOOKING_CARD = (By.CLASS_NAME, "booking-card")
    NEW_BOOKING_BUTTON = (By.ID, "new-booking-btn")
    BOOKING_DATE_FIELD = (By.ID, "booking-date")
    BOOKING_TIME_FIELD = (By.ID, "booking-time")
    BOOKING_SUBMIT_BUTTON = (By.ID, "submit-booking-btn")
    
    # Messages Page
    MESSAGES_CONTAINER = (By.CLASS_NAME, "messages-container")
    MESSAGE_THREAD = (By.CLASS_NAME, "message-thread")
    NEW_MESSAGE_BUTTON = (By.ID, "new-message-btn")
    MESSAGE_INPUT_FIELD = (By.ID, "message-input")
    MESSAGE_SEND_BUTTON = (By.ID, "send-message-btn")
    
    # Common Elements
    LOADING_SPINNER = (By.CLASS_NAME, "loading-spinner")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "success-message")
    CONFIRM_BUTTON = (By.CLASS_NAME, "confirm-btn")
    CANCEL_BUTTON = (By.CLASS_NAME, "cancel-btn")
    CLOSE_BUTTON = (By.CLASS_NAME, "close-btn")
    
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
