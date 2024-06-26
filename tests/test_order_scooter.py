import allure
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
import pytest
import data


class TestOrderScooter:

    @pytest.mark.parametrize('name, surname, address, station, phone, delivery, rent, color, comment', (
            (
                    (data.names[0], data.surnames[0], data.address[0],
                     data.metro_station[0], data.phones[0], data.delivery_date[0],
                     data.time_rent[0], data.color_scooter[0], data.comment[0]),
                    (data.names[1], data.surnames[1], data.address[1],
                     data.metro_station[1], data.phones[1], data.delivery_date[1],
                     data.time_rent[1], data.color_scooter[1], data.comment[1])
            )
    ))
    @allure.title('Проверка оформления заказа самоката с двумя наборами тестовых данных')
    @allure.description('Клик на кнопку "Заказать", заполнение форм "Для кого самокат" и "Про аренду",\
                        проверка появления окна "Заказ оформлен" с кнопкой "Посмотреть статус"')

    def test_order_info(self, driver, name, surname, address, station, phone, delivery, rent, color, comment):
        order_page = OrderPage(driver)
        order_page.set_personal_info(name, surname, address, station, phone)
        order_page.set_rent_info(delivery, rent, color, comment)
        result = order_page.get_button_text()
        assert result == 'Посмотреть статус'

