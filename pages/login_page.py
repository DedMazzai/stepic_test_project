from .generators import DataGenerator
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_url = self.browser.current_url
        assert "login" in login_url, "It's not login Url!"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        generator = DataGenerator()
        email = generator.random_string(20) + "@example.stepic"
        password = generator.random_string_digits(20)
        input_string_email_for_reg = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS_IN_REG_FORM)
        input_string_email_for_reg.send_keys(email)
        input_string_password_for_reg = self.browser.find_element(*LoginPageLocators.PASSWORD_IN_REG_FORM)
        input_string_password_for_reg.send_keys(password)
        input_confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        input_confirm_password.send_keys(password)
        login_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        login_button.click()
