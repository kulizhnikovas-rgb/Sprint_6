import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    LOGO_YANDEX = (By.CLASS_NAME,'Header_LogoYandex__3TSOI')
    LOGO_SCOOTER = (By.CLASS_NAME,'Header_LogoScooter__3lsAR')
    ORDER_BUTTON = (By.XPATH, './/button[text()="Заказать"]')
    FOOTER_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Home_ThirdPart')]//button[text()='Заказать']")
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')

    def get_faq_question_locator(self, index):
        return (By.ID, f"accordion__heading-{index}")
    
    def get_faq_answer_locator(self, index):
        return (By.ID, f"accordion__panel-{index}")
    
    @allure.step("Принять куки")
    def accept_cookies(self):
        self.click_element(self.COOKIE_BUTTON)
    
    @allure.step("Нажать на верхнюю кнопку Заказать")
    def click_button_order(self):
        self.click_element(self.ORDER_BUTTON)

    @allure.step("Нажать на нижнюю кнопку Заказать")    
    def click_footer_order(self):
        self.scroll_to_element(self.FOOTER_ORDER_BUTTON)
        self.click_element(self.FOOTER_ORDER_BUTTON)

    @allure.step("Кликнуть по вопросу FAQ под номером {index}")
    def click_faq_question(self, index):
        locator = self.get_faq_question_locator(index)
        self.scroll_to_element(locator)
        self.click_element(locator)
    
    @allure.step("Получить текст ответа FAQ под номером {index}")
    def get_faq_answer_text(self, index):
        locator = self.get_faq_answer_locator(index)
        return self.get_text(locator)
    
    @allure.step("Нажать на логотип Самокат")
    def click_scooter_logo(self):
        self.click_element(self.LOGO_SCOOTER)

    @allure.step("Нажать на логотип Яндекс")
    def click_yandex_logo(self):
        self.click_element(self.LOGO_YANDEX)
    
    