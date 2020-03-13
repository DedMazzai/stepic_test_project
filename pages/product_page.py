from selenium import webdriver
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button add to basket is not presented"

    def click_button_add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()

    def should_be_alert_about_adding_product_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.ALERT_ABOUT_ADDING_PRODUCT_TO_BASKET), "Name of product in alert is not presented"

    def should_be_product_name_in_alert_match_product_name(self):
        text_alert_about_adding_product_to_basket = self.browser.find_element(
            *ProductPageLocators.ALERT_ABOUT_ADDING_PRODUCT_TO_BASKET).text
        text_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert text_product_name in text_alert_about_adding_product_to_basket, \
            "A message about adding a product to the basket does not contain information about the desired product"

    def shold_be_alert_with_cost_basket(self):
        assert self.browser.find_element(
            *ProductPageLocators.ALERT_WITH_COST_BASKET), "Alert with cost of basket is not presented"

    def should_be_cost_product_in_alert_with_cost_basket(self):
        text_cost_basket_in_alert = self.browser.find_element(*ProductPageLocators.COST_BASKET_IN_ALERT).text
        text_cost_product = self.browser.find_element(*ProductPageLocators.COST_PRODUCT).text
        assert text_cost_basket_in_alert == text_cost_product, \
            "The cost of the basket does not match the cost of the product"
