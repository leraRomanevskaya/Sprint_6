import pytest

from selenium import webdriver

from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture()  # драйвер для setup и teardown браузера
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture()
def order_page(driver):
    driver.get('https://qa-scooter.praktikum-services.ru/order')
    return OrderPage(driver)


@pytest.fixture()
def main_page(driver):
    driver.get('https://qa-scooter.praktikum-services.ru/')
    return MainPage(driver)
