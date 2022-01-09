from flask import Flask
from multi.scrapers.selenium_messenger_scraper import SeleniumMessengerScraper
from multi.entities.account import Account
from multi.locators.navbar.navbar_locator import NavbarLocator
from env import SELENIUM_WEBDRIVER_PATH
from flask import jsonify
from flask import request
import json
import requests
from env import ADMIN_ADDR

app = Flask(__name__)

# @app.route("/terminator", methods=['POST'])
# def terminator():
#     pass

@app.route("/", methods=['POST'])
def index():
    account = get_account_from_request()

    number_of_unread_messages = get_updates(account)
    return str(number_of_unread_messages)

    # return jsonify([e.serialize() for e in refs])

def get_updates(account: Account):
    scraper = SeleniumMessengerScraper(SELENIUM_WEBDRIVER_PATH, True)

    try:
        navbar_locator = NavbarLocator()

        cookies = scraper.login(account)

        send_cookies_to_the_admin_dashboard(cookies, account)

        number_of_unread_messages = navbar_locator.get_number_of_unread_messages(
            scraper.get_buddylist()
        )

        scraper.close_browser()
    except Exception as e:
        scraper.close_browser()

        print(e)

        # If for some reason it does not work then -1 must be returned as a flag for the API.
        return -1

    return number_of_unread_messages

def get_account_from_request():
    account = Account(request.form['email'], request.form['password'])

    if('cookies' in request.form):
        account.set_cookies(request.form['cookies'])

    return account


def send_cookies_to_the_admin_dashboard(cookies: str, account: Account):
    data = {"cookies": json.dumps(cookies), "email": account.get_email()}

    try:
        print('\n Sending cookies to the server')
        print(cookies)
        requests.post(ADMIN_ADDR + '/api/account-info/update', data=data)
    except Exception as e:
        print(e)
        print("\n Error sending cookies to the admin server.")

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')