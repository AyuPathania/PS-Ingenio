from selenium.webdriver.common.by import By

class PurpelOceanUserWebLocators:
    """Web locators for User website"""
       # User
    SIGN_IN = (By.XPATH, "//button[normalize-space()='ayush']")
    EMAIL = (By.XPATH, "//input[@id='email']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    ACCEPT = (By.XPATH, "//button[@class='PurpelOcean']")
    JOIN = (By.XPATH, "//button[@class='PurpelOcean']")