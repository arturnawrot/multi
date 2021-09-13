from flask import Flask
from multi.scrapers.selenium_messenger_scraper import SeleniumMessengerScraper
from multi.entities.account import Account
from multi.locators.list.list_locator import ListLocator
from env import SELENIUM_WEBDRIVER_PATH
from flask import jsonify

FLASK_ENV="development"

scraper = SeleniumMessengerScraper(SELENIUM_WEBDRIVER_PATH)
list_locator = ListLocator()

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(['e2sa', 23])

def get_updates(account: Account):
    account = Account('stephenconroy30809@gmail.com', 'Myszka1234511!')
    scraper.login(account)

    return list_locator.get_refs(
        scraper.get_buddylist()
    )