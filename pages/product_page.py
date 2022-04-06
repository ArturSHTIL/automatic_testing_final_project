from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def should_be_promo_url(self):
        login_url = self.browser.current_url
        assert "?promo=newYear" in login_url, 'Sorry Promo url is not present'

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()
        self.solve_quiz_and_get_code()

    def should_be_price_of_product(self):
        price_on_market = self.browser.find_element(*ProductPageLocators.PRICE_ON_MARKET).text
        price_on_basket = self.browser.find_element(*ProductPageLocators.PRICE_ON_BASKET).text
        assert price_on_market == price_on_basket, "price on market is not equal in basket!"

    def should_be_name_of_product(self):
        name_on_market = self.browser.find_element(*ProductPageLocators.NAME_ON_MARKET).text
        name_on_basket = self.browser.find_element(*ProductPageLocators.NAME_IN_BASKET).text
        assert name_on_market == name_on_basket, "name on market is not equal in basket!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented, but should  be"
