from .base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    CART_BUTTON = (By.CSS_SELECTOR, "button[data-toggle='dropdown']")
    VIEW_CART_LINK = (By.LINK_TEXT, "View Cart")
    ITEMS_IN_CART = (By.CSS_SELECTOR, "table.table tbody tr")

    def get_cart_items_count(self):
        return len(self.find_elements(*self.ITEMS_IN_CART))