import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestMainTransitions:


    @allure.title('Переход на главную страницу по клику на лого "Самокат"')
    @allure.description('Клик на кнопку "Заказать", клик на лого "Самокат", \
                        происходит переход на главную страницу приложения')
    def test_transition_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.click_logo_scooter()
        assert main_page.get_text_of_element(MainPageLocators.main_text) == 'Самокат\nна пару дней\nПривезём его прямо к вашей двери,\nа когда накатаетесь — заберём'

    @allure.title('Переход на главную страницу "Дзен" по клику на лого "Яндекс"')
    @allure.description('Клик на лого "Яндекс". Открывается главная страница "Дзен". Проверяем url')
    def test_transition_logo_dzen(self, driver):
        main_page = MainPage(driver)
        assert main_page.check_move_to_dzen() == "https://dzen.ru/?yredirect=true"

