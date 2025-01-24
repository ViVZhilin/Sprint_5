from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
import string
from locators import Locators


class TestRedirection:

    link = "https://stellarburgers.nomoreparties.site"

    def test_redirection_by_header_links(self):

        driver = webdriver.Chrome()
        driver.get(self.link)

        driver.find_element(*Locators.PERSONAL_PAGE).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.CONSTRUCTOR_PAGE).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.PERSONAL_PAGE).click()
        driver.find_element(*Locators.LOGO).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()