from locators import MainPageLocators
from conftest import BASE_URL
from selenium.webdriver.common.by import By

class TestConstructor:

    def test_switch_to_buns_tab(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.SAUCE_TAB).click()
        driver.find_element(*MainPageLocators.BUN_TAB).click()
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        assert "Булки" in active_tab

    def test_switch_to_sauces_tab(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.SAUCE_TAB).click()
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        assert "Соусы" in active_tab

    def test_switch_to_fillings_tab(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.FILLING_TAB).click()
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        assert "Начинки" in active_tab
        