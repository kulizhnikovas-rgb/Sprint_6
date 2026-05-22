import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrderFlow:
    
    @pytest.mark.parametrize("entry_point, name, surname, address, metro, phone, date, period, color, comment",
        [
        ("top", "Иван", "Петров", "ул. Ленина, д. 5", "Черкизовская", "79991112233", "25.10.2026", "сутки", "black", "Позвоните за час"),
        ("bottom", "Анна", "Смирнова", "пр. Мира, д. 12, кв. 4", "Сокольники", "89995554422", "30.11.2026", "двое суток", "grey", "Оставить у двери")
                             ],)
    def test_order_scooter_success(self, driver, entry_point, name, surname, address, metro, phone, date, period, color, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open()
        main_page.accept_cookies()

        if entry_point == "top":
            main_page.click_button_order()
        else:
            main_page.click_footer_order()

        order_page.fill_personal_data(name, surname, address, metro, phone)
        order_page.fill_rent_data(date, period, color, comment)

        success_text = order_page.get_success_popup_text()
        assert "Заказ оформлен" in success_text


class TestHeaderLogos:
    
    def test_click_scooter_logo_opens_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()

        main_page.click_button_order()
        main_page.click_scooter_logo()

        assert driver.current_url == main_page.base_url

    def test_click_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()

        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        main_page.wait_for_url_contains("dzen.ru")
        assert "dzen.ru" in driver.current_url
