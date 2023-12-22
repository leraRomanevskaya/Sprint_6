import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик на кнопку "Заказать" в хедере')
    def click_the_main_order_button(self):
        self.find_view(MainPageLocators.ORDER_BUTTON_MAIN).click()

    @allure.step('Клик на кнопку "Заказать" на странице')
    def click_the_middle_order_button(self):
        self.find_view(MainPageLocators.ORDER_BUTTON_MIDDLE).click()

    @allure.step('Скроллим до кнопки "Заказать" на странице')
    def scroll_to_the_middle_order_button(self):
        middle_order_button = self.find_view(MainPageLocators.ORDER_BUTTON_MIDDLE)
        self.scroll_to_view(middle_order_button)
        self.wait_until_visible(5, MainPageLocators.ORDER_BUTTON_MIDDLE)
