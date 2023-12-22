from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Класс с локаторами на странице заказа."""
    ORDER_FORM = (By.CLASS_NAME, 'Order_Content__bmtHS')
    ORDER_BUTTON_MIDDLE = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    FORM_NAME = (By.XPATH, './/input[@placeholder="* Имя"]')
    FORM_SURNAME = (By.XPATH, './/input[@placeholder="* Фамилия"]')
    ADDRESS = (By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATIONS = (By.XPATH, './/div[@class="select-search"]')
    FIRST_METRO_STATION = (By.XPATH, './/li[1]')
    SECOND_METRO_STATION = (By.XPATH, './/li[2]')
    TELEPHONE_NUMBER = (By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, './/button[starts-with(text(),"Далее")]')
    ABOUT_RENT_HEADER = (By.CLASS_NAME, 'Order_Header__BZXOb')
    CALENDAR = (By.XPATH, './/input[@placeholder="* Когда привезти самокат"]')
    FIRST_DATE = (By.XPATH, '.// div[starts-with(text(), "19")]')
    SECOND_DATE = (By.XPATH, '.// div[starts-with(text(), "20")]')
    THE_RENTAL_PERIOD = (By.XPATH, './/div[contains(text(), "Срок аренды")]')
    ONE_DAY_RENT = (By.XPATH, '.// div[starts-with(text(), "сутки")]')
    TWO_DAY_RENT = (By.XPATH, '.// div[starts-with(text(), "двое суток")]')
    ACCEPT_BUTTON = (By.XPATH, './/button[starts-with(text(), "Да")]')
    SUCCESSFUL_ORDER_HEADER = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
