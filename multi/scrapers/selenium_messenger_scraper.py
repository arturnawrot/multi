from multi.selenium.selenium_client import SeleniumClient
from multi.scrapers.urls import MESSENGER_HOME, LOGIN_PAGE, ROOT_URL, NEW_VERSION_URL
from multi.entities.account import Account
from multi.entities.ref import Ref
from selenium.webdriver.firefox.options import Options
import json
import requests
import time

class SeleniumMessengerScraper:

    def __init__(self, path, isHeadless: bool = True):

        options = Options()
        options.headless = isHeadless
        self.scraper = SeleniumClient(path, options=options)

    def get_html_from_url(self, url: str) -> str:
        self.scraper.get_page_and_wait_to_load(url)
        return self.scraper.get_html()

    def switch_to_new_version(self) -> None:
        self.scraper.get_page(NEW_VERSION_URL)

    def login_using_credentials(self, account: Account):
        self.scraper.get_page_and_wait_to_load(LOGIN_PAGE)

        time.sleep(0.6)
        self.scraper.get_page_and_wait_to_load(LOGIN_PAGE)

        try:
            login_input = self.scraper.find('ID', 'm_login_email')
        except:
            raise Exception('Login input was not found.')

        login_input.send_keys(account.get_email())

        time.sleep(0.6)

        try:
            password_input = self.scraper.find('NAME', 'pass')
        except:
            raise Exception('Password input was not found')

        password_input.send_keys(account.get_password())

        time.sleep(0.6)

        try:
            login_button = self.scraper.find('NAME', 'login')
        except:
            raise Exception('Login button was not found')

        login_button.click()

        time.sleep(2)

        return self.scraper.get_cookies()

    def login_using_cookies(self, account: Account):
        self.scraper.get_page_and_wait_to_load(LOGIN_PAGE)

        cookies = account.get_cookies()
        self.scraper.add_cookies(cookies)
        self.scraper.get_page_and_wait_to_load(ROOT_URL)

        try:
            self.scraper.find('ID', 'mbasic_logout_button')
        except:
            raise Exception('The logout button was not found. Assuming the login attempt has failed.')

        return self.scraper.get_cookies()

    # Login and return cookies, otherwise raise an exception
    def login(self, account: Account) -> str:
        if account.get_cookies() is not None:
            try:
                return self.login_using_cookies(account)
            except:
                print('Tried to log in using cookies, but no success.')

        # self.scraper.delete_all_cookies()
        
        cookies = self.login_using_credentials(account)

        return cookies


    def get_buddylist(self) -> str:
        html = self.get_html_from_url(MESSENGER_HOME)
        time.sleep(1.5)
        self.scraper.driver.execute_script("window.stop();")
        return html

    def get_chat(self, ref: Ref):
        return self.get_html_from_url(
            ref.get_full_url_to_chat()
        )

    def clear_session(self):
        self.scraper.delete_all_cookies()

    def close_browser(self):
        self.scraper.close_browser()

    def send_message(self, ref: Ref, body):
        self.scraper.get_page_and_wait_to_load(
            ref.get_full_url_to_chat()
        )

        textarea = self.scraper.find_by_tag_name('textarea')
        submit_button = self.scraper.find('XPATH', '//input[@value="Send"]')

        textarea.send_keys(body)
        submit_button.click()