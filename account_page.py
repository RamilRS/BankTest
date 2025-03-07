from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

class AccountPageLocators():
    TRANSACTIONS_BUTTON = (By.CSS_SELECTOR,'button.btn[ng-click="transactions()"]')
    DEPOSIT_BUTTON = (By.CSS_SELECTOR,'button.btn[ng-click="deposit()"]')
    ACCOUNT_LIST = (By.ID, 'accountSelect')
    AMOUNT_TO_DEPOSIT = (By.CSS_SELECTOR,'input[placeholder="amount"]')
    DEPOSIT_SUBMIT = (By.CSS_SELECTOR,'button[type="submit"]')

class AccountPage(BasePage):
    def goto_transactions(self):
        self.browser.find_element(*AccountPageLocators.TRANSACTIONS_BUTTON).click()

    def select_account_by_index(self, index):
        select = Select(self.browser.find_element(*AccountPageLocators.ACCOUNT_LIST))
        select.select_by_index(index)

    def deposit(self, amount):
        self.browser.find_element(*AccountPageLocators.DEPOSIT_BUTTON).click()
        sleep(1)
        self.browser.find_element(*AccountPageLocators.AMOUNT_TO_DEPOSIT).send_keys(str(amount))
        sleep(1)
        self.browser.find_element(*AccountPageLocators.DEPOSIT_SUBMIT).click()



