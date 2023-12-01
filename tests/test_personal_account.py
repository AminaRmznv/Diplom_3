import allure
from pages.home_page import HomePage
from pages.personal_account import PersonalAccountPage
from pages.order_history_page import OrderHistoryPage
from pages.login_page import LoginPage


class TestPersonalAccount:

    @allure.title("Тест перехода в личный кабинет")
    @allure.description("Тест проверяет переход пользователя в личный кабинет по клику на соответствующую кнопку")
    def test_go_to_personal_account(self, driver, create_and_delete_user):
        home_page = HomePage(driver)
        home_page.click_private_account_button()
        personal_account = PersonalAccountPage(driver)
        assert personal_account.visibility_of_account_navigation()

    @allure.title("Тест перехода в историю заказов")
    @allure.description("Тест проверяет переход пользователя в раздел 'История заказов' в личном кабинете")
    def test_go_to_order_history(self, driver, create_and_delete_user):
        home_page = HomePage(driver)
        home_page.click_private_account_button()
        personal_account = PersonalAccountPage(driver)
        personal_account.visibility_of_account_navigation()
        personal_account.click_order_history_button()
        order_history = OrderHistoryPage(driver)
        assert 'https://stellarburgers.nomoreparties.site/account/order-history' == order_history.check_current_order_history_url()

    @allure.title("Тест выхода из личного кабинета")
    @allure.description("Тест проверяет функциональность кнопки выхода из личного кабинета")
    def test_logout_from_account(self, driver, create_and_delete_user):
        home_page = HomePage(driver)
        home_page.click_private_account_button()
        personal_account = PersonalAccountPage(driver)
        personal_account.visibility_of_account_navigation()
        personal_account.click_on_exit_button()
        login_page = LoginPage(driver)
        assert 'https://stellarburgers.nomoreparties.site/login' == login_page.get_current_url_with_wait()
