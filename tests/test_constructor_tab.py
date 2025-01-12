from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
import string

class TestConstructorTab:

    def test_constructor_tab(self):

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")

        driver.find_element(By.XPATH, "//div/span[text()='Соусы']").click()

        sous_tab = driver.find_element(By.XPATH, "//h2[text()='Соусы']")
        filling_tab = driver.find_element(By.XPATH, "//h2[text()='Начинки']")
        buns_tab = driver.find_element(By.XPATH, "//h2[text()='Булки']")

        driver.implicitly_wait(5)
        driver.execute_script("arguments[0].scrollIntoView();", sous_tab)
        assert "tab_tab_type_current__2BEPc" in driver.find_element(By.XPATH, "//div/span[text()='Соусы']/parent::div").get_attribute("class")

        driver.execute_script("arguments[0].scrollIntoView();", filling_tab)
        assert "tab_tab_type_current__2BEPc" in driver.find_element(By.XPATH, "//div/span[text()='Начинки']/parent::div").get_attribute("class")

        driver.execute_script("arguments[0].scrollIntoView();", buns_tab)
        assert "tab_tab_type_current__2BEPc" in driver.find_element(By.XPATH, "//div/span[text()='Булки']/parent::div").get_attribute("class")

        driver.quit()