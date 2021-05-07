from multi.selenium.selenium_client import SeleniumClient
from multi.scrapers.urls import MESSENGER_HOME, LOGIN_PAGE, ROOT_URL
from multi.entities.account import Account
from multi.entities.ref import Ref

class SeleniumMessengerScraper:

    def __init__(self, path):
        self.scraper = SeleniumClient(path)

    def get_html_from_url(self, url: str) -> str:
        self.scraper.get_page(url)
        return self.scraper.get_html()

    # Login and return cookies, otherwise raise an exception
    def login(self, account: Account) -> str:
        # @TODO
        # self.scraper.get_page(LOGIN_PAGE)
        pass

    def get_buddylist(self) -> str:
        return self.get_html_from_url(MESSENGER_HOME)

    def get_chat(self, ref: Ref):
        return self.get_html_from_url(
            ref.get_full_url_to_chat()
        )

    def __del__(self):
        self.scraper.close_browser()