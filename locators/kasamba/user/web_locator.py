from selenium.webdriver.common.by import By

class KasambaUserWebLocators:
    """Web locators for User website"""
       # User
    SIGN_IN = (By.XPATH, "//button[normalize-space()='Sign in']")
    EMAIL = (By.XPATH, "//input[@id='email']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    ACCEPT = (By.XPATH, "//button[@class='kasamba']")
    JOIN = (By.XPATH, "//button[@class='kasamba']")