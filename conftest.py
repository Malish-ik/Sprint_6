import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--width=1080")
    firefox_options.add_argument("--height=800")
    driver = webdriver.Firefox(options=firefox_options)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    driver.find_element(By.ID, "rcc-confirm-button").click()
    yield driver
    driver.quit()