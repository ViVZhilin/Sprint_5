from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
import string
from locators import Locators

class TestConstructorTab:

    link = "https://stellarburgers.nomoreparties.site"

    def test_constructor_tab(self):

        ScrollScript = "arguments[0].scrollIntoView();"

        driver = webdriver.Chrome()
        driver.get(self.link)

        driver.find_element(*Locators.SOUS_TITLE).click()

        sous_tab = driver.find_element(*Locators.SOUS_TITLE_BLOCK)
        filling_tab = driver.find_element(*Locators.FILLINGS_TITLE_BLOCK)
        buns_tab = driver.find_element(*Locators.BUNS_TITLE_BLOCK)

        driver.implicitly_wait(5)
        driver.execute_script(ScrollScript, sous_tab)
        assert "tab_tab_type_current__2BEPc" in driver.find_element(*Locators.SOUS_TITLE).get_attribute("class")

        driver.execute_script(ScrollScript, filling_tab)
        assert "tab_tab_type_current__2BEPc" in driver.find_element(*Locators.FILLINGS_TITLE).get_attribute("class")

        driver.execute_script(ScrollScript, buns_tab)
        assert "tab_tab_type_current__2BEPc" in driver.find_element(*Locators.BUNS_TITLE).get_attribute("class")

        driver.quit()