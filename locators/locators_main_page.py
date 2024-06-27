from selenium.webdriver.common.by import By


class LocatorsMainPage:
                #ГЛАВНАЯ СТРАНИЦА

# Кнопка принятия куки
    ACCEPT_COOKIES = (By.ID, 'rcc-confirm-button')
#Ссылка на Яндекс Дзен
    DZEN = (By.XPATH, ".//a[@href='https://yandex.ru/']")
#Ссылка на главную страницу Яндекс Самокат
    SAMOKAT = (By.XPATH, ".//a[@href='/']")
#Кнопка "Заказать"
    ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')
#Кнопка "Статус заказа"
    STATUS_ORDER_BUTTON = (By.CLASS_NAME, 'Header_Link__1TAG7')
#Поле ввода номера заказа
    ORDER_NUMBER = (By.XPATH, "//input[@placeholder='Введите номер заказа']")
#Кнопка "GO!"
    GO_BUTTON = (By.LINK_TEXT, 'GO!')
#Кнопка "Зказать" внизу страницы
    ORDER_BUTTON_BOTTOM = (By.CLASS_NAME, 'Button_Button__ra12g Button_UltraBig__UU3Lp')
#Кнопка принятия куки
    ACCEPT_COOKIES = (By.ID, 'rcc-confirm-button')