import allure

import data
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    button_order = 0
    @allure.step('Клик по кнопке Заказать(header).')
    def click_order_button_header(self):
        self.click_on_element(MainPageLocators.order_button_header)
        self.find_element_and_wait(OrderPageLocators.personal_info_form)

    @allure.step('Клик по кнопке Заказать(body).')
    def click_order_button_body(self):
        self.click_on_element(MainPageLocators.order_button_body)
        self.find_element_and_wait(OrderPageLocators.personal_info_form)


    @allure.step('Заполнение полей формы "Для кого самокат"')
    def set_personal_info(self, name, surname, address, metro_station, phone):
        if self.button_order == 0:
            self.click_order_button_header()
            self.button_order = 1
        else:
            self.click_order_button_body()
            self.button_order = 0
        self.set_text_to_input_field(OrderPageLocators.name_input, name)
        self.set_text_to_input_field(OrderPageLocators.surname_input, surname)
        self.set_text_to_input_field(OrderPageLocators.address_input, address)
        self.click_on_element(OrderPageLocators.metro_station_input)
        method_m, locator_m = OrderPageLocators.choose_station
        locator_m = locator_m.format(metro_station)
        self.scroll_and_click((method_m, locator_m))
        self.set_text_to_input_field(OrderPageLocators.phone_number_input, phone)
        self.click_on_element(OrderPageLocators.button_next)


    @allure.step('Заполнение полей формы "Про аренду"')
    def set_rent_info(self, date, duration, color, comment):
        self.find_element_and_wait(OrderPageLocators.rent_form)
        self.set_text_to_input_field_and_press_enter(OrderPageLocators.delivery_time_input, date)
        '''self.click_on_element(OrderPageLocators.delivery_time_input)
        method_dd, locator_dd = OrderPageLocators.delivery_date
        locator_dd = locator_dd.format(date)
        self.click_on_element((method_dd, locator_dd))'''
        self.click_on_element(OrderPageLocators.duration_input)
        method_d, locator_d = OrderPageLocators.duration_value
        locator_d = locator_d.format(duration)
        self.click_on_element((method_d, locator_d))
        self.find_element_and_wait(OrderPageLocators.scooter_color)
        method_sc, locator_sc = OrderPageLocators.choose_color
        locator_sc = locator_sc.format(color)
        self.click_on_element((method_sc, locator_sc))
        self.click_on_element(OrderPageLocators.comment_input)
        self.set_text_to_input_field(OrderPageLocators.comment_input, comment)
        self.click_on_element(OrderPageLocators.order_accept_button)
        self.find_element_and_wait(OrderPageLocators.block_of_order)
        self.click_on_element(OrderPageLocators.button_yes)

    @allure.step('Окно- уведомление об успешном создании заказа. Получение текста кнопки Посмотреть статус.')
    def get_button_text(self):
        return self.get_text_of_element(OrderPageLocators.button_status)

    @allure.step('Проверка, что текст кнопки - Посмотреть статус.')
    def check_button_text(self, result, button_text):
        assert result == button_text











