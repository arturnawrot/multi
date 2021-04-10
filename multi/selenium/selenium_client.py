from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class SeleniumClient:

    def __init__(self):
        driver = webdriver.Firefox()
        self.driver = driver

    def set_up_screen_resolution(self, x, y):
        self.driver.set_window_size(x, y)

    def get_page(self, url):
        self.driver.get(url)

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