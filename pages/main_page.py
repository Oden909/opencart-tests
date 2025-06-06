from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    LOGO = (By.CSS_SELECTOR, "img[title='Your Store']")
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn-light")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "button.dropdown-toggle")
    EURO_CURRENCY = (By.NAME, "EUR")
    DOLLAR_CURRENCY = (By.NAME, "USD")
    PRODUCT_LINK = (By.LINK_TEXT, "iPhone")
    MENU_PC = (By.LINK_TEXT, "PC")
    REGISTER_LINK = (By.LINK_TEXT, "Register")
    
    CAMERA_LINK = (By.LINK_TEXT, "Canon EOS 5D")
    TABLET_LINK = (By.LINK_TEXT, "Samsung Galaxy Tab 10.1")
    PHONE_LINK = (By.PARTIAL_LINK_TEXT, "HTC Touch HD")

    def change_currency_to(self, currency):
        self.click(*self.CURRENCY_DROPDOWN)
        if currency == "EUR":
            self.click(*self.EURO_CURRENCY)
        else:
            self.click(*self.DOLLAR_CURRENCY)