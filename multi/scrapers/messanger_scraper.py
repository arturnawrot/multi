from multi.selenium.selenium_client import SeleniumClient
from multi.scrapers.urls import MESSENGER_HOME, LOGIN_PAGE, ROOT_URL
from multi.entities.account import Account
from multi.entities.ref import Ref

class MessengerScraper:

    def __init__(self):
        self.scraper = SeleniumClient()

    def get_html_from_url(self, url: str) -> str:
        self.scraper.get_page(url)
        return self.scraper.get_html()

    # Login and return cookies, otherwise raise an exception
    def login(self, account: Account) -> str:
        # @TODO
        # self.scraper.get_page(LOGIN_PAGE)
        pass

    def get_messenger_home_html(self) -> str:
        return self.get_html_from_url(MESSENGER_HOME)

    # url = '/message/read/?some=parameters
    def get_chat_html(self, url):
        return self.get_html_from_url(ROOT_URL + url)
