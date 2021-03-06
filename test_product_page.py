from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
product_links = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
url = [f"{product_links}/?promo=offer{number}" for number in range(10)]
url[7] = pytest.param(f"{product_links}/?promo=offer7", marks=pytest.mark.xfail)


def test_guest_should_see_promo_link(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_promo_url()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_name_of_product()


@pytest.mark.need_review
@pytest.mark.parametrize("offer", url)
def test_user_can_add_good_to_basket(browser, offer):
    page = ProductPage(browser, offer)
    page.open()
    page.add_product_to_basket()
    page.should_be_price_of_product()
    page.should_be_name_of_product()


@pytest.mark.need_review
@pytest.mark.xfail
def test_guest_can_see_positive_message_after_adding_good_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_price_of_product()
    page.should_be_name_of_product()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_success_message()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_empty_basket()
    page.should_be_text_about_empty_basket()
    page.should_not_be_empty_basket()
