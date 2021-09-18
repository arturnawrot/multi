from flask import Flask
from multi.scrapers.selenium_messenger_scraper import SeleniumMessengerScraper
from multi.entities.account import Account
from multi.locators.navbar.navbar_locator import NavbarLocator
from env import SELENIUM_WEBDRIVER_PATH
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def index():
    account = Account('stephenconroy30809@gmail.com', 'Myszka1234511!')
    number_of_unread_messages = get_updates(account)
    return str(number_of_unread_messages)
    # return jsonify([e.serialize() for e in refs])

def get_updates(account: Account):
    scraper = SeleniumMessengerScraper(SELENIUM_WEBDRIVER_PATH)
    navbar_locator = NavbarLocator()

    scraper.login(account)

    number_of_unread_messages = navbar_locator.get_number_of_unread_messages(
        scraper.get_buddylist()
    )

    scraper.close_browser()

    return number_of_unread_messages

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')