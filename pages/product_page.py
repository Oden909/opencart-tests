from .base_page import BasePage
from selenium.webdriver.common.by import By
import time

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")
    ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Add to Wish List']")
    SCREENSHOTS = (By.CSS_SELECTOR, "ul.thumbnails li")
    REVIEW_TAB = (By.LINK_TEXT, "Reviews")
    REVIEW_INPUT = (By.ID, "input-review")
    REVIEW_NAME = (By.ID, "input-name")
    RATING_RADIO = (By.NAME, "rating")
    REVIEW_SUBMIT = (By.ID, "button-review")

    def switch_screenshots(self):
        screenshots = self.find_elements(*self.SCREENSHOTS)
        for screenshot in screenshots:
            screenshot.click()
            time.sleep(1)