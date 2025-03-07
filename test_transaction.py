import pytest
from selenium import webdriver
from main_page import MainPage
from account_page import AccountPage
from transactions_page import  TransactionsPage
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture()
def transactions(browser):
    link = "https://www.globalsqa.com/angularJs-protractor/BankingProject/"
    page = MainPage(browser, link)
    page.open()
    page.customer_login()
    page.select_customer_by_index(1)
    page.submit_user()
    account_page = AccountPage(browser, browser.current_url)
    account_page.goto_transactions()
    transactions = TransactionsPage(browser, browser.current_url)
    return transactions

@pytest.mark.skip
def test_transaction(transactions):
    trans = transactions.get_transaction(0)  # первая транзакция
    print(trans)
    assert (trans[1] == '30' and trans[2] == "Credit") == True

@pytest.mark.skip
def test_sort_reverse(transactions):
    assert transactions.get_sort_reverse() == False

def test_transaction_appears(browser):
    link = "https://www.globalsqa.com/angularJs-protractor/BankingProject/"
    page = MainPage(browser, link)
    page.open()
    page.customer_login()
    page.select_customer_by_index(1)
    page.submit_user()
    account_page = AccountPage(browser, browser.current_url)
    account_page.deposit(1000)
    account_page.goto_transactions()
    account_page.select_account_by_index(0) # с 0 счетом работает корректно
    transactions_page=TransactionsPage(browser,browser.current_url)
    transactions_page.reverse_sort()
    trans = transactions_page.get_transaction(0) # первая транзакция
    print(trans)
    assert (trans[1]=='1000' and trans[2]=="Credit")==True


if __name__ == '__main__':
    link = "https://www.globalsqa.com/angularJs-protractor/BankingProject/"
    browser = webdriver.Chrome()
    browser.get(link)
    page = MainPage(browser,link)
    page.open()
#    sleep(1)
#    page.manager_login()
#    sleep(2)
#    page.open_account(1)
#    sleep(2)
#    page.open()
#    sleep(2)

    page.customer_login()
    sleep(1)
#    page.select_customer_by_name("Hermoine Granger")
    page.select_customer_by_index(1)
    page.submit_user()
    account_page=AccountPage(browser,browser.current_url)
    sleep(1)
    account_page.deposit(1000)
    sleep(1)
    account_page.goto_transactions()
    account_page.select_account_by_index(0) # с 0 счетом работает корректно
    sleep(1)
    transactions_page=TransactionsPage(browser,browser.current_url)
    transactions_page.reverse_sort()
    sleep(5)
    trans = transactions_page.get_transaction(0) # первая транзакция
    print(trans)
    print(transactions_page.get_sort_reverse())
    assert (trans[1]=='30' and trans[2]=="Credit")==True
    browser.quit()

