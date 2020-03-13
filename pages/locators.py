from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form>button")
    ALERT_ABOUT_ADDING_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, "#messages>div>div")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    ALERT_WITH_COST_BASKET = (By.CSS_SELECTOR, "#messages > .alert:last-child > .alertinner")
    COST_BASKET_IN_ALERT = (By.CSS_SELECTOR, "#messages > .alert:last-child > .alertinner strong")
    COST_PRODUCT = (By.CSS_SELECTOR, "#content_inner .price_color")