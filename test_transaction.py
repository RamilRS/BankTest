import pytest
from selenium import webdriver
from main_page import MainPage
from account_page import AccountPage
from transactions_page import  TransactionsPage
from selenium.webdriver.common.by import By
from time import sleep

def test_transaction(browser):
    link = "https://www.globalsqa.com/angularJs-protractor/BankingProject/"
    page = MainPage(browser, link)
    page.open()
    page.customer_login()
    page.select_customer_by_index(1)
    page.submit_user()
    account_page = AccountPage(browser, browser.current_url)
    account_page.goto_transactions()
    transactions_page = TransactionsPage(browser, browser.current_url)
    trans = transactions_page.get_transaction(0)  # первая транзакция
    print(trans)
    assert (trans[1] == '30' and trans[2] == "Credit") == True

if __name__ == '__main__':
    link = "https://www.globalsqa.com/angularJs-protractor/BankingProject/"
    browser = webdriver.Chrome()
    browser.get(link)
    page = MainPage(browser,link)
    page.open()
    sleep(2)
    page.customer_login()
    sleep(2)
#    page.select_customer_by_name("Hermoine Granger")
    page.select_customer_by_index(1)
    page.submit_user()
    account_page=AccountPage(browser,browser.current_url)
    account_page.goto_transactions()
    transactions_page=TransactionsPage(browser,browser.current_url)
    trans = transactions_page.get_transaction(0) # первая транзакция
    print(trans)
    sleep(1)
    assert (trans[1]=='30' and trans[2]=="Credit")==True
    browser.quit()

