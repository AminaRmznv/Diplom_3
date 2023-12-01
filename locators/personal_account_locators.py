from selenium.webdriver.common.by import By


class PersonalAccountLocators:

    ACCOUNT_NAV = (By.XPATH, "//nav[contains(@class, 'Account_nav')]")
    ORDER_HISTORY_BUTTON = (By.XPATH, '//a[text()="История заказов"]')
    EXIT_FROM_PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Выход']")
