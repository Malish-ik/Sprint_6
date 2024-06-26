import allure
from pages.questions_page import QuestionsPage
import pytest
import data


class TestQuestionsPage:

    @pytest.mark.parametrize('num, answer', (
        (0, data.answers[0]),
        (1, data.answers[1]),
        (2, data.answers[2]),
        (3, data.answers[3]),
        (4, data.answers[4]),
        (5, data.answers[5]),
        (6, data.answers[6]),
        (7, data.answers[7])
    ))
    @allure.title('Проверка текста ответов в блоке "Вопросы о важном"')
    @allure.description('Главная страница. Скролл до блока "Вопросы о важном". \
                         Клик на вопрос, проверка отображения текста ответа')
    def test_answers(self, driver, num, answer):
        question_page = QuestionsPage(driver)
        question_page.scroll_to_last_question()
        result = question_page.click_on_element_and_get_text(str(num))
        assert question_page.check_answer_text(result, answer), \
            f'Ожидаемый результат: "{answer}", фактический результат: "{result}"'
