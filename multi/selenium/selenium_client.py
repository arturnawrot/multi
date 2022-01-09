from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class SeleniumClient:

    def __init__(self, path, options=None):
        caps = DesiredCapabilities().FIREFOX
        caps["pageLoadStrategy"] = "eager"  #  interactive

        driver = webdriver.Firefox(executable_path=path, options=options, capabilities=caps)
        self.driver = driver

    def set_up_screen_resolution(self, x, y):
        self.driver.set_window_size(x, y)

    def get_page(self, url):
        self.driver.get(url)

    def get_page_and_wait_to_load(self, url, timeout=15):
        self.get_page(url)

        seconds = 0
        while self.page_has_loaded() is False:
            if seconds > timeout:
                raise Exception('It took to long to load the page: ' + url)

            time.sleep(1)
            seconds =+ 1

    def wait_and_find_all(self, by_property, locator_name):
        return self.create_web_driver_wait().until(
            EC.presence_of_all_elements_located(self.create_locator(by_property, locator_name))
        )

    def wait_and_find(self, by_property, locator_name):
        return self.create_web_driver_wait().until(
            EC.presence_of_element_located(self.create_locator(by_property, locator_name))
        )

    def find(self, by_property, locator_name):
        return self.driver.find_element(
            *self.create_locator(by_property, locator_name)
        )

    def find_all(self, by_property, locator_name):
        return self.driver.find_elements(
            *self.create_locator(by_property, locator_name)
        )

    @staticmethod
    def create_locator(by_property, locator_name):
        return getattr(By, by_property), locator_name

    def create_web_driver_wait(self, waiting_time=8):
        return WebDriverWait(self.driver, waiting_time)

    def click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def get_current_url(self):
        return self.driver.current_url

    def get_html(self):
        return self.driver.find_element_by_xpath("//*").get_attribute("outerHTML")

    def find_possible_element(self, possible_selectors):
        for possible_selector in possible_selectors:
            try:
                return self.find(possible_selector[0], possible_selector[1])
            except NoSuchElementException:
                pass

        raise NoSuchElementException("Element was not found")

    def close_browser(self) -> None:
        self.driver.quit()

    def add_cookies(self, cookies: dict) -> None:
        for cookie in cookies:
            # example_cookie = {'name': 'lang', 'value': 'en-US'}
            self.driver.add_cookie(cookie)

    def page_has_loaded(self):
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'

    def get_cookies(self):
        return self.driver.get_cookies()

    def delete_all_cookies(self):
        return self.driver.delete_all_cookies()

    def find_by_tag_name(self, tag_name: str):
        return self.driver.find_element_by_tag_name(tag_name)

    def open_new_tab(self, url: str) -> None:
        self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
        self.get_page_and_wait_to_load(url)
