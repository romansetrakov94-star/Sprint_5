from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/..")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/..")
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]//a")
    BUN_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCE_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLING_TAB = (By.XPATH, "//span[text()='Начинки']")
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span")

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    RESET_LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']")   # на странице /forgot-password

class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")   # на странице регистрации

class PersonalAccountLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    