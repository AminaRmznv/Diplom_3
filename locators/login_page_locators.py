from selenium.webdriver.common.by import By


class LoginPageLocators:
    FORGOT_PASSWORD_LINK = (By.XPATH, '//a[text()="Восстановить пароль"]')
    USERNAME_FIELD = (By.NAME, "name")
    PASSWORD_FIELD = (By.NAME, "Пароль")
    SUBMIT_LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
