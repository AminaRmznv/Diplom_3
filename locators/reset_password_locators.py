from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    PASSWORD_RECOVERY_TABLE = (By.CLASS_NAME, 'Auth_login__3hAey')
    NEW_PASSWORD_INPUT = (By.NAME, 'Введите новый пароль')
    VISIBILITY_ICON = (By.XPATH, "//div[@class='input__icon input__icon-action']//*//*")
    FOCUS = (By.CLASS_NAME, 'input_status_active')
