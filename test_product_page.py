from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_button_add_to_basket()
    product_page.click_button_add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_alert_about_adding_product_to_basket()
    product_page.should_be_product_name_in_alert_match_product_name()
    product_page.shold_be_alert_with_cost_basket()
    product_page.should_be_cost_product_in_alert_with_cost_basket()
