from pages.base_page import BasePage
from locators.questions_page_locators import QuestionsPageLocators
import allure

class QuestionsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Блок куки. Клик по кнопке принять куки.')
    def accept_cookie(self):
        self.click_on_element(QuestionsPageLocators.accept_cookie)

    @allure.step('Блок "Вопросы о важном". Скролл до последнего вопроса.')
    def scroll_to_last_question(self):
        self.scroll_to_element(QuestionsPageLocators.last_question)

    @allure.step('Блок "Вопросы о важном". Клик по вопросу, получение текста ответа.')
    def click_on_element_and_get_text(self, num: str):
        method_q, locator_q = QuestionsPageLocators.question_locator
        locator_q = locator_q + num
        method_a, locator_a = QuestionsPageLocators.answer_locator
        locator_a = locator_a.format(num)
        self.scroll_and_click((method_q, locator_q))
        result = self.get_text_of_element((method_a, locator_a))
        return result

    @allure.step('Блок "Вопросы о важном". Сравнение актуального текста с ожидаемым.')
    def check_answer_text(self, result, answers_text):
        return result == answers_text



