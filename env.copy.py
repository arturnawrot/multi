import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_DIR = os.path.join(ROOT_DIR, r'tests\fixtures')
SELENIUM_WEBDRIVER_PATH = os.path.join(ROOT_DIR, r'geckodriver.exe')

FACEBOOK_TEST_ACCOUNTS = [
    Account('jack@gmail.com', 'admin123'),
    Account('john@gmail.com', 'qwerty')
]

ADMIN_ADDR = 'http://localhost:8000'