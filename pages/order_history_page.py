from pages.base_page import BasePage
from locators.order_history_locators import OrderHistoryLocators
import allure


class OrderHistoryPage(BasePage):

    @allure.step("Проверка видимости истории заказов")
    def visibility_of_order_history(self):
        self.wait_for_element_visibility(OrderHistoryLocators.ORDER_HISTORY)

    @allure.step("Нажатие на карточку с моим заказом")
    def click_on_my_order_card(self):
        self.click_on_element(OrderHistoryLocators.MY_ORDER_CARD)

    @allure.step("Получение номера моего заказа")
    def get_order_number(self):
        return self.get_element_text(OrderHistoryLocators.MY_ORDER_NUMBER)

    @allure.step("Нажатие на кнопку 'Лента заказов'")
    def click_on_order_feed_button(self):
        self.click_on_element(OrderHistoryLocators.ORDER_FEED_BUTTON)
