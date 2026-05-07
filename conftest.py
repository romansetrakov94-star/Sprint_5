import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators, LoginPageLocators
from data import generate_name, generate_email, generate_password

BASE_URL = "https://stellarburgers.education-services.ru"

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def registered_user(driver):
    driver.get(f"{BASE_URL}/register")
    name = generate_name()
    email = generate_email()
    password = generate_password()
    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
    return {"email": email, "password": password}
