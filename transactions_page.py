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

    def get_sort_reverse(self):
        dateheader = self.browser.find_element(By.CSS_SELECTOR,'a[ng-click*="sortType = "]')
        reverse = self.browser.execute_script('return angular.element(arguments[0]).scope().sortReverse;', dateheader)
        return reverse

    def reverse_sort(self):
        dateheader = self.browser.find_element(By.CSS_SELECTOR,'a[ng-click*="sortType = "]')
        self.browser.execute_script("arguments[0].click();", dateheader)

