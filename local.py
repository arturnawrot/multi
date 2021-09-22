from multi.scrapers.selenium_messenger_scraper import SeleniumMessengerScraper
from multi.entities.account import Account
from env import SELENIUM_WEBDRIVER_PATH
import sys
import requests
import time

try:

    data = requests.utils.unquote(sys.argv[1])
    data = data.replace("multi:", "")

    data = data.split()

    email = data[0]
    password = data[1]

    account = Account(email, password)
    
    if(len(data) > 2):
        cookies = ' '.join(data[2:])
        account.set_cookies(cookies)

    # print(account.get_cookies())
    # input('enter')

    scraper = SeleniumMessengerScraper(SELENIUM_WEBDRIVER_PATH, False)

    cookies = scraper.login(account)
    scraper.switch_to_new_version()

except Exception as e:
    print(e)
    input("\n Press enter to exit")
