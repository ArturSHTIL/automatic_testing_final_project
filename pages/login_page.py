import random

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
        assert 'login' in login_url, 'login url is not present'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is absent"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is absent"
        assert True

    def register_new_user(self):
        user = random.randint(1, 100000)
        email = f"{user}aurum@minde.com"
        password = f"{user}PythonAmore"

        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_input.send_keys(email)

        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_input.send_keys(password)

        confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_FIELD)
        confirm_password.send_keys(password)

        register_user = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_user.click()
