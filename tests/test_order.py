import allure
import pytest
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


class TestOrder:

    @allure.title('Проверка открытия формы заказа через первую кнопку "Заказать"')
    @allure.description('Проверка открытия формы заказа через первую кнопку "Заказать"')
    def test_opened_the_order_form_through_the_main_button(self, main_page):
        main_page.click_the_main_order_button()
        assert main_page.get_current_url() == 'https://qa-scooter.praktikum-services.ru/order'
        order_page = OrderPage(main_page.get_driver())
        assert order_page.is_order_form_visible()

    @allure.title('Проверка открытия формы заказа через вторую кнопку "Заказать"')
    @allure.description('Проверка открытия формы заказа вторую первую кнопку "Заказать"')
    def test_opened_the_order_form_through_the_middle_button(self, main_page):
        main_page.scroll_to_the_middle_order_button()
        main_page.click_the_middle_order_button()
        assert main_page.get_current_url() == 'https://qa-scooter.praktikum-services.ru/order'
        order_page = OrderPage(main_page.get_driver())
        assert order_page.is_order_form_visible()

    @allure.title('Проверка успешного заказа')
    @allure.description('Проверка успешного заказа')
    @pytest.mark.parametrize(
        'name, surname, address, metro_station, telephone_number, delivery_date, rental_period',
        [
            ['Кошечка', 'Крошечка', 'улица Хороших Котиков, дом 3', OrderPageLocators.FIRST_METRO_STATION,
             '+79991112233',
             OrderPageLocators.FIRST_DATE, OrderPageLocators.ONE_DAY_RENT],
            ['Котик', 'Спотик', 'проспект Хороших Мальчиков, дом 6', OrderPageLocators.SECOND_METRO_STATION,
             '+79993334455',
             OrderPageLocators.SECOND_DATE, OrderPageLocators.TWO_DAY_RENT],
        ]
    )
    def test_check_of_successful_order(
            self,
            order_page,
            name,
            surname,
            address,
            metro_station,
            telephone_number,
            delivery_date,
            rental_period,
    ):
        order_page.check_a_successful_order(name, surname, address, metro_station, telephone_number, delivery_date, rental_period)
        assert order_page.is_successful_order_header_visible()
