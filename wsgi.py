from flask import Flask
from multi.scrapers.selenium_messenger_scraper import SeleniumMessengerScraper
from multi.entities.account import Account
from multi.locators.list.list_locator import ListLocator
from env import SELENIUM_WEBDRIVER_PATH
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def index():
    account = Account('stephenconroy30809@gmail.com', 'Myszka1234511!')
    refs = get_updates(account)
    return jsonify([e.serialize() for e in refs])

def get_updates(account: Account):
    scraper = SeleniumMessengerScraper(SELENIUM_WEBDRIVER_PATH)
    list_locator = ListLocator()

    scraper.login(account)

    refs = list_locator.get_refs(
        scraper.get_buddylist()
    )

    scraper.close_browser()

    return refs

if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')