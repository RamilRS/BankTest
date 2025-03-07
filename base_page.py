from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self, browser, url, timeout=2):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how,what)
        except NoSuchElementException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)
