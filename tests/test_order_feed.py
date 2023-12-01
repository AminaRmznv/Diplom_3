import time

import allure
from pages.home_page import HomePage
from pages.order_feed_page import OrderFeedPage
from pages.order_history_page import OrderHistoryPage
from pages.personal_account import PersonalAccountPage


class TestOrderFeed:

    @allure.title("Тест отображения деталей заказа при клике")
    @allure.description("Тест проверяет отображение всплывающего окна с деталями заказа при клике по карточке заказа")
    def test_click_order_shows_details(self, driver, create_order):
        order_feed = OrderFeedPage(driver)
        order_feed.go_to_order_feed_page()
        order_feed.click_on_order_card()
        assert order_feed.visibility_of_order_details_popup()

    @allure.title("Тест отображения заказов из истории в ленте заказов")
    @allure.description(
        "Тест проверяет, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_orders_from_order_history_displayed(self, driver, create_order):
        home_page = HomePage(driver)
        home_page.click_private_account_button()
        personal_account = PersonalAccountPage(driver)
        personal_account.visibility_of_account_navigation()
        personal_account.click_order_history_button()
        order_history = OrderHistoryPage(driver)
        order_history.visibility_of_order_history()
        order_history_number = order_history.get_order_number()
        order_history.click_on_order_feed_button()
        order_feed = OrderFeedPage(driver)
        order_feed.visibility_of_order_feed()
        assert order_history_number in order_feed.get_all_order_numbers()

    @allure.title("Тест увеличения счётчика выполненных заказов")
    @allure.description("Тест проверяет увеличение счётчика 'Выполнено за всё время' при создании нового заказа")
    def test_completed_orders_counter_increases(self, driver, create_and_delete_user):
        home_page = HomePage(driver)
        home_page.click_order_feed()
        order_feed = OrderFeedPage(driver)
        number_of_all_orders_before = order_feed.get_number_of_all_orders()
        home_page.go_to_home_page()
        home_page.visibility_of_burger_ingredients_section()
        home_page.drag_ingredient_to_basket()
        home_page.click_place_order_button()
        home_page.visibility_of_order_prepared_modal_window()
        order_feed.go_to_order_feed_page()
        number_of_all_orders_after = order_feed.get_number_of_all_orders()
        assert number_of_all_orders_before < number_of_all_orders_after

    @allure.title("Тест увеличения счётчика выполненных заказов за сегодня")
    @allure.description("Тест проверяет увеличение счётчика 'Выполнено за сегодня' при создании нового заказа")
    def test_completed_orders_today_counter_increases(self, driver, create_order):
        home_page = HomePage(driver)
        home_page.click_order_feed()
        order_feed = OrderFeedPage(driver)
        number_of_all_today_orders_before = order_feed.get_number_of_all_orders_for_today()
        home_page.go_to_home_page()
        home_page.visibility_of_burger_ingredients_section()
        home_page.drag_ingredient_to_basket()
        home_page.click_place_order_button()
        home_page.visibility_of_order_prepared_modal_window()
        order_feed.go_to_order_feed_page()
        number_of_all_today_orders_after = order_feed.get_number_of_all_orders_for_today()
        assert number_of_all_today_orders_before < number_of_all_today_orders_after

    @allure.title("Тест появления заказа в разделе 'В работе'")
    @allure.description("Тест проверяет, что после оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_appears_in_progress(self, driver, create_and_delete_user):
        home_page = HomePage(driver)
        home_page.go_to_home_page()
        home_page.visibility_of_burger_ingredients_section()
        home_page.drag_ingredient_to_basket()
        home_page.click_place_order_button()
        home_page.visibility_of_order_prepared_modal_window()
        time.sleep(2)
        my_order_number = home_page.get_order_number_from_order_prepared_modal_window()
        order_feed = OrderFeedPage(driver)
        order_feed.go_to_order_feed_page()
        time.sleep(3)
        assert my_order_number in order_feed.get_number_of_all_pending_orders()
