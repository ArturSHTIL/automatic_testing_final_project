from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_empty_basket_message(self):
        assert self.is_not_element_present(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE), "We see the empty basket message is presented, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE), "We see empty basket message is not presented, but should be"

    def should_be_empty_basket(self):
        assert self.is_element_present(
            *BasketPageLocators.CONTINUOUS_LINK), "We see the goods in the basket, but not should be"
