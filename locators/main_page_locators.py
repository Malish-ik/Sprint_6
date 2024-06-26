from selenium.webdriver.common.by import By

class MainPageLocators:


    order_button_header = [By.XPATH, ".//button[contains(@class, 'Button_Button') and text()='Заказать' and not(contains(@class, 'Button_Middle'))]"]
    order_button_body = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    logo_scooter = [By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]"]
    logo_yandex = [By.XPATH, ".//a[@href= '//yandex.ru']"]
    main_text = [By.XPATH, ".//div[contains(@class, 'Home_Header')]"]
    accept_cookie = [By.ID, "rcc-confirm-button"]