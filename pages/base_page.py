import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver

    @allure.step('Проверяем видимость элемента')
    def is_element_visible(self, locator):
        return expected_conditions.visibility_of_element_located(locator)

    @allure.step('Ожидаем, пока элемент не станет видимым')
    def wait_until_visible(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(self.is_element_visible(locator))

    @allure.step('Ищем элемент на странице')
    def find_view(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Скроллим до элемента')
    def scroll_to_view(self, view):
        self.driver.execute_script("arguments[0].scrollIntoView();", view)

    @allure.step('Клик на логотип Скутера')
    def click_the_scooter_logo(self):
        self.find_view(BasePageLocators.SCOOTER_LOGO).click()

    @allure.step('Клик на логотип Яндекса')
    def click_the_yandex_logo(self):
        self.find_view(BasePageLocators.YANDEX_LOGO).click()

    @allure.step('Клик на кнопку "Заказать" в хедере')
    def click_the_main_order_button(self):
        self.find_view(BasePageLocators.ORDER_BUTTON_MAIN).click()

    @allure.step('Клик на кнопку "Заказать" на странице')
    def click_the_middle_order_button(self):
        self.find_view(BasePageLocators.ORDER_BUTTON_MIDDLE).click()

    @allure.step('Скроллим до кнопки "Заказать" на странице')
    def scroll_to_the_middle_order_button(self):
        middle_order_button = self.find_view(BasePageLocators.ORDER_BUTTON_MIDDLE)
        self.scroll_to_view(middle_order_button)
        self.wait_until_visible(5, BasePageLocators.ORDER_BUTTON_MIDDLE)
