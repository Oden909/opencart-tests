import pytest
import time
from pages.admin_page import AdminPage
from pages.main_page import MainPage

class TestKT5:
    def test_create_category_and_products(self, browser):
        admin_page = AdminPage(browser)
        main_page = MainPage(browser)
        
        admin_page.login("demo", "demo")
        admin_page.create_category("Devices")
        
        products = [
            {"name": "Wireless Mouse", "model": "WM-100"},
            {"name": "Gaming Mouse", "model": "GM-200"},
            {"name": "Mechanical Keyboard", "model": "MK-100"},
            {"name": "Wireless Keyboard", "model": "WK-200"}
        ]
        
        for product in products:
            admin_page.add_product(product["name"], product["model"], "Devices")
        
        for product in products:
            assert main_page.search_product(product["name"])
        
        products_to_delete = ["Wireless Mouse", "Mechanical Keyboard"]
        for product in products_to_delete:
            admin_page.delete_product(product)
        
        remaining_products = ["Gaming Mouse", "Wireless Keyboard"]
        for product in remaining_products:
            assert main_page.search_product(product)
        
        for product in products_to_delete:
            assert not main_page.search_product(product)