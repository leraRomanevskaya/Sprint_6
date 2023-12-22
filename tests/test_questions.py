import allure
import pytest

from locators.main_page_locators import MainPageLocators
from testdata import HOW_MUCH_DOES_IT_COST_ANSWER_TEXT, WANT_SOME_SCOOTERS_ANSWER_TEXT, HOW_TIME_IS_CALCULATED_ANSWER_TEXT, \
    CAN_I_ORDER_A_SCOOTER_TODAY_ANSWER_TEXT, EXTENDED_THE_ORDER_ANSWER_TEXT, CHARGING_WITH_A_SCOOTER_ANSWER_TEXT, \
    CANCEL_THE_ORDER_ANSWER_TEXT, LIFE_BEYOND_THE_MKAD_ANSWER_TEXT


class TestQuestions:

    @allure.title('Проверка соответствия текста ответа для вопроса в выпадающем списке')
    @allure.description('Проверка соответствия текста ответа для вопроса в выпадающем списке')
    @pytest.mark.parametrize(
        'question_locator, answer_locator, answer_text',
        [
            [MainPageLocators.HOW_MUCH_DOES_IT_COST_QUESTION, MainPageLocators.HOW_MUCH_DOES_IT_COST_ANSWER, HOW_MUCH_DOES_IT_COST_ANSWER_TEXT],
            [MainPageLocators.WANT_SOME_SCOOTERS_QUESTION, MainPageLocators.WANT_SOME_SCOOTERS_ANSWER, WANT_SOME_SCOOTERS_ANSWER_TEXT],
            [MainPageLocators.HOW_TIME_IS_CALCULATED_QUESTION, MainPageLocators.HOW_TIME_IS_CALCULATED_ANSWER, HOW_TIME_IS_CALCULATED_ANSWER_TEXT],
            [MainPageLocators.CAN_I_ORDER_A_SCOOTER_TODAY_QUESTION, MainPageLocators.CAN_I_ORDER_A_SCOOTER_TODAY_ANSWER, CAN_I_ORDER_A_SCOOTER_TODAY_ANSWER_TEXT],
            [MainPageLocators.EXTENDED_THE_ORDER_QUESTION, MainPageLocators.EXTENDED_THE_ORDER_ANSWER, EXTENDED_THE_ORDER_ANSWER_TEXT],
            [MainPageLocators.CHARGING_WITH_A_SCOOTER_QUESTION, MainPageLocators.CHARGING_WITH_A_SCOOTER_ANSWER, CHARGING_WITH_A_SCOOTER_ANSWER_TEXT],
            [MainPageLocators.CANCEL_THE_ORDER_QUESTION, MainPageLocators.CANCEL_THE_ORDER_ANSWER, CANCEL_THE_ORDER_ANSWER_TEXT],
            [MainPageLocators.LIFE_BEYOND_THE_MKAD_QUESTION, MainPageLocators.LIFE_BEYOND_THE_MKAD_ANSWER, LIFE_BEYOND_THE_MKAD_ANSWER_TEXT],
        ]
    )
    def test_questions_and_answers(self, main_page, question_locator, answer_locator, answer_text):
        question_view = main_page.find_view(question_locator)
        main_page.scroll_to_view(question_view)
        main_page.wait_until_visible(5, question_locator)
        question_view.click()
        answer_view = main_page.find_view(answer_locator)
        assert answer_view.text == answer_text
