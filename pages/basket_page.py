from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Basket not Empty"

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Message is absent"

    def should_not_be_empty_basket(self):
        assert self.is_disappeared(*BasketPageLocators.PRODUCT_IN_BASKET), "Your basket not empty, but should be empty"
