from tests.base_test import BaseTest
from env import FACEBOOK_TEST_ACCOUNTS, SELENIUM_WEBDRIVER_PATH
from multi.scrapers.selenium_messenger_scraper import SeleniumMessengerScraper
from multi.locators.list.list_locator import ListLocator
from multi.locators.chat.chat_locator import ChatLocator
from multi.entities.ref import Ref
from random import randrange
import time
import unittest

class SeleniumMessangerScraperTest(BaseTest):

    unittest.TestLoader.sortTestMethodsUsing = None

    def setUp(self) -> None:
        if len(FACEBOOK_TEST_ACCOUNTS) != 2:
            raise Exception('2 Facebook test accounts are required. Add them in .env')

        self.scraper = SeleniumMessengerScraper(SELENIUM_WEBDRIVER_PATH)
        self.list_locator = ListLocator()
        self.chat_locator = ChatLocator()

    def test_login_and_return_cookies_then_login_just_using_cookies(self) -> None:
        account = FACEBOOK_TEST_ACCOUNTS[0]
        account.set_cookies(None)
        cookies = self.scraper.login(account)
        self.scraper.clear_session()
        account.set_cookies(cookies)
        self.scraper.login(account)

    def test_login_using_credentials_if_cookies_dont_work(self):
        account = FACEBOOK_TEST_ACCOUNTS[0]
        account.set_cookies({'name': 'some_fake_cookies', 'value': 'it wont work'})
        self.scraper.login(account)

    def test_raise_an_exception_if_neither_cookies_nor_credentials_work(self):
        pass

    def test_raise_an_exception_if_the_website_is_broken(self):
        pass


    def test_get_the_unread_refs_in_the_buddylist(self):
        account1 = FACEBOOK_TEST_ACCOUNTS[0]
        account2 = FACEBOOK_TEST_ACCOUNTS[1]
        ref = Ref(None, account2.get_chat_link(), 0)
        self.scraper.login(account1)
        self.scraper.send_message(ref, "Hi, what's up? " + str(randrange(10)))

        self.scraper.clear_session()

        self.scraper.login(account2)
        refs = self.list_locator.get_refs(
            self.scraper.get_buddylist()
        )

        success = False

        for ref in refs:
            if ref.name == account1.name:
                success = True

        if not success:
            raise Exception('Message was not received')

    # def test_no_unread_messages_in_the_buddylist(self):
    #     refs = self.list_locator.get_refs(
    #         self.scraper.get_buddylist()
    #     )
    #
    #     pass
    #
    #
    # def test_read_the_messages(self):
    #     pass

    def tearDown(self) -> None:
        del self.scraper