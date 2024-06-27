import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title("Первый позитивный тест заказа самоката по клику на кнопку 'Заказать в шапке сайта")
    @allure.description("Кликаем 'Заказать в шапке сайта', заполняем форму на странице 'Для кого самокат', "
                        "кликаем по кнопке 'Далее', заполняем данные в форме 'Про аренду', кликаем по кнопке 'Заказать',"
                        "подтверждаем заказ, проверяем открытие окна с подтверждением заказа")
    def test_order_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_button_cookies()
        main_page.click_order_button()
        order_page.order_scooter_full()
        assert order_page.check_order()