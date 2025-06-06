import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    
    driver.get("https://demo.opencart.com/")
    driver.maximize_window()
    yield driver
    driver.quit()