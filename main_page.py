from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class MainPageLocators():
    CUSTOMER_LOGIN_LINK = (By.CSS_SELECTOR, 'button.btn-lg[ng-click="customer()"]')
    MANAGER_LOGIN_LINK = (By.CSS_SELECTOR, 'button.btn-lg[ng-click="manager()"]')
    USER_LIST = (By.ID, 'userSelect')
    SUBMIT_USER = (By.CSS_SELECTOR,'button.btn[type="submit"]')
    OPEN_ACCOUNT_BUTTON = (By.CSS_SELECTOR,'button.btn[ng-click="openAccount()"]')
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR,'button[type="submit"]')
    CURRENCY_LIST = (By.ID, 'currency')


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def customer_login(self):
        self.browser.find_element(*MainPageLocators.CUSTOMER_LOGIN_LINK).click()

    def manager_login(self):
        self.browser.find_element(*MainPageLocators.MANAGER_LOGIN_LINK).click()

    def select_customer_by_name(self, name):
        select = Select(self.browser.find_element(*MainPageLocators.USER_LIST))
        select.select_by_visible_text(name)

    def select_customer_by_index(self, index):
        select = Select(self.browser.find_element(*MainPageLocators.USER_LIST))
        select.select_by_index(index)

    def submit_user(self):
        self.browser.find_element(*MainPageLocators.SUBMIT_USER).click()

    def open_account(self,nameIndex):
        self.browser.find_element(*MainPageLocators.OPEN_ACCOUNT_BUTTON).click()
        self.select_customer_by_index(nameIndex)
        time.sleep(1)
        select = Select(self.browser.find_element(*MainPageLocators.CURRENCY_LIST))
        select.select_by_index(1)
        time.sleep(1)
        self.browser.find_element(*MainPageLocators.CREATE_ACCOUNT_BUTTON).click()
        time.sleep(1)
        confirm = self.browser.switch_to.alert
        confirm.accept()
        time.sleep(1)

