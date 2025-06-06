import pytest
import time
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.register_page import RegisterPage

class TestKT2:
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_product_screenshots(self, browser):
        main_page = MainPage(browser)
        product_page = ProductPage(browser)
        
        main_page.click(*main_page.PRODUCT_LINK)
        product_page.switch_screenshots()

    @pytest.mark.parametrize("currency", ["EUR", "USD"])
    def test_currency_switch(self, browser, currency):
        main_page = MainPage(browser)
        main_page.change_currency_to(currency)

    def test_empty_pc_category(self, browser):
        main_page = MainPage(browser)
        main_page.click(*main_page.MENU_PC)
        assert "No products" in browser.page_source

    def test_user_registration(self, browser):
        main_page = MainPage(browser)
        register_page = RegisterPage(browser)
        
        main_page.click(*main_page.REGISTER_LINK)
        register_page.register_user("Test", "User", f"test{time.time()}@example.com", "123456789", "password123")
        assert "Your Account Has Been Created!" in browser.page_source