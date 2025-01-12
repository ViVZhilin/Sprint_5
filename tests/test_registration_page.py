from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
import string


class TestRegistration:

    # Прохождение регистрации с невалидным Email
    def test_registration_with_invalid_email(self):

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")

        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()


        driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("Viktor")
        invalid_email = 'blablabla'
        driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(invalid_email)
        driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys("123456")

        driver.find_element(By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[@class = 'input__error text_type_main-default']")))
        assert driver.find_element(By.XPATH, ".//div[@class = 'Auth_login__3hAey']/p[@class = 'input__error text_type_main-default']").text == 'Такой пользователь уже существует'

        driver.quit()

    # Прохождение регистрации с невалидным паролем
    def test_registration_with_invalid_password(self):


        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")

        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

        driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("Viktor")
        driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("viktor_zhilin_17_000@yandex.ru")
        symbol_range = string.ascii_letters + string.digits + string.punctuation
        invalid_password = ''
        for length in range(5):
            invalid_password += random.choice(symbol_range)
        driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys(invalid_password)

        driver.find_element(By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        assert driver.find_element(By.XPATH, "//form/fieldset[3]/div/p[@class = 'input__error text_type_main-default']").text == 'Некорректный пароль'

        driver.quit()



    # Прохождение регистрации с валидными данными
    def test_registration_with_valid_data(self):

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")

        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

        driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("Viktor")
        driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("viktor_zhilin_17_000@yandex.ru")
        driver.find_element(By.XPATH, "html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys("123456")

        driver.find_element(By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        driver.quit()