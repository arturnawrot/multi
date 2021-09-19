from flask import Flask
from multi.scrapers.selenium_messenger_scraper import SeleniumMessengerScraper
from multi.entities.account import Account
from multi.locators.navbar.navbar_locator import NavbarLocator
from env import SELENIUM_WEBDRIVER_PATH
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def index():
    account = Account(request.form['email'], request.form['password'])
    number_of_unread_messages = get_updates(account)
    return str(number_of_unread_messages)

    # return jsonify([e.serialize() for e in refs])

def get_updates(account: Account):
    try:
        scraper = SeleniumMessengerScraper(SELENIUM_WEBDRIVER_PATH, True)
        navbar_locator = NavbarLocator()

        scraper.login(account)

        number_of_unread_messages = navbar_locator.get_number_of_unread_messages(
            scraper.get_buddylist()
        )

        scraper.close_browser()
    except Exception:
        scraper.close_browser()
        return -1

    return number_of_unread_messages

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')