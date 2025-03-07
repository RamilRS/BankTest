from base_page import BasePage
from selenium.webdriver.common.by import By

class TransactionsPageLocators():
    TRANSACTIONS_TABLE = (By.CSS_SELECTOR,'tr[id*="anchor"]')

class TransactionsPage(BasePage):
    def get_transactions(self):
        return self.browser.find_elements(*TransactionsPageLocators.TRANSACTIONS_TABLE)

    def get_transaction(self, index):
        date = self.browser.find_elements(By.CSS_SELECTOR,f'tr[id*="anchor{index}"] td:nth-child(1)')[0].text
        amount = self.browser.find_elements(By.CSS_SELECTOR,f'tr[id*="anchor{index}"] td:nth-child(2)')[0].text
        type = self.browser.find_elements(By.CSS_SELECTOR,f'tr[id*="anchor{index}"] td:nth-child(3)')[0].text
        return (date,amount,type)

