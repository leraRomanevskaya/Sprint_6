from selenium.webdriver.common.by import By


class BasePageLocators:
    """Класс с общими локаторами."""
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    DZEN_LOGO = (By.XPATH, './/a[@data-testid="logo"]')
    ORDER_BUTTON_MAIN = (By.XPATH, './/button[@class="Button_Button__ra12g"]')
    ORDER_BUTTON_MIDDLE = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
