from .base_page import BasePage
from selenium.webdriver.common.by import By

class AdminPage(BasePage):
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    CATALOG_MENU = (By.CSS_SELECTOR, "#menu-catalog > a")
    CATEGORIES_LINK = (By.LINK_TEXT, "Categories")
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, "a[data-bs-original-title='Add New']")
    CATEGORY_NAME = (By.ID, "input-name-1")
    META_TAG = (By.ID, "input-meta-title-1")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def login(self, username, password):
        self.send_keys(*self.USERNAME_INPUT, text=username)
        self.send_keys(*self.PASSWORD_INPUT, text=password)
        self.click(*self.LOGIN_BUTTON)