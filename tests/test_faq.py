import pytest
from pages.main_page import MainPage


class TestFaq:

    def test_faq_question_0_returns_correct_answer(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_faq_question(0)
        actual_answer = main_page.get_faq_answer_text(0)
        assert (
            actual_answer
            == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        )

    def test_faq_question_1_returns_correct_answer(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_faq_question(1)
        actual_answer = main_page.get_faq_answer_text(1)
        assert (
            actual_answer
            == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        )

    def test_faq_question_2_returns_correct_answer(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_faq_question(2)
        actual_answer = main_page.get_faq_answer_text(2)
        assert (
            actual_answer
            == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        )

    def test_faq_question_3_returns_correct_answer(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_faq_question(3)
        actual_answer = main_page.get_faq_answer_text(3)
        assert (
            actual_answer
            == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        )

    def test_faq_question_4_returns_correct_answer(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_faq_question(4)
        actual_answer = main_page.get_faq_answer_text(4)
        assert (
            actual_answer
            == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        )

    def test_faq_question_5_returns_correct_answer(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_faq_question(5)
        actual_answer = main_page.get_faq_answer_text(5)
        assert (
            actual_answer
            == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        )

    def test_faq_question_6_returns_correct_answer(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_faq_question(6)
        actual_answer = main_page.get_faq_answer_text(6)
        assert (
            actual_answer
            == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        )

    def test_faq_question_7_returns_correct_answer(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_faq_question(7)
        actual_answer = main_page.get_faq_answer_text(7)
        assert (
            actual_answer
            == "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        )