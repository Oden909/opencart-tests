import pytest
import time
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

class TestKT3:
    @pytest.mark.parametrize("product", ["camera", "tablet", "phone"])
    def test_add_to_cart(self, browser, product):
        main_page = MainPage(browser)
        product_page = ProductPage(browser)
        cart_page = CartPage(browser)
        
        if product == "camera":
            main_page.click(*main_page.CAMERA_LINK)
        elif product == "tablet":
            main_page.click(*main_page.TABLET_LINK)
        else:
            main_page.click(*main_page.PHONE_LINK)
            
        product_page.add_to_cart()
        assert cart_page.get_cart_items_count() == 1

    def test_add_to_wishlist(self, browser):
        main_page = MainPage(browser)
        product_page = ProductPage(browser)
        
        main_page.click(*main_page.PRODUCT_LINK)
        product_page.add_to_wishlist()

    def test_write_review(self, browser):
        main_page = MainPage(browser)
        product_page = ProductPage(browser)
        
        main_page.click(*main_page.PRODUCT_LINK)
        product_page.write_review("Test User", "Great product!", 5)