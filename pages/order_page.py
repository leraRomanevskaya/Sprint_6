import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Вводим имя в поле "Имя"')
    def set_name(self, name):
        self.find_view(OrderPageLocators.FORM_NAME).send_keys(name)

    @allure.step('Вводим фамилию в поле "Фамилия"')
    def set_surname(self, surname):
        self.find_view(OrderPageLocators.FORM_SURNAME).send_keys(surname)

    @allure.step('Вводим адрес в поле "Адрес"')
    def set_address(self, address):
        self.find_view(OrderPageLocators.ADDRESS).send_keys(address)

    @allure.step('Вводим номер в поле "Телефон"')
    def set_telephone_number(self, telephone_number):
        self.find_view(OrderPageLocators.TELEPHONE_NUMBER).send_keys(telephone_number)

    @allure.step('Раскрываем выпадающий список со станциями метро')
    def click_metro_station_field(self):
        self.find_view(OrderPageLocators.METRO_STATIONS).click()

    @allure.step('Выбираем станцию метро в выпадающем списке')
    def choosing_a_metro_station(self, metro_station):
        self.find_view(metro_station).click()

    @allure.step('Нажимаем на кнопку "Далее"')
    def click_next_button(self):
        self.find_view(OrderPageLocators.NEXT_BUTTON).click()

    @allure.step('Нажимаем на поле "Календарь"')
    def click_the_calendar_field(self):
        self.find_view(OrderPageLocators.CALENDAR).click()

    @allure.step('Выбираем день в календаре')
    def choosing_delivery_date(self, delivery_date):
        self.find_view(delivery_date).click()

    @allure.step('Нажимаем на поле "Срок аренды"')
    def click_the_rental_period_field(self):
        self.find_view(OrderPageLocators.THE_RENTAL_PERIOD).click()

    @allure.step('Выбираем срок аренды')
    def choosing_rental_period(self, rental_period):
        self.find_view(rental_period).click()

    @allure.step('Нажимаем на кнопку "Да" в форме подтверждения заказа')
    def click_the_accept_button(self):
        self.find_view(OrderPageLocators.ACCEPT_BUTTON).click()

    @allure.step('Клик на кнопку "Заказать" на странице')
    def click_the_middle_order_button(self):
        self.find_view(OrderPageLocators.ORDER_BUTTON_MIDDLE).click()

    @allure.step('Клик на логотип Скутера')
    def click_the_scooter_logo(self):
        self.find_view(OrderPageLocators.SCOOTER_LOGO).click()

    @allure.step('Клик на логотип Яндекса')
    def click_the_yandex_logo(self):
        self.find_view(OrderPageLocators.YANDEX_LOGO).click()

    @allure.step('Проверяем, что форма заказа видима')
    def is_order_form_visible(self):
        return self.is_element_visible(OrderPageLocators.ORDER_FORM)

    @allure.step('Проверяем видимость хедера в форме об успешно созданном заказе')
    def is_successful_order_header_visible(self):
        return self.is_element_visible(OrderPageLocators.SUCCESSFUL_ORDER_HEADER)

    @allure.step('Проверка успешно созданного заказа')
    def check_a_successful_order(self, name, surname, address, metro_station, telephone_number, delivery_date, rental_period):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.click_metro_station_field()
        self.choosing_a_metro_station(metro_station)
        self.set_telephone_number(telephone_number)
        self.click_next_button()
        self.click_the_calendar_field()
        self.choosing_delivery_date(delivery_date)
        self.click_the_rental_period_field()
        self.choosing_rental_period(rental_period)
        self.click_the_middle_order_button()
        self.click_the_accept_button()
