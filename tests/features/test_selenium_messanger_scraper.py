from tests.base_test import BaseTest
from env import FACEBOOK_TEST_ACCOUNTS, SELENIUM_WEBDRIVER_PATH
from multi.scrapers.selenium_messenger_scraper import SeleniumMessengerScraper

class SeleniumMessangerScraperTest(BaseTest):

    def setUp(self) -> None:
        if len(FACEBOOK_TEST_ACCOUNTS) != 2:
            raise Exception('2 Facebook test accounts are required. Add them in .env')

        self.scraper = SeleniumMessengerScraper(SELENIUM_WEBDRIVER_PATH)

    def test_login_and_return_cookies_then_login_just_using_cookies(self) -> None:
        account = FACEBOOK_TEST_ACCOUNTS[0]
        account.set_cookies(None)rfsdf
        cookies = self.scraper.login(account)
        self.scraper.clear_session()
        account.set_cookies(cookies)
        self.scraper.login(account)

    def test_login_using_credentials_if_cookies_dont_work(self):
        account = FACEBOOK_TEST_ACCOUNTS[0]
        account.set_cookies({'name': 'some_fake_cookies', 'value': 'it wont work'})
        self.scraper.login(account)
    #
    # def test_raise_an_exception_if_neither_cookies_nor_credentials_work(self):
    #     pass
    #
    # def test_raise_an_exception_if_the_website_is_broken(self):
    #     pass
    #
    # def test_no_unread_messages_in_the_buddylist(self):
    #     pass
    #
    # def test_send_messages(self):
    #     pass
    #
    # def test_get_the_unread_refs_in_the_buddylist(self):
    #     pass
    #
    # def test_read_the_messages(self):
    #     pass
    #
    # def tearDown(self) -> None:
    #     del self.scraper