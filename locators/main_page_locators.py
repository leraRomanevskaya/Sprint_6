from selenium.webdriver.common.by import By


class MainPageLocators:
    """Класс с локаторами главной страницы."""
    LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    HOW_MUCH_DOES_IT_COST_QUESTION = (By.XPATH, './/div[@id="accordion__heading-0"]')
    HOW_MUCH_DOES_IT_COST_ANSWER = (By.XPATH, './/div/p[starts-with(text(),"Сутки")]')
    WANT_SOME_SCOOTERS_QUESTION = (By.XPATH, './/div[@id="accordion__heading-1"]')
    WANT_SOME_SCOOTERS_ANSWER = (By.XPATH, './/div/p[starts-with(text(),"Пока что у нас так")]')
    HOW_TIME_IS_CALCULATED_QUESTION = (By.XPATH, './/div[@id="accordion__heading-2"]')
    HOW_TIME_IS_CALCULATED_ANSWER = (By.XPATH, './/div/p[starts-with(text(),"Допустим")]')
    CAN_I_ORDER_A_SCOOTER_TODAY_QUESTION = (By.XPATH, './/div[@id="accordion__heading-3"]')
    CAN_I_ORDER_A_SCOOTER_TODAY_ANSWER = (By.XPATH, './/div/p[starts-with(text(),"Только")]')
    EXTENDED_THE_ORDER_QUESTION = (By.XPATH, './/div[@id="accordion__heading-4"]')
    EXTENDED_THE_ORDER_ANSWER = (By.XPATH, './/div/p[starts-with(text(),"Пока что нет")]')
    CHARGING_WITH_A_SCOOTER_QUESTION = (By.XPATH, './/div[@id="accordion__heading-5"]')
    CHARGING_WITH_A_SCOOTER_ANSWER = (By.XPATH, './/div/p[starts-with(text(),"Самокат приезжает")]')
    CANCEL_THE_ORDER_QUESTION = (By.XPATH, './/div[@id="accordion__heading-6"]')
    CANCEL_THE_ORDER_ANSWER = (By.XPATH, './/div/p[starts-with(text(),"Да, пока самокат")]')
    LIFE_BEYOND_THE_MKAD_QUESTION = (By.XPATH, './/div[@id="accordion__heading-7"]')
    LIFE_BEYOND_THE_MKAD_ANSWER = (By.XPATH, './/div/p[starts-with(text(),"Да, обязательно")]')
