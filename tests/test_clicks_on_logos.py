import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocators


class TestClickedOnLogos:

    @allure.title('Проверка открытия главной страницы по клику на лого Самоката')
    @allure.description('Проверка открытия главной страницы по клику на лого Самоката')
    def test_clicked_on_the_scooter_logo(self, order_page):
        order_page.click_the_scooter_logo()
        assert order_page.get_driver().current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка открытия Дзена по клику на лого Яндекса')
    @allure.description('Проверка открытия Дзена по клику на лого Яндекса')
    def test_clicked_on_the_yandex_logo(self, order_page):
        order_page.click_the_yandex_logo()
        # Дзен – не является частью сервиса, соответственно POM в этом случае не применяю
        with allure.step('Переходим на открывшуюся вкладку с Дзеном'):
            driver = order_page.get_driver()
            driver.switch_to.window(driver.window_handles[1])
            WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(BasePageLocators.DZEN_LOGO))
        assert expected_conditions.visibility_of_element_located(BasePageLocators.DZEN_LOGO)
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'
