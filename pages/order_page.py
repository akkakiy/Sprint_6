import allure

from data import MainUser
from locators.locators_page_order import LocatorsPageOrder


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form_name(self):       #Заполнить поле "Имя"
        self.driver.find_element(*LocatorsPageOrder.FIELD_NAME).send_keys(MainUser.user[1])

    def fill_form_surname(self):            #Заполнить поле "Фамилия"
        self.driver.find_element(*LocatorsPageOrder.FIELD_SURNAME).send_keys(MainUser.user[2])

    def fill_form_address(self):            #Заполнить поле "Адрес"
        self.driver.find_element(*LocatorsPageOrder.FIELD_ADDRESS).send_keys(MainUser.user[3])

    def click_form_metro(self):         #Раскрыть список "Станция метро"
        self.driver.find_element(*LocatorsPageOrder.FIELD_METRO).click()

    def fill_form_metro(self):          #Выбрать "Лубянка" из списка "Станция метро"
        self.driver.find_element(*LocatorsPageOrder.STATION_METRO).click()

    def fill_form_phone(self):          #Заполнить поле "Телефон"
        self.driver.find_element(*LocatorsPageOrder.FIELD_PHONE).send_keys(MainUser.user[4])

    def click_button_next(self):            #Нажать на кнопку "Далее"
        self.driver.find_element(*LocatorsPageOrder.BUTTON_NEXT).click()

    def order_page_name(self):
        self.fill_form_name()
        self.fill_form_surname()
        self.fill_form_address()
        self.click_form_metro()
        self.fill_form_metro()
        self.fill_form_phone()
        self.click_button_next()

    def fill_form_when(self):           #Выбрать дату в поле "Когда привезти самокат"
        self.driver.find_element(*LocatorsPageOrder.FIELD_WHEN).send_keys(MainUser.user[5])

    def click_field_period(self):           #Выбрать поле "Срок аренды"
        self.driver.find_element(*LocatorsPageOrder.FIELD_PERIOD).click()

    def click_field_period_day(self):           #Выбрать "трое суток"
        self.driver.find_element(*LocatorsPageOrder.FIELD_PERIOD_DAY).click()

    def select_color(self):         #Выбрать цвет
        self.driver.find_element(*LocatorsPageOrder.CHECKBOX_COLOR_BLACK).click()

    def fill_form_comment(self):            #Заполнить поле "Комментарий для курьера"
        self.driver.find_element(*LocatorsPageOrder.FIELD_COMMENT).send_keys(MainUser.user[8])

    def click_button_order(self):            #Нажать на кнопку "Далее"
        self.driver.find_element(*LocatorsPageOrder.BUTTON_ORDER).click()

    def order_page_rent(self):
        self.fill_form_when()
        self.click_field_period()
        self.click_field_period_day()
        self.select_color()
        self.fill_form_comment()
        self.click_button_order()

    def click_button_yes(self):
        self.driver.find_element(*LocatorsPageOrder.BUTTON_YES).click()

    def order_scooter_full(self):
        self.order_page_name()
        self.order_page_rent()
        self.click_button_yes()

    def check_order(self):
        return self.driver.find_element(*LocatorsPageOrder.ORDER_CONFIRM).text
