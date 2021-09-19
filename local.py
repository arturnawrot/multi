from multi.scrapers.selenium_messenger_scraper import SeleniumMessengerScraper
from multi.entities.account import Account
from env import SELENIUM_WEBDRIVER_PATH
import sys
import requests

try:
    data = requests.utils.unquote(sys.argv[1])
    data = data.replace("multi:", "")

    email = data.split()[0]
    password = data.split()[1]

    scraper = SeleniumMessengerScraper(SELENIUM_WEBDRIVER_PATH, False)
    account = Account(email, password)

    scraper.login(account)
    scraper.switch_to_new_version()
except Exception as e:
    print(e)
    input("\n Press enter to exit")
