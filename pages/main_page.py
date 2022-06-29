from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import BasePageLocators
from pages.login_page import LoginPage

class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)