import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class OrderPage(BasePage):
    INPUT_NAME = (By.XPATH, ".//input[contains(@placeholder, 'Имя')]")
    INPUT_SURNAME = (By.XPATH, ".//input[contains(@placeholder, 'Фамилия')]")
    INPUT_ADDRESS = (By.XPATH, ".//input[contains(@placeholder, 'Адрес')]")
    INPUT_METRO = (By.XPATH, ".//input[contains(@placeholder, 'Станция')]")
    INPUT_PHONE = (By.XPATH, ".//input[contains(@placeholder, 'Телефон')]")
    BUTTON_NEXT = (By.XPATH, './/button[text()="Далее"]')

    INPUT_DATE = (By.XPATH, './/input[contains(@placeholder, "Когда")]')
    DROPDOWN_PERIOD = (By.CLASS_NAME, "Dropdown-placeholder")
    METRO_OPTION = (By.CLASS_NAME, "select-search__row")
    INPUT_COMMENT = (By.XPATH, './/input[contains(@placeholder, "Комментарий")]')

    CHECKBOX_COLOR_BLACK = (By.ID, "black")
    CHECKBOX_COLOR_GREY = (By.ID, "grey")
    DROPDOWN_SELECTED = (By.CSS_SELECTOR, ".Dropdown-placeholder.is-selected")
    BUTTON_ORDER = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    BUTTON_CONFIRM_YES = (By.XPATH, ".//button[text()='Да']")
    POPUP_SUCCESS_HEADER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    RENT_HEADER = (By.CLASS_NAME, "Order_Header__B1w_M")

    def get_period_option_locator(self, period_text):
        return (By.XPATH , f".//div[@class='Dropdown-option' and text()='{period_text}']")
    
    def get_color_checkbox_locator(self, color_name):
        return(By.ID, color_name)
    
    @allure.step("Заполнить личные данные")
    def fill_personal_data(self, name, surname, address, metro_name, phone):
        self.fill_field(self.INPUT_NAME, name)
        self.fill_field(self.INPUT_SURNAME, surname)
        self.fill_field(self.INPUT_ADDRESS, address)
        
        self.click_element(self.INPUT_METRO)
        self.fill_field(self.INPUT_METRO, metro_name)
        self.click_element(self.METRO_OPTION)

        self.fill_field(self.INPUT_PHONE, phone)
        self.click_element(self.BUTTON_NEXT)
    
    @allure.step("Заполнить параметры проката")
    def fill_rent_data(self, date, period, color, comment):
        date_field = self.find_element(self.INPUT_DATE)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)

        self.click_element(self.DROPDOWN_PERIOD)
        self.click_element(self.get_period_option_locator(period))
        self.click_element(self.get_color_checkbox_locator(color))

        self.fill_field(self.INPUT_COMMENT, comment)
        self.click_element(self.BUTTON_ORDER)
        self.click_element(self.BUTTON_CONFIRM_YES)
    
    @allure.step("Получить текст подтверждения успешного заказа")
    def get_success_popup_text(self):
        return self.get_text(self.POPUP_SUCCESS_HEADER)
    
