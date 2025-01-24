from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
import string
from locators import Locators



class TestLogin:
    valid_email = "viktor_zhilin_17_000@yandex.ru"
    valid_password = '123456'
    link = "https://stellarburgers.nomoreparties.site"

    # 1. Вход по кнопке "Войти в аккаунт" на главной странице
    def test_login_from_main_page(self):
        driver = webdriver.Chrome()
        driver.get(self.link)

        driver.find_element(*Locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()

        driver.find_element(*Locators.EMAIL_INPUT_ACTIVE).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(self.valid_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(self.valid_password)
        driver.find_element(*Locators.LOGIN_BUTTON_ON_LOGIN_PAGE).click()

        driver.find_element(*Locators.PERSONAL_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PERSONAL_EMAIL_FIELD))
        assert driver.find_element(*Locators.PERSONAL_EMAIL_DATA).get_attribute('value') == self.valid_email

        driver.quit()

    # 2. Вход через кнопку "Личный кабинет"
    def test_login_from_personal_account(self):
        driver = webdriver.Chrome()
        driver.get(self.link)

        driver.find_element(*Locators.PERSONAL_PAGE).click()
        driver.find_element(*Locators.EMAIL_INPUT_ACTIVE).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(self.valid_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(self.valid_password)
        driver.find_element(*Locators.LOGIN_BUTTON_ON_LOGIN_PAGE).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//nav[@class = 'AppHeader_header__nav__g5hnF']/a/p")))

        driver.find_element(*Locators.PERSONAL_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PERSONAL_EMAIL_FIELD))
        assert driver.find_element(*Locators.PERSONAL_EMAIL_DATA).get_attribute('value') == self.valid_email

        driver.quit()

    # 3. Вход через кнопку на форме регистрации
    def test_login_from_registration_page(self):
        driver = webdriver.Chrome()
        driver.get(self.link)

        driver.find_element(*Locators.PERSONAL_PAGE).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT_ACTIVE).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(self.valid_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(self.valid_password)
        driver.find_element(*Locators.LOGIN_BUTTON_ON_LOGIN_PAGE).click()

        driver.find_element(*Locators.PERSONAL_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PERSONAL_EMAIL_FIELD))
        assert driver.find_element(*Locators.PERSONAL_EMAIL_DATA).get_attribute('value') == self.valid_email

        driver.quit()

    # 4. Вход по кнопке "Восстановить пароль"
    def test_login_from_password_recover_page(self):
        driver = webdriver.Chrome()
        driver.get(self.link)

        driver.find_element(*Locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*Locators.PASSWORD_RECOVER_BUTTON).click()
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        driver.find_element(*Locators.EMAIL_INPUT_ACTIVE).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(self.valid_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(self.valid_password)
        driver.find_element(*Locators.LOGIN_BUTTON_ON_LOGIN_PAGE).click()

        driver.find_element(*Locators.PERSONAL_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PERSONAL_EMAIL_FIELD))
        assert driver.find_element(*Locators.PERSONAL_EMAIL_DATA).get_attribute('value') == self.valid_email

        driver.quit()