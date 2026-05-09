from locators import MainPageLocators, LoginPageLocators, PersonalAccountLocators
from conftest import BASE_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPersonalAccount:

    def test_go_to_personal_account(self, driver, registered_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(registered_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        # Ждём загрузки главной после входа
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
        # Переход в личный кабинет через JavaScript (надёжнее)
        personal_button = driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        driver.execute_script("arguments[0].click();", personal_button)
        # Ждём появления кнопки "Выход"
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(PersonalAccountLocators.LOGOUT_BUTTON))
        assert driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON).is_displayed()

    def test_logout_from_personal_account(self, driver, registered_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(registered_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
        personal_button = driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        driver.execute_script("arguments[0].click();", personal_button)
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(PersonalAccountLocators.LOGOUT_BUTTON))
        logout_button = driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON)
        logout_button.click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).is_displayed()

    def test_go_to_constructor_from_personal_account_by_constructor_button(self, driver, registered_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(registered_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
        personal_button = driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        driver.execute_script("arguments[0].click();", personal_button)
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(PersonalAccountLocators.LOGOUT_BUTTON))
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.BUN_TAB))
        assert driver.find_element(*MainPageLocators.BUN_TAB).is_displayed()

    def test_go_to_constructor_from_personal_account_by_logo(self, driver, registered_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(registered_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
        personal_button = driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        driver.execute_script("arguments[0].click();", personal_button)
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(PersonalAccountLocators.LOGOUT_BUTTON))
        driver.find_element(*MainPageLocators.LOGO).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.BUN_TAB))
        assert driver.find_element(*MainPageLocators.BUN_TAB).is_displayed()
        