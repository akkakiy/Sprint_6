import allure
import pytest
from selenium import webdriver

from data import Urls


@allure.step('Открытие браузера -> Переход на страницу сервиса -> Закрытие браузера')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.MAIN_SCOOTER_PAGE)

    yield driver

    driver.quit()