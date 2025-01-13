from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
import string
from locators import Locators

class TestRegistration:

    link = "https://stellarburgers.nomoreparties.site"

    # Прохождение регистрации с невалидным Email
    def test_registration_with_invalid_email(self):

        driver = webdriver.Chrome()
        driver.get(self.link)

        driver.find_element(*Locators.PERSONAL_PAGE).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        driver.find_element(*Locators.NAME_INPUT).send_keys("Viktor")
        invalid_email = 'blablabla'

        driver.find_element(*Locators.EMAIL_INPUT_ACTIVE).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(invalid_email)

        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")

        driver.find_element(*Locators.LOGIN_BUTTON_ON_REGISTRATION_PAGE).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[@class = 'input__error text_type_main-default']")))
        assert driver.find_element(*Locators.EMAIL_ERROR_MESSAGE).text == 'Такой пользователь уже существует'

        driver.quit()


    # Прохождение регистрации с невалидным паролем
    def test_registration_with_invalid_password(self):

        driver = webdriver.Chrome()
        driver.get(self.link)

        driver.find_element(*Locators.PERSONAL_PAGE).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        driver.find_element(*Locators.NAME_INPUT).send_keys("Viktor")
        driver.find_element(*Locators.EMAIL_INPUT_ACTIVE).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("viktor_zhilin_17_000@yandex.ru")

        symbol_range = string.ascii_letters + string.digits + string.punctuation

        invalid_password = ''
        for length in range(5):
            invalid_password += random.choice(symbol_range)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(invalid_password)

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert driver.find_element(*Locators.PASSWORD_ERROR_MESSAGE).text == 'Некорректный пароль'

        driver.quit()


    # Прохождение регистрации с валидными данными
    def test_registration_with_valid_data(self):

        driver = webdriver.Chrome()
        driver.get(self.link)

        driver.find_element(*Locators.PERSONAL_PAGE).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        driver.find_element(*Locators.NAME_INPUT).send_keys("Viktor")

        driver.find_element(*Locators.EMAIL_INPUT_ACTIVE).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("viktor_zhilin_17_000@yandex.ru")

        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")

        driver.find_element(*Locators.LOGIN_BUTTON_ON_REGISTRATION_PAGE).click()

        driver.quit()