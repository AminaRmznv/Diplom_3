from selenium.webdriver.common.by import By

class OrderFeedLocators:
    ORDER_CARD = (By.XPATH, '//ul[@class="OrderFeed_list__OLh59"]/li[1]')
    ORDER_DETAILS_POPUP = (By.CLASS_NAME, 'Modal_modal_opened__3ISw4')
    ALL_ORDERS = (By.XPATH, '//ul[@class="OrderFeed_list__OLh59"]/li//p[1]')
    ORDER_FEED = (By.CLASS_NAME, 'OrderFeed_orderFeed__2RO_j')
    ORDERS_NUMBER_FOR_ALL_PERIOD = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p[1]")
    ORDERS_FOR_TODAY = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p[1]")
    ORDER_FEED_LIST_READY = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li[contains(@class, 'text_type_digits-default')]")
