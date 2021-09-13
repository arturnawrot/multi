from multi.scrapers.selenium_messenger_scraper import SeleniumMessengerScraper
from multi.entities.account import Account
from multi.locators.list.list_locator import ListLocator
from env import SELENIUM_WEBDRIVER_PATH

scraper = SeleniumMessengerScraper(SELENIUM_WEBDRIVER_PATH)
list_locator = ListLocator()

account = Account('stephenconroy30809@gmail.com', 'Myszka1234511!')
scraper.login(account)

print(list_locator.get_refs(
    scraper.get_buddylist()
))