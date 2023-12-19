from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        self.driver.find_element(*OrderPageLocators.FORM_NAME).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.FORM_SURNAME).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.ADDRESS).send_keys(address)

    def set_telephone_number(self, telephone_number):
        self.driver.find_element(*OrderPageLocators.TELEPHONE_NUMBER).send_keys(telephone_number)

    def click_metro_station_field(self):
        self.driver.find_element(*OrderPageLocators.METRO_STATIONS).click()

    def choosing_a_metro_station(self, metro_station):
        self.driver.find_element(*metro_station).click()

    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    def click_the_calendar_field(self):
        self.driver.find_element(*OrderPageLocators.CALENDAR).click()

    def choosing_delivery_date(self, delivery_date):
        self.driver.find_element(*delivery_date).click()

    def click_the_rental_period_field(self):
        self.driver.find_element(*OrderPageLocators.THE_RENTAL_PERIOD).click()

    def choosing_rental_period(self, rental_period):
        self.driver.find_element(*rental_period).click()

    def click_the_order_button(self):
        self.driver.find_element(*BasePageLocators.ORDER_BUTTON_MIDDLE).click()

    def click_the_accept_button(self):
        self.driver.find_element(*OrderPageLocators.ACCEPT_BUTTON).click()

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
        self.click_the_order_button()
        self.click_the_accept_button()

