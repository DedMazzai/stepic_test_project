from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_link()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.should_be_login_form()
        login_page.should_be_register_form()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_product_in_basket()
        basket_page.should_be_text_about_empty_basket()
