
import pytest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_page_locators import OrderPageLocators


@pytest.fixture()  # драйвер для setup и teardown браузера
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture()
def open_order_url(driver):
    order_url = 'https://qa-scooter.praktikum-services.ru/order'
    driver.get(order_url)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(OrderPageLocators.ORDER_FORM))


@pytest.fixture()
def open_main_page_url(driver):
    main_page_url = 'https://qa-scooter.praktikum-services.ru/'
    driver.get(main_page_url)
