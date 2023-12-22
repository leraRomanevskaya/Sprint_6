import allure

from locators.dzen_page_locator import DzenPageLocators


class TestClickedOnLogos:

    @allure.title('Проверка открытия главной страницы по клику на лого Самоката')
    @allure.description('Проверка открытия главной страницы по клику на лого Самоката')
    def test_clicked_on_the_scooter_logo(self, order_page):
        order_page.click_the_scooter_logo()
        assert order_page.get_current_url() == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка открытия Дзена по клику на лого Яндекса')
    @allure.description('Проверка открытия Дзена по клику на лого Яндекса')
    def test_clicked_on_the_yandex_logo(self, order_page):
        order_page.click_the_yandex_logo()
        order_page.switch_to_window(1)
        order_page.wait_until_visible(5, DzenPageLocators.DZEN_LOGO)
        assert order_page.get_current_url() == 'https://dzen.ru/?yredirect=true'
