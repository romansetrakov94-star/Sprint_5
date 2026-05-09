from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators
from conftest import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:

    def test_login_from_main_page(self, driver, registered_user):
        driver.get(BASE_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(registered_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        order_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после входа"

    def test_login_from_personal_account(self, driver, registered_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(registered_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        order_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после входа"

    def test_login_from_registration_form(self, driver, registered_user):
        driver.get(f"{BASE_URL}/register")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(registered_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        order_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после входа"

    def test_login_from_forgot_password(self, driver, registered_user):
        driver.get(f"{BASE_URL}/forgot-password")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.RESET_LOGIN_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(registered_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        order_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после входа"
        