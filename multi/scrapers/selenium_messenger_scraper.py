from multi.selenium.selenium_client import SeleniumClient
from multi.scrapers.urls import MESSENGER_HOME, LOGIN_PAGE, ROOT_URL
from multi.entities.account import Account
from multi.entities.ref import Ref
import time

class SeleniumMessengerScraper:

    def __init__(self, path):
        self.scraper = SeleniumClient(path)

    def get_html_from_url(self, url: str) -> str:
        self.scraper.get_page(url)
        return self.scraper.get_html()

    def login_using_credentials(self, account: Account):
        self.scraper.get_page_and_wait_to_load(LOGIN_PAGE)

        time.sleep(1)

        try:
            login_input = self.scraper.find('ID', 'm_login_email')
        except:
            raise Exception('Login input was not found.')

        login_input.send_keys(account.get_email())

        time.sleep(1)

        try:
            password_input = self.scraper.find('NAME', 'pass')
        except:
            raise Exception('Password input was not found')

        password_input.send_keys(account.get_password())

        time.sleep(1)

        try:
            login_button = self.scraper.find('NAME', 'login')
        except:
            raise Exception('Login button was not found')

        login_button.click()

        return self.scraper.get_cookies()

    def login_using_cookies(self, account: Account):
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
                pass

        return self.login_using_credentials(account)

    def get_buddylist(self) -> str:
        return self.get_html_from_url(MESSENGER_HOME)

    def get_chat(self, ref: Ref):
        return self.get_html_from_url(
            ref.get_full_url_to_chat()
        )

    def clear_session(self):
        self.scraper.delete_all_cookies()

    def close_browser(self):
        self.scraper.close_browser()

    def __del__(self):
        self.close_browser()