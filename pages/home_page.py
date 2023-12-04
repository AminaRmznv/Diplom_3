from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from urls import Urls
import allure

class HomePage(BasePage):

    @allure.step("Переход на главную страницу")
    def go_to_home_page(self):
        self.go_to_page(Urls.home_page_url)

    @allure.step("Клик по кнопке личного кабинета")
    def click_private_account_button(self):
        self.click_on_element(HomePageLocators.PRIVATE_ACCOUNT_TEXT)

    @allure.step("Клик по кнопке конструктора")
    def click_on_constructor_button(self):
        self.click_on_element(HomePageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Проверка видимости секции ингредиентов бургера")
    def visibility_of_burger_ingredients_section(self):
        return self.wait_for_element_visibility(HomePageLocators.BURGER_INGREDIENTS_SECTION)

    @allure.step("Клик по кнопке ленты заказов")
    def click_order_feed(self):
        self.click_on_element(HomePageLocators.ORDER_FEED_BUTTON)

    @allure.step("Клик по ингредиенту")
    def click_on_ingredient(self):
        self.click_on_element(HomePageLocators.INGREDIENT)

    @allure.step("Проверка видимости модального окна с деталями ингредиента")
    def visibility_of_modal_window_with_ingredient_details(self):
        return self.wait_for_element_visibility(HomePageLocators.MODAL_WINDOW_WITH_INGREDIENT_DETAILS)

    @allure.step("Проверка невидимости модального окна с деталями ингредиента")
    def invisibility_of_modal_window_with_ingredient_details(self):
        return self.wait_for_element_invisibility(HomePageLocators.OPENED_MODAL_WINDOW)

    @allure.step("Закрытие модального окна с деталями ингредиента")
    def close_modal_window_with_ingredient_details(self):
        self.click_on_element(HomePageLocators.MODAL_WINDOW_CLOSE_BUTTON)

    @allure.step("Перетаскивание ингредиента в корзину")
    def drag_ingredient_to_basket(self):
        self.drag_and_drop(HomePageLocators.INGREDIENT, HomePageLocators.BURGER_CONSTRUCTOR_BASKET)

    @allure.step("Получение числа счетчика")
    def get_counter_number(self):
        return self.get_element_text(HomePageLocators.COUNTER)

    @allure.step("Клик по кнопке оформления заказа")
    def click_place_order_button(self):
        self.click_on_element(HomePageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Проверка видимости модального окна подготовки заказа")
    def visibility_of_order_prepared_modal_window(self):
        return self.wait_for_element_visibility(HomePageLocators.ORDER_PREPARED_MODAL_WINDOW)

    @allure.step("Получение текста из модального окна с деталями заказа")
    def get_text_from_order_prepared_modal_window(self):
        return self.get_element_text(HomePageLocators.ORDER_PREPARED_MODAL_WINDOW)

    @allure.step("Получение номера заказа из модального окна с деталями заказа")
    def get_order_number_from_order_prepared_modal_window(self):
        return self.get_element_text(HomePageLocators.ORDER_NUMBER_IN_MODAL_WINDOW)
