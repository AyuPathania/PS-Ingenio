from selenium.webdriver.common.by import By

class UserWebLocators:
    """Web locators for User website"""
       # User
    SIGN_IN = (By.XPATH, "//button[normalize-space()='Sign in']")
    EMAIL = (By.XPATH, "//input[@id='email']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    ACCEPT = (By.XPATH, "//button[@class='wpccBtn--dwsPv']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[@data-testid='login-button' and @type='button']")
    PROFILE = (By.XPATH, "(//img[@class='avatar--e_6rk'])[1]")
    SETTING_BUTTON_ON_PROFILE = (By.XPATH, "(//a[@class='popoverItem--CEguW'])[1]")
    USER_ID = (By.XPATH, "//div[text()='User ID']/following-sibling::div")
    SEARCH_ADVISOR = (By.XPATH, "//input[@placeholder='Search by specialty or reading type']")
    FIND_ADVISOR = (By.XPATH, "(//button[@class='searchButton--zl5Mn'])[1]")
    CLICK_ADVISOR = (By.XPATH, "//img[@alt='{advisor_name}']")
    CLICK_CHAT = (By.XPATH, "(//span[@class='modeTitle--KFD4l'][normalize-space()='Chat'])[1]")
    START_CHAT = (By.XPATH, "(//button[@class='mbw-button-primary'])[1]")
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
    CURRENT_BALANCE_TEXT = (By.XPATH, "//span[@class='clientAvailableCreditText--PjAfk']")

    # user_balance_check
    USER_ICON = (By.XPATH, "//img[@class='avatar--e_6rk']")
    BALANCE = (By.XPATH, "//a[@class='addCreditsButton--zTp2Z']")

    # user_introduction_form
    # NICKNAME = (By.XPATH, "//input[@class='inputClass--DG6nI']")
    # GENDER = (By.XPATH, "//div[contains(text(),'Male')]//*[name()='svg']")
    # DATE_OF_BIRTH = (By.XPATH, "//input[@class='datePickerInput--x0pit']")
    # START_LIVE_CHAT_BUTTON = (By.XPATH, "//span[normalize-space()='Start live chat']")

        # Sidemenu_items

    SIDEMENU = (By.XPATH, "(//button[@class='menuButton--uALyj'])[1]")
    SIDEMENU_ACTIVITY = (By.XPATH, "//div[contains(text(),'My activity')]")
    SIDEMENU_ACTIVITY_USERCLICK = (By.XPATH, "//span[normalize-space()='Hubert Blaine'][1]")
    SIDEMENU_ACTIVITY_MESSAGE_FIELD = (By.XPATH, "//textarea[@id='sendInput']")
    SIDEMENU_ACTIVITY_SEND_BUTTON = (By.XPATH, "//button[@class='sendButton--R6WFP']//*[name()='svg']")
    SIDEMENU_ACTIVITY_USER_MESSAGE_VALIDATION = (By.XPATH, "(//div[contains(text(),'Hello Hubert')])[1]")
    ADVISOR_MESSAGE_ON_USER_SIDE = (By.XPATH, "(//div[@class='chatBubbleMessageText--n2ssQ'])[1]")
    USER_MESSAGE_ON_USER_SIDE = (By.XPATH, "(//div[@class='chatBubbleMessageText--n2ssQ'])[1]")
    SIDE_MENU_ADD_FUNDS = (By.XPATH, "//div[text()='Add funds']")
    GET_20_CREDIT = (By.XPATH, "(//button[@class='btn--cEcKk'])[1]")
    SIDE_MENU_PAYMENT_METHOD = (By.XPATH, "(//div[text()='Payment methods'])[1]")
    ADD_NEW_PAYMENT_METHOD_BUTTON = (By.XPATH, "//div[text()='Add a new payment method']")
    ADD_ANOTHER_PAYMENT_METHOD = (By.XPATH, "//div[text()='Add another payment method']")

    #chat on live call
    TYPE_MESSAGE= (By.XPATH, "//textarea[@placeholder='Your message...']")
    SEND=(By.XPATH, "//button[normalize-space()='Send']")
    USER_SEND_MESSAGE_TEXT=(By.XPATH, "(//span[@class='bubbdleText--PUOSa'])[last()]")
    MESSAGE_TEXT_FROM_ADVISOR=(By.XPATH, "(//span[@class='bubbdleText--PUOSa'])[4]")

    # chat duration pop up
    BACK_BUTTON = (By.XPATH, "(//div[@class='arrowImgContainer--bSijc'])[1]")
    FORWARD_BUTTON = (By.XPATH, "(//div[@class='arrowImgContainer--bSijc'])[2]")
    MINUTES_TEXT = (By.XPATH, "(//div[@class='mbw-duration-item-duration-selected'])[1]")
    CLOSE_POPUP_BUTTON = (By.XPATH, "(//button[@class='downloadAppPopupCloseBtn--E9rKR'])[1]")
    AMOUNT_BEFORE_PAYMENT_PRICE = (By.XPATH, "//div[@class='mbw-duration-item-selected']// div[@class='durationItemPriceContainerPrice--MBHsQ']")
    AMOUNT_BEFORE_PAYMENT_PRICE_ON_CHAT = (By.XPATH, "//div[@class='mbw-duration-item-current-balance']")
    AMOUNT_BEFORE_PAYMENT_SALES = (By.XPATH, "//div[@class='mbw-duration-item-selected']// div[@class='durationItemPriceContainerSalesPrice--wS3iW']")
    ACTUAL_AMOUNT = (By.XPATH, "(//b[@class='priceTitle--iaF2q'])[1]")
    PAY_TEXT = (By.XPATH, "//div[@class='buyButton--Xc2uP']")
    CLOSE_POPUP_AFTER_CALL = (By.XPATH, "//button[@data-testid='popup-close-btn']")
    SEARCH_ICON_BUTTON = (By.XPATH, "//button[@class='headerSearchButton--t8pEi']//*[name()='svg']")
    HEADER_SIDE_FIND_ADVISOR = (By.XPATH, "//button[@class='headerSearchLineButton--iuug7']")

    #call calculations

    TOTAL_DURATION = (By.XPATH, "(//div[@class='descriptionDataBrowser--GrQN_'])[1]")
    ADVISOR_RATE = (By.XPATH, "(//div[@class='descriptionDataBrowser--GrQN_'])[2]")
    TOTAL_CREDIT_CHARGED = (By.XPATH, "(//div[@class='totalValue--iTijP'])")
    COUPON_TEXT_ON_USER_SIDE = (By.XPATH, "//div[@class='mbw-coupon-info-container']")
    ACTUAL_PRICE = (By.XPATH, "(//span[@class='modePrice--Dl5PX'])[1]//span")
    DISCOUNTED_PRICE = (By.XPATH, "(//span[@class='modePrice--Dl5PX'])[1]//div")

    # 50% discount
    BEFORE_50_DISCOUNT_PRICE = (By.XPATH, "(//span[@class='sale--QvuT7'])[1]")
    AFTER_50_DISCOUNT_PRICE = (By.XPATH, "(//span[@class='sale--QvuT7'])[1]/following-sibling::div")
    ADD_CHAT_TIME = (By.XPATH, "(//button[@data-testid='mbw-button'])[2]")
    CALL_END = (By.XPATH, "//button[@class='mbw-button-secondary']")
    CLOSE_QR_CODE_SCREEN = (By.XPATH, "//button[@class='downloadAppPopupCloseBtn--E9rKR']")
    TOTAL_DURATION = (By.XPATH, "//span[normalize-space()='Total duration']/following-sibling::div")
    YOUR_RATE = (By.XPATH, "(//span[contains(@class,'descriptionTextBrowser--uQkcb')]/following-sibling::div)[2]")
    SUBTOTAL_PRICE = (By.XPATH, "//span[normalize-space()='Subtotal']/following-sibling::div")
    DISCOUNT_50_PERCENT = (By.XPATH, "//div[normalize-space()='Discount']/following-sibling::div")
    TOTAL_PAY = (By.XPATH, "(//div[normalize-space()='Total']/following-sibling::div)[1]")
    YOU_SAVED = (By.XPATH, "(//div[normalize-space()='Total']/following-sibling::div)[2]")
    SELECT_ONE_MINUTE = (By.XPATH, "(//div[@class='durationItem--qG0j_'])[1]")

    CHAT_DISCOUNT_TEXT = (By.XPATH, "(//span[@class='bubbdleText--PUOSa'])[1]")
    DISCOUNT_ON_COUPON_TEXT = (By.XPATH, "(//DIV[@class='smallBlockValue--GRQbW'])[1]")




