import allure
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


@allure.title('Проверка открытия формы заказа через первую кнопку "Заказать"')
@allure.description('Проверка открытия формы заказа через первую кнопку "Заказать"')
def test_opened_the_order_form_through_the_main_button(driver, open_main_page_url):
    with allure.step('Нажимаем на кнопку "Заказать"'):
        driver.find_element(*BasePageLocators.ORDER_BUTTON_MAIN).click()
    assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/order'
    assert expected_conditions.visibility_of_element_located(OrderPageLocators.ORDER_FORM)


@allure.title('Проверка открытия формы заказа через вторую кнопку "Заказать"')
@allure.description('Проверка открытия формы заказа вторую первую кнопку "Заказать"')
def test_opened_the_order_form_through_the_middle_button(driver, open_main_page_url):
    with allure.step('Нажимаем на кнопку "Заказать"'):
        button = driver.find_element(*BasePageLocators.ORDER_BUTTON_MIDDLE)
        driver.execute_script("arguments[0].scrollIntoView();", button)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.WANT_SOME_SCOOTERS_QUESTION))
        button.click()
    assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/order'
    assert expected_conditions.visibility_of_element_located(OrderPageLocators.ORDER_FORM)


@allure.title('Проверка успешного заказа')
@allure.description('Проверка успешного заказа')
@pytest.mark.parametrize(
        'name, surname, address, metro_station, telephone_number, delivery_date, rental_period',
        [
            ['Кошечка', 'Крошечка', 'улица Хороших Котиков, дом 3', OrderPageLocators.FIRST_METRO_STATION, '+79991112233', OrderPageLocators.FIRST_DATE, OrderPageLocators.ONE_DAY_RENT],
            ['Котик', 'Спотик', 'проспект Хороших Мальчиков, дом 6', OrderPageLocators.SECOND_METRO_STATION, '+79993334455', OrderPageLocators.SECOND_DATE, OrderPageLocators.TWO_DAY_RENT],
        ]
    )
def test_check_of_successful_order(driver, open_order_url, name, surname, address, metro_station, telephone_number, delivery_date, rental_period):
    with allure.step('Заполняем форму заказа'):
        order = OrderPage(driver)
        order.check_a_successful_order(name, surname, address, metro_station, telephone_number, delivery_date, rental_period)
    assert expected_conditions.visibility_of_element_located(OrderPageLocators.SUCCESSFUL_ORDER_HEADER)
