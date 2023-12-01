import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.personal_account import PersonalAccountPage


class TestHomePage:

    @allure.title("Тест клика по кнопке конструктора")
    @allure.description("Тест проверяет функциональность кнопки конструктора на главной странице")
    def test_click_constructor(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_login_page()
        home_page = HomePage(driver)
        home_page.click_on_constructor_button()
        assert home_page.visibility_of_burger_ingredients_section()

    @allure.title("Тест клика по ленте заказов")
    @allure.description("Тест проверяет переход пользователя по клику на 'Лента заказов'")
    def test_click_order_feed(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_home_page()
        home_page.click_order_feed()
        assert "https://stellarburgers.nomoreparties.site/feed" in home_page.get_current_url()

    @allure.title("Тест отображения деталей ингредиента")
    @allure.description("Тест проверяет появление всплывающего окна с деталями ингредиента при клике на ингредиент")
    def test_ingredient_details_appear(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_home_page()
        home_page.click_on_ingredient()
        assert home_page.visibility_of_modal_window_with_ingredient_details()

    @allure.title("Тест закрытия всплывающего окна")
    @allure.description("Тест проверяет закрытие всплывающего окна с деталями ингредиента по клику на крестик")
    def test_close_popup_by_cross_button(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_home_page()
        home_page.click_on_ingredient()
        home_page.close_modal_window_with_ingredient_details()
        element = home_page.invisibility_of_modal_window_with_ingredient_details()
        assert element

    @allure.title("Тест увеличения счетчика ингредиентов")
    @allure.description("Тест проверяет увеличение счетчика ингредиентов при добавлении ингредиента в заказ")
    def test_increase_ingredient_counter(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_home_page()
        home_page.drag_ingredient_to_basket()
        assert "2" in home_page.get_counter_number()

    @allure.title("Тест оформления заказа пользователем")
    @allure.description("Тест проверяет возможность оформления заказа залогиненным пользователем")
    def test_user_can_place_order(self, driver, create_and_delete_user):
        home_page = HomePage(driver)
        home_page.click_private_account_button()
        personal_account = PersonalAccountPage(driver)
        personal_account.visibility_of_account_navigation()
        home_page.click_on_constructor_button()
        home_page.drag_ingredient_to_basket()
        home_page.click_place_order_button()
        home_page.visibility_of_order_prepared_modal_window()
        assert 'Ваш заказ начали готовить' in home_page.get_text_from_order_prepared_modal_window()
