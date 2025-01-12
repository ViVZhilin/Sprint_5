from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
import string


class TestRedirection:

    def test_redirection_by_header_links(self):

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")

        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        WebDriverWait(driver, 3)

        driver.find_element(By.LINK_TEXT, "Конструктор").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        WebDriverWait(driver, 3)

        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        driver.find_element(By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()