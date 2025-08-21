from selenium.webdriver.common.by import By

class UserWebLocators:
    """Web locators for User website"""
       # User
    SIGN_IN = (By.XPATH, "//button[normalize-space()='Sign in']")
    EMAIL = (By.XPATH, "//input[@id='email']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    ACCEPT = (By.XPATH, "//button[@class='wpccBtn--dwsPv']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[@data-testid='login-button' and @type='button']")
    PROFILE = (By.XPATH, "//div[@type='button']//div[contains(text(),'Sweet')]")
    SEARCH_ADVISOR = (By.XPATH, "//input[@placeholder='Search by specialty or reading type']")
    FIND_ADVISOR = (By.XPATH, "(//button[@class='searchButton--zl5Mn'])[1]")
    CLICK_ADVISOR = (By.XPATH, "//img[@alt='{advisor_name}']")
    CLICK_CHAT = (By.XPATH, "(//span[@class='modeTitle--KFD4l'][normalize-space()='Chat'])[2]")
    START_CHAT = (By.XPATH, "//button[@class='mbw-button-primary']")
    TYPE_MESSAGE_USER2ADVISOR = (By.XPATH, "//textarea[@placeholder='Your message...']")
    SEND_MESSAGE_BUTTON_USER = (By.XPATH, "//button[normalize-space()='Send']")
    NETWORK_OFFLINE = (By.XPATH, "//div[contains(text(),'Network seems to be offline')]")
    NETWORK_SESSION_EXPIRED = (By.XPATH, "//div[@class='hangupError--B8h5h']")
    JOIN = (By.XPATH, "//button[@class='loginButtonContainer--r7uit']")
    RANDOM_EMAIL = (By.XPATH, "//input[@id='email']")
    RETYPE_EMAIL = (By.XPATH, "//input[@id='confirmEmail']")
    RANDOM_PASSWORD = (By.XPATH, "//input[@id='password']")
    CREATE_ACCOUNT = (By.XPATH, "//button[@class='actionButton--UxfDy']")
    TERMS_POLICY = (By.XPATH, "//button[@class='ppTofModalSignUpButton--Imglp']")
    HANG_UP_BUTTON = (By.XPATH, "//button[@class='hangupBtn--EGCTW']")
    CONTINUE_BUTTON = (By.XPATH, "//button[normalize-space()='Continue']")

        # add_Credit_Card_Detail
    ADD_NEW_CREDIT_DEBIT_CARD = (By.XPATH, "//button[@id='add_new_cc']")
    CARD_HOLDER_NAME = (By.XPATH, "//input[@id='nameOfCard']")
    CARD_NUMBER_FRAME = (By.XPATH, "//iframe[@id='cardNumber']")
    CARD_NUMBER = (By.XPATH, "//input[@id='checkout-frames-card-number']")
    EXPIRE_DATE_FRAME = (By.XPATH, "//iframe[@id='expiryDate']")
    EXPIRE_DATE = (By.XPATH, "//input[@id='checkout-frames-expiry-date']")
    CVC_FRAME = (By.XPATH, "//iframe[@id='cvv']")
    CVV = (By.XPATH, "//input[@id='checkout-frames-cvv']")
    ZIP_CODE = (By.XPATH, "//input[@id='zip']")
    ADD_CARD_BUTTON = (By.XPATH, "//button[text()='Add card']")
    PAY_BUTTON = (By.XPATH, "//div[@class='buyButton--Xc2uP']")
    START_LIVE_CHAT_BUTTON = (By.XPATH, "//button[normalize-space()='Start live chat']")
    NICKNAME = (By.XPATH, "//input[@placeholder='Nickname']")
    MALE_RADIO_BUTTON = (By.XPATH, "//div[@value='M']")
    DOB = (By.XPATH, "//input[@class='datePickerInput--x0pit']")
    DURATION_CARD = (By.XPATH, "(//div[@class='durationItem--qG0j_'])")
    ADD_MIN_BALANCE_BUTTON = (By.XPATH, "//div[@class='buyButton--Xc2uP']")

    # promocode_apply
    HOME_PAGE = (By.XPATH, "(//div[@class='headerTitle--EzGzO'])[1]")
    SIDEMENU_APPLY_PROMOCODE = (By.XPATH, "//div[contains(text(),'Apply promo code')]")
    SIDEMENU_PROMOCODE = (By.XPATH, "//input[@class='inputContent--omlML']")
    SIDEMENU_SUBMIT_BUTTON = (By.XPATH, "//button[@class='submitButton--yY77x']") 
    PROMOCODE_SUCCESS_MESSAGE = (By.XPATH, "//button[@class='promoCodeModalOkButton--DMvSR']")
    CLOSE_CHAT_POPUP = (By.XPATH, "//button[@class='closeBtn--KvTru']//*[name()='svg']")

    # bonus_get
    ADD_BONUS_BUTTON = (By.XPATH, "//div[@class='buttonTitleText--pZbgX']")
    CONFIRM_BONUS_MESSAGE = (By.XPATH, "//button[@class='confirmButton--VMA1l']")

    # user_balance_check
    USER_ICON = (By.XPATH, "//img[@class='avatar--e_6rk']")
    BALANCE = (By.XPATH, "//a[@class='addCreditsButton--zTp2Z']")

    # user_introduction_form
    NICKNAME = (By.XPATH, "//input[@class='inputClass--DG6nI']")
    GENDER = (By.XPATH, "//div[contains(text(),'Male')]//*[name()='svg']")
    DATE_OF_BIRTH = (By.XPATH, "//input[@class='datePickerInput--x0pit']")
    START_LIVE_CHAT_BUTTON = (By.XPATH, "//span[normalize-space()='Start live chat']")

        # Sidemenu_items

    SIDEMENU = (By.XPATH, "(//button[@class='menuButton--uALyj'])[1]")
    SIDEMENU_ACTIVITY = (By.XPATH, "//div[contains(text(),'My activity')]")
    SIDEMENU_ACTIVITY_USERCLICK = (By.XPATH, "//span[normalize-space()='Hubert Blaine'][1]")
    SIDEMENU_ACTIVITY_MESSAGE_FIELD = (By.XPATH, "//textarea[@id='sendInput']")
    SIDEMENU_ACTIVITY_SEND_BUTTON = (By.XPATH, "//button[@class='sendButton--R6WFP']//*[name()='svg']")
    SIDEMENU_ACTIVITY_USER_MESSAGE_VALIDATION = (By.XPATH, "(//div[contains(text(),'Hello Hubert')])[1]")

    #chat on live call
    TYPE_MESSAGE= (By.XPATH, "//textarea[@placeholder='Your message...']")
    SEND=(By.XPATH, "//button[normalize-space()='Send']")
    MESSAGE_TEXT=(By.XPATH, "(//span[@class='bubbdleText--PUOSa'])[3]")
    MESSAGE_TEXT_FROM_ADVISOR=(By.XPATH, "(//span[@class='bubbdleText--PUOSa'])[4]")

    # chat duration pop up
    BACK_BUTTON = (By.XPATH, "(//div[@class='arrowImgContainer--bSijc'])[1]")
    FORWARD_BUTTON = (By.XPATH, "(//div[@class='arrowImgContainer--bSijc'])[2]")
    MINUTES_TEXT = (By.XPATH, "//div[@class='mbw-duration-item-duration-selected']")
    CLOSE_POPUP_BUTTON = (By.XPATH, "(//button[@class='downloadAppPopupCloseBtn--E9rKR'])[1]")


