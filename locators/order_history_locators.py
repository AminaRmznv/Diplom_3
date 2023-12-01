from selenium.webdriver.common.by import By


class OrderHistoryLocators:
    ORDER_HISTORY = (By.CLASS_NAME, 'OrderHistory_orderHistory__qy1VB')
    MY_ORDER_CARD = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList__')]/li")
    MY_ORDER_NUMBER = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList__')]/li//p")
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]')
