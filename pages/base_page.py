from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def check_current_url(self):
        return self.driver.current_url

    def find_element_and_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        self.find_element_and_wait(locator).click()

    def get_text_of_element(self, locator):
        return self.find_element_and_wait(locator).text

    def set_text_to_input_field(self, locator, text):
        self.find_element_and_wait(locator).send_keys(text)

    def set_text_to_input_field_and_press_enter(self, locator, text):
        element = self.find_element_and_wait(locator)
        element.send_keys(text)
        element.send_keys(Keys.ENTER)


    def scroll_to_element(self, locator):
        self.driver.execute_script('arguments[0].scrollIntoView();', self.driver.find_element(*locator))

    def open_page_in_new_tab(self, locator, title):
        wait = WebDriverWait(self.driver, 10)
        original_window = self.driver.current_window_handle
        self.click_on_element(locator)
        wait.until(expected_conditions.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        wait.until(expected_conditions.title_is(title))

    def scroll_and_click(self, locator):
        self.scroll_to_element(locator)
        self.find_element_and_wait(locator)
        self.click_on_element(locator)
