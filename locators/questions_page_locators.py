from selenium.webdriver.common.by import By

class QuestionsPageLocators:

    questions_block = [By.XPATH,  ".//div[@data-accordion-component='Accordion']"]
    last_question = [By.ID, "accordion__heading-7"]
    accept_cookie = [By.ID, "rcc-confirm-button"]
    question_locator = [By.ID, "accordion__heading-"]
    answer_locator = [By.ID, "accordion__panel-{}"]
