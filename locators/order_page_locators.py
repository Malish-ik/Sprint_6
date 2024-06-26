from selenium.webdriver.common.by import By


class OrderPageLocators:

    order_button_header = [By.XPATH, "//*[contains(@class, 'Button_Button') and text()='Заказать' and not(contains(@class, 'Button_Middle'))]"]
    order_button_body = [By.XPATH, "//*[contains(@class, 'Button_Middle') and text()='Заказать']"]
    personal_info_form = [By.XPATH, ".//div[text()= 'Для кого самокат']"]
    rent_form = [By.XPATH, ".//div[text()= 'Про аренду']"]
    name_input = [By.XPATH, ".//input[@placeholder='* Имя']"]
    surname_input = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    address_input = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    metro_station_input = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    choose_station = [By.XPATH, ".//div[text()='{}']"]
    phone_number_input = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    button_next = [By.XPATH, ".//button[text()= 'Далее']"]

    delivery_time_input = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    deliver_time_value = [By.XPATH, ".//div[@class='{}']"]
    delivery_date = [By.XPATH, ".//div[@class='{}']"]
    duration_input = [By.XPATH, ".//div[@class='Dropdown-control']"]
    duration_value = [By.XPATH, ".//div[text()='{}']"]
    scooter_color = [By.XPATH, ".//div[text()='Цвет самоката']"]
    choose_color = [By.XPATH, ".//label[@for='{}']"]
    comment_input = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]
    order_accept_button = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    block_of_order = [By.XPATH, ".//div[contains(@class, 'Order_Form__17u6u')]"]
    button_yes = [By.XPATH, ".//button[text()= 'Да']"]
    button_no = [By.XPATH, ".//button[text()= 'Нет']"]
    button_status = [By.XPATH, ".//button[text()= 'Посмотреть статус']"]

    order_number_input = [By.XPATH, ".//input[@placeholder='Введите номер заказа']"]