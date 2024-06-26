from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Главная страница. Клик по лого "Самокат".')
    def click_logo_scooter(self):
        self.click_on_element(MainPageLocators.order_button_header)
        self.click_on_element(MainPageLocators.logo_scooter)

    @allure.step('Подвердить переход на главную страницу.')
    def check_move_to_main_page(self):
        return self.get_text_of_element(MainPageLocators.main_text)

    @allure.step('Главная страница. Клик по лого "Яндекс". Проверка перехода на страницу Яндекс.Дзен.')
    def check_move_to_dzen(self):
        self.open_page_in_new_tab(MainPageLocators.logo_yandex, "Дзен")
        return self.check_current_url()


