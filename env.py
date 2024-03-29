import os
from multi.entities.account import Account

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_DIR = os.path.join(ROOT_DIR, r'tests\fixtures')
SELENIUM_WEBDRIVER_PATH = os.path.join(ROOT_DIR, r'geckodriver.exe')

FACEBOOK_TEST_ACCOUNTS = [
    Account('******@gmail.com', 'Myszka1234511!', None, '/messages/read/?fbid=100063745055206&click_type=buddylist#fua', 'Paul'),
    Account('stephenconroy30809@gmail.com', 'Myszka1234511!', None, '/messages/read/?fbid=100063488482176', 'Stephen')
]

ADMIN_ADDR = 'http://localhost:8000'