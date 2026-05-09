from locators import MainPageLocators
from conftest import BASE_URL
import pytest

class TestConstructor:
    @pytest.mark.parametrize("tab_locator, expected_text", [
        (MainPageLocators.BUN_TAB, "Булки"),
        (MainPageLocators.SAUCE_TAB, "Соусы"),
        (MainPageLocators.FILLING_TAB, "Начинки"),
    ])
    def test_switch_to_tab(self, driver, tab_locator, expected_text):
        driver.get(BASE_URL)
        tab = driver.find_element(*tab_locator)
        driver.execute_script("arguments[0].click();", tab)
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        assert expected_text in active_tab
                     