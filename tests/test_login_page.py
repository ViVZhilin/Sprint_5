from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
import string



class TestLogin:
    valid_email = "viktor_zhilin_17_000@yandex.ru"
    valid_password = '123456'

    # 1. Вход по кнопке "Войти в аккаунт" на главной странице
    def test_login_from_main_page(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")

        driver.find_element(By.XPATH, ".//div[@class = 'BurgerConstructor_basket__container__2fUl3 mt-10']/button").click()
        driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(self.valid_email)
        driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(self.valid_password)
        driver.find_element(By.XPATH, ".//form[@class = 'Auth_form__3qKeq mb-20']/button").click()

        driver.find_element(By.XPATH, ".//nav[@class = 'AppHeader_header__nav__g5hnF']/a/p").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@class = 'input pr-6 pl-6 input_type_text input_size_default input_status_disabled']")))
        assert driver.find_element(By.XPATH, ".//ul[@class = 'Profile_profileList__3vTor']/li[2]/div/div/input").get_attribute('value') == self.valid_email

        driver.quit()

    # 2. Вход через кнопку "Личный кабинет"
    def test_login_from_personal_account(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")

        driver.find_element(By.XPATH, ".//nav[@class = 'AppHeader_header__nav__g5hnF']/a/p").click()
        driver.find_element(By.XPATH, ".//form[@class = 'Auth_form__3qKeq mb-20']/fieldset[1]/div/div/input").send_keys(self.valid_email)
        driver.find_element(By.XPATH, ".//form[@class = 'Auth_form__3qKeq mb-20']/fieldset[2]/div/div/input").send_keys(self.valid_password)
        driver.find_element(By.XPATH, ".//form[@class = 'Auth_form__3qKeq mb-20']/button").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//nav[@class = 'AppHeader_header__nav__g5hnF']/a/p")))

        driver.find_element(By.XPATH, ".//nav[@class = 'AppHeader_header__nav__g5hnF']/a/p").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@class = 'input pr-6 pl-6 input_type_text input_size_default input_status_disabled']")))
        assert driver.find_element(By.XPATH, ".//ul[@class = 'Profile_profileList__3vTor']/li[2]/div/div/input").get_attribute('value') == self.valid_email

        driver.quit()

    # 3. Вход через кнопку на форме регистрации
    def test_login_from_registration_page(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")

        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

        driver.find_element(By.LINK_TEXT, "Войти").click()
        driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(self.valid_email)
        driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(self.valid_password)
        driver.find_element(By.XPATH, ".//form[@class = 'Auth_form__3qKeq mb-20']/button").click()

        driver.find_element(By.XPATH, ".//nav[@class = 'AppHeader_header__nav__g5hnF']/a/p").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@class = 'input pr-6 pl-6 input_type_text input_size_default input_status_disabled']")))
        assert driver.find_element(By.XPATH, ".//ul[@class = 'Profile_profileList__3vTor']/li[2]/div/div/input").get_attribute('value') == self.valid_email

        driver.quit()

    # 4. Вход по кнопке "Восстановить пароль"
    def test_login_from_password_recover_page(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")

        driver.find_element(By.XPATH, ".//div[@class = 'BurgerConstructor_basket__container__2fUl3 mt-10']/button").click()
        driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()
        driver.find_element(By.LINK_TEXT, "Войти").click()

        driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(self.valid_email)
        driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(self.valid_password)
        driver.find_element(By.XPATH, ".//form[@class = 'Auth_form__3qKeq mb-20']/button").click()

        driver.find_element(By.XPATH, ".//nav[@class = 'AppHeader_header__nav__g5hnF']/a/p").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@class = 'input pr-6 pl-6 input_type_text input_size_default input_status_disabled']")))
        assert driver.find_element(By.XPATH, ".//ul[@class = 'Profile_profileList__3vTor']/li[2]/div/div/input").get_attribute('value') == self.valid_email

        driver.quit()