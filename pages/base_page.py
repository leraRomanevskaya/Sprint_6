import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver

    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переключить окно')
    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    @allure.step('Проверяем видимость элемента')
    def is_element_visible(self, locator):
        return expected_conditions.visibility_of_element_located(locator)

    @allure.step('Ожидаем, пока элемент не станет видимым')
    def wait_until_visible(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(self.is_element_visible(locator))

    @allure.step('Ожидаем, пока элемент не станет видимым')
    def wait_until_visible(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(self.is_element_visible(locator))

    @allure.step('Ищем элемент на странице')
    def find_view(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Скроллим до элемента')
    def scroll_to_view(self, view):
        self.driver.execute_script("arguments[0].scrollIntoView();", view)
