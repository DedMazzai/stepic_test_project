from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ADDRESS_IN_REG_FORM = (By.CSS_SELECTOR, ".register_form [type='email']")
    PASSWORD_IN_REG_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_BUTTON = (By.CSS_SELECTOR, "[name = 'registration_submit']")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form>button")
    ALERT_ABOUT_ADDING_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, "#messages>div>div")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages > .alert:first-child > .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1 ")
    ALERT_WITH_COST_BASKET = (By.CSS_SELECTOR, "#messages > .alert:last-child > .alertinner")
    COST_BASKET_IN_ALERT = (By.CSS_SELECTOR, "#messages > .alert:last-child > .alertinner strong")
    COST_PRODUCT = (By.CSS_SELECTOR, "#content_inner .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")


class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>a")
    BASKET_SUMMARY = (By.CSS_SELECTOR, ".basket_summary")
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")
