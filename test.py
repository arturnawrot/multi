from multi.scrapers.selenium_messenger_scraper import SeleniumMessengerScraper
from multi.entities.account import Account
from multi.locators.navbar.navbar_locator import NavbarLocator
from env import SELENIUM_WEBDRIVER_PATH

scraper = SeleniumMessengerScraper(SELENIUM_WEBDRIVER_PATH)
navbar_locator = NavbarLocator()

account = Account('stephenconroy30809@gmail.com', 'Myszka1234511!')
scraper.login(account)

print(navbar_locator.get_number_of_unread_messages(
    scraper.get_buddylist()
))