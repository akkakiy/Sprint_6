from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from locators.locators_main_page import LocatorsMainPage



class MainPage:

    def __init__(self, driver):
        self.driver = driver

    #Проверить текущий url
    def check_url(self):
        return self.driver.current_url

    def click_button_cookies(self):
        self.driver.find_element(*LocatorsMainPage.ACCEPT_COOKIES).click()

    #Проверить наличие кнопки "Заказать"
    def check_order_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(LocatorsMainPage.ORDER_BUTTON))

    #Нажать на кнопку "Заказать"
    def click_order_button(self):
        self.driver.find_element(*LocatorsMainPage.ORDER_BUTTON).click()






