from selenium.webdriver.common.by import By


class LocatorsQuestions:
#Раздел с вопросами
    QUESTIONS_LIST = (By.XPATH, ".//div[text='Вопросы о важном']")
#Кнопки с вопросами
    BUTTON_QUESTION = [
        (By.ID, 'accordion__heading-0'),
        (By.ID, 'accordion__heading-1'),
        (By.ID, 'accordion__heading-2'),
        (By.ID, 'accordion__heading-3'),
        (By.ID, 'accordion__heading-4'),
        (By.ID, 'accordion__heading-5'),
        (By.ID, 'accordion__heading-6'),
        (By.ID, 'accordion__heading-7')
    ]

#Текст с ответами
    ANSWER = [
        (By.ID, 'accordion__panel-0'),
        (By.ID, 'accordion__panel-1'),
        (By.ID, 'accordion__panel-2'),
        (By.ID, 'accordion__panel-3'),
        (By.ID, 'accordion__panel-4'),
        (By.ID, 'accordion__panel-5'),
        (By.ID, 'accordion__panel-6'),
        (By.ID, 'accordion__panel-7')
    ]
