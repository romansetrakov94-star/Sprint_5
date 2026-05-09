import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators, LoginPageLocators
from data import generate_email, generate_name, generate_password, generate_short_password
from conftest import BASE_URL
from selenium.webdriver.common.by import By

class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(f"{BASE_URL}/register")
        name = generate_name()
        email = generate_email()
        password = generate_password()
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).is_displayed()

    def test_short_password_error(self, driver):
        driver.get(f"{BASE_URL}/register")
        name = generate_name()
        email = generate_email()
        short_password = generate_short_password()
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(short_password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        error = driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE)
        assert "Некорректный пароль" in error.text
        