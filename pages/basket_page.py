from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), "Basket is not empty"


    def should_be_text_about_empty_basket(self):
        message_about_empty_basket = self.browser.find_element(*BasketPageLocators.TEXT_EMPTY_BASKET).text
        assert "Your basket is empty." in message_about_empty_basket, "Message about empty basket is not presented"
