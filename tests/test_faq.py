import pytest
from pages.main_page import MainPage
from data import TestData


class TestFaq:

    @pytest.mark.parametrize("index, expected_answer", TestData.FAQ_DATA)

    def test_faq_answer(self, driver, index, expected_answer):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()

        main_page.click_faq_question(index)
        actual_answer = main_page.get_faq_answer_text(index)
        assert expected_answer in actual_answer