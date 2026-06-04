import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import Urls
from data import TestData

class TestOrderFlow:
    
    @pytest.mark.parametrize("button_locator, name, surname, address, metro, phone, date, period, color, comment",
        TestData.ORDER_DATA
    )
    def test_order_scooter_success(self, driver, button_locator, name, surname, address, metro, phone, date, period, color, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open()
        main_page.accept_cookies()

        main_page.scroll_to_element(button_locator)
        main_page.click_element(button_locator)

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

        assert main_page.get_current_url() == Urls.BASE_URL

    def test_click_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()

        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        main_page.wait_for_url_contains(Urls.DZEN_URL)
        assert Urls.DZEN_URL in main_page.get_current_url()
