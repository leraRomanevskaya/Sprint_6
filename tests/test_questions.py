import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators
from testdata import HOW_MUCH_DOES_IT_COST_ANSWER_TEXT, WANT_SOME_SCOOTERS_ANSWER, HOW_TIME_IS_CALCULATED_ANSWER_TEXT, \
    CAN_I_ORDER_A_SCOOTER_TODAY_ANSWER_TEXT, EXTENDED_THE_ORDER_ANSWER_TEXT, CHARGING_WITH_A_SCOOTER_ANSWER_TEXT, \
    CANCEL_THE_ORDER_ANSWER_TEXT, LIFE_BEYOND_THE_MKAD_ANSWER_TEXT


@allure.title('Проверка соответствия текста ответа для первого вопроса в выпадающем списке')
@allure.description('Проверка соответствия текста ответа для первого вопроса в выпадающем списке')
def test_how_much_does_it_сost_question(driver, open_main_page_url):
    with allure.step('Находим на странице первый вопрос'):
        question = driver.find_element(*MainPageLocators.HOW_MUCH_DOES_IT_COST_QUESTION)
        driver.execute_script("arguments[0].scrollIntoView();", question)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.WANT_SOME_SCOOTERS_QUESTION))
    with allure.step('Раскрываем вопрос'):
        question.click()
    assert driver.find_element(*MainPageLocators.HOW_MUCH_DOES_IT_COST_ANSWER).text == HOW_MUCH_DOES_IT_COST_ANSWER_TEXT


@allure.title('Проверка соответствия текста ответа для второго вопроса в выпадающем списке')
@allure.description('Проверка соответствия текста ответа для второго вопроса в выпадающем списке')
def test_want_some_scooters_question(driver, open_main_page_url):
    with allure.step('Находим на странице второй вопрос'):
        question = driver.find_element(*MainPageLocators.WANT_SOME_SCOOTERS_QUESTION)
        driver.execute_script("arguments[0].scrollIntoView();", question)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.WANT_SOME_SCOOTERS_QUESTION))
    with allure.step('Раскрываем вопрос'):
        question.click()
    assert driver.find_element(*MainPageLocators.WANT_SOME_SCOOTERS_ANSWER).text == WANT_SOME_SCOOTERS_ANSWER


@allure.title('Проверка соответствия текста ответа для третьего вопроса в выпадающем списке')
@allure.description('Проверка соответствия текста ответа для третьего вопроса в выпадающем списке')
def test_how_time_is_calculated_question(driver, open_main_page_url):
    with allure.step('Находим на странице третий вопрос'):
        question = driver.find_element(*MainPageLocators.HOW_TIME_IS_CALCULATED_QUESTION)
        driver.execute_script("arguments[0].scrollIntoView();", question)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.HOW_TIME_IS_CALCULATED_QUESTION))
    with allure.step('Раскрываем вопрос'):
        question.click()
    assert driver.find_element(*MainPageLocators.HOW_TIME_IS_CALCULATED_ANSWER).text == HOW_TIME_IS_CALCULATED_ANSWER_TEXT


@allure.title('Проверка соответствия текста ответа для четвёртого вопроса в выпадающем списке')
@allure.description('Проверка соответствия текста ответа для четвёртого вопроса в выпадающем списке')
def test_сan_i_order_a_scooter_today_question(driver, open_main_page_url):
    with allure.step('Находим на странице четвёртый вопрос'):
        question = driver.find_element(*MainPageLocators.CAN_I_ORDER_A_SCOOTER_TODAY_QUESTION)
        driver.execute_script("arguments[0].scrollIntoView();", question)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.CAN_I_ORDER_A_SCOOTER_TODAY_QUESTION))
    with allure.step('Раскрываем вопрос'):
        question.click()
    assert driver.find_element(*MainPageLocators.CAN_I_ORDER_A_SCOOTER_TODAY_ANSWER).text == CAN_I_ORDER_A_SCOOTER_TODAY_ANSWER_TEXT


@allure.title('Проверка соответствия текста ответа для пятого вопроса в выпадающем списке')
@allure.description('Проверка соответствия текста ответа для пятого вопроса в выпадающем списке')
def test_extend_the_order_question(driver, open_main_page_url):
    with allure.step('Находим на странице пятый вопрос'):
        question = driver.find_element(*MainPageLocators.EXTENDED_THE_ORDER_QUESTION)
        driver.execute_script("arguments[0].scrollIntoView();", question)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.EXTENDED_THE_ORDER_QUESTION))
    with allure.step('Раскрываем вопрос'):
        question.click()
    assert driver.find_element(*MainPageLocators.EXTENDED_THE_ORDER_ANSWER).text == EXTENDED_THE_ORDER_ANSWER_TEXT


@allure.title('Проверка соответствия текста ответа для шестого вопроса в выпадающем списке')
@allure.description('Проверка соответствия текста ответа для шестого вопроса в выпадающем списке')
def test_charging_with_a_scooter_question(driver, open_main_page_url):
    with allure.step('Находим на странице шестой вопрос'):
        question = driver.find_element(*MainPageLocators.CHARGING_WITH_A_SCOOTER_QUESTION)
        driver.execute_script("arguments[0].scrollIntoView();", question)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.CHARGING_WITH_A_SCOOTER_QUESTION))
    with allure.step('Раскрываем вопрос'):
        question.click()
    assert driver.find_element(*MainPageLocators.CHARGING_WITH_A_SCOOTER_ANSWER).text == CHARGING_WITH_A_SCOOTER_ANSWER_TEXT


@allure.title('Проверка соответствия текста ответа для седьмого вопроса в выпадающем списке')
@allure.description('Проверка соответствия текста ответа для седьмого вопроса в выпадающем списке')
def test_cancel_the_order_question(driver, open_main_page_url):
    with allure.step('Находим на странице седьмой вопрос'):
        question = driver.find_element(*MainPageLocators.CANCEL_THE_ORDER_QUESTION)
        driver.execute_script("arguments[0].scrollIntoView();", question)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.CANCEL_THE_ORDER_QUESTION))
    with allure.step('Раскрываем вопрос'):
        question.click()
    assert driver.find_element(*MainPageLocators.CANCEL_THE_ORDER_ANSWER).text == CANCEL_THE_ORDER_ANSWER_TEXT


@allure.title('Проверка соответствия текста ответа для восьмого вопроса в выпадающем списке')
@allure.description('Проверка соответствия текста ответа для восьмого вопроса в выпадающем списке')
def test_life_beyond_the_MKAD_question(driver, open_main_page_url):
    with allure.step('Находим на странице седьмой вопрос'):
        question = driver.find_element(*MainPageLocators.LIFE_BEYOND_THE_MKAD_QUESTION)
        driver.execute_script("arguments[0].scrollIntoView();", question)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.LIFE_BEYOND_THE_MKAD_QUESTION))
    with allure.step('Раскрываем вопрос'):
        question.click()
    assert driver.find_element(*MainPageLocators.LIFE_BEYOND_THE_MKAD_ANSWER).text == LIFE_BEYOND_THE_MKAD_ANSWER_TEXT
