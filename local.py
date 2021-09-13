from multi.scrapers.selenium_messenger_scraper import SeleniumMessengerScraper
from multi.locators.list.list_locator import ListLocator
from multi.entities.account import Account
from env import SELENIUM_WEBDRIVER_PATH

scraper = SeleniumMessengerScraper(SELENIUM_WEBDRIVER_PATH)
account = Account('stephenconroy30809@gmail.com', 'Myszka1234511!')

scraper.login(account)
scraper.switch_to_new_version()