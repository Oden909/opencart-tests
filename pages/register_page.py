from .base_page import BasePage
from selenium.webdriver.common.by import By

class RegisterPage(BasePage):
    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    TELEPHONE = (By.ID, "input-telephone")
    PASSWORD = (By.ID, "input-password")
    CONFIRM_PASSWORD = (By.ID, "input-confirm")
    PRIVACY_CHECKBOX = (By.NAME, "agree")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[value='Continue']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#content h1")

    def register_user(self, first_name, last_name, email, telephone, password):
        self.send_keys(*self.FIRST_NAME, text=first_name)
        self.send_keys(*self.LAST_NAME, text=last_name)
        self.send_keys(*self.EMAIL, text=email)
        self.send_keys(*self.TELEPHONE, text=telephone)
        self.send_keys(*self.PASSWORD, text=password)
        self.send_keys(*self.CONFIRM_PASSWORD, text=password)
        self.click(*self.PRIVACY_CHECKBOX)
        self.click(*self.CONTINUE_BUTTON)