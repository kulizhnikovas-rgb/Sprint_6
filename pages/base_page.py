from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



class BasePage:

    TIMEOUT = 5
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru/'

    def open(self):
        self.driver.get(self.base_url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(expected_conditions.presence_of_element_located(locator))
    
    def click_element(self, locator):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(expected_conditions.element_to_be_clickable(locator))
        element.click()

    def fill_field(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text
    
    def scroll_to_element(self, locator):
         element = WebDriverWait(self.driver, self.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(locator)
        )
         return element.text


    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_for_url_contains(self, text):
        return WebDriverWait(self.driver, self.TIMEOUT).until(expected_conditions.url_contains(text))
    