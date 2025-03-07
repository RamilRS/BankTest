from base_page import BasePage
from selenium.webdriver.common.by import By

class AccountPageLocators():
    TRANSACTIONS_BUTTON = (By.CSS_SELECTOR,'button.btn[ng-click="transactions()"]')

class AccountPage(BasePage):
    def goto_transactions(self):
        self.browser.find_element(*AccountPageLocators.TRANSACTIONS_BUTTON).click()

