import allure
import time
from urls import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



class BasePage:

    TIMEOUT = 5
    def __init__(self, driver):
        self.driver = driver
        self.base_url = Urls.BASE_URL
    
    @allure.step("Открыть страницу")
    def open(self):
        self.driver.get(self.base_url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(expected_conditions.presence_of_element_located(locator))
    
    @allure.step("Кликнуть по элементу")
    def click_element(self, locator):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(expected_conditions.element_to_be_clickable(locator))
        time.sleep(0.3)
        element.click()
    
    @allure.step("Заполнить полле текстом")
    def fill_field(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Получить видимый текст элемента")
    def get_text(self, locator):
        return self.find_element(locator).text
    
    @allure.step("Прокрутить страницу до элемента")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("window.scrollBy(0, -150);")
    
    @allure.step("Переключиться на новую вкладку в браузере")
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Дождаться, когда URL начнет содержать текст: {text}")
    def wait_for_url_contains(self, text):
        return WebDriverWait(self.driver, self.TIMEOUT).until(expected_conditions.url_contains(text))
    
    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url