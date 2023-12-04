from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from urls import Urls
import allure


class OrderFeedPage(BasePage):

    @allure.step("Переход на страницу ленты заказов")
    def go_to_order_feed_page(self):
        self.go_to_page(Urls.order_feed_url)

    @allure.step("Клик по карточке заказа")
    def click_on_order_card(self):
        self.click_on_element(OrderFeedLocators.ORDER_CARD)

    @allure.step("Проверка видимости всплывающего окна деталей заказа")
    def visibility_of_order_details_popup(self):
        return self.wait_for_element_visibility(OrderFeedLocators.ORDER_DETAILS_POPUP)

    @allure.step("Проверка видимости раздела 'Заказы'")
    def visibility_of_order_feed(self):
        self.wait_for_element_visibility(OrderFeedLocators.ORDER_FEED)

    @allure.step("Получение всех номеров заказов")
    def get_all_order_numbers(self):
        return self.get_order_numbers(OrderFeedLocators.ALL_ORDERS)

    @allure.step("Получение общего количества всех заказов")
    def get_number_of_all_orders(self):
        return int(self.get_element_text(OrderFeedLocators.ORDERS_NUMBER_FOR_ALL_PERIOD))

    @allure.step("Получение общего количества заказов за сегодня")
    def get_number_of_all_orders_for_today(self):
        return int(self.get_element_text(OrderFeedLocators.ORDERS_FOR_TODAY))

    @allure.step("Получение номера ожидающего заказа")
    def get_number_of_all_pending_orders(self):
        self.wait_for_element_visibility(OrderFeedLocators.ORDER_FEED_LIST_READY)
        return self.get_element_text(OrderFeedLocators.ORDER_FEED_LIST_READY)
