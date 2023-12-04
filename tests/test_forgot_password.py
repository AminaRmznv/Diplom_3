import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


class TestForgotPassword:

    @allure.title("Тест перехода на страницу восстановления пароля")
    @allure.description(
        "Проверка перехода на страницу восстановления пароля через клик по кнопке 'Восстановить пароль'")
    def test_password_reset_page_navigation(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_login_page()
        login_page.click_on_forgot_password_button()
        current_url = login_page.get_current_url()
        assert current_url == 'https://stellarburgers.nomoreparties.site/forgot-password'

    @allure.title("Тест сброса пароля с действительным email")
    @allure.description(
        "Проверка процесса сброса пароля, начиная с ввода действительного email и завершая переходом на страницу сброса пароля")
    def test_password_reset_with_valid_email(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_login_page()
        login_page.click_on_forgot_password_button()
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.set_email_to_recover()
        forgot_password.click_recovery_button()
        reset_password = ResetPasswordPage(driver)
        reset_password.visibility_of_password_recovery_table()
        current_url = reset_password.check_current_reset_password_url()
        assert current_url == 'https://stellarburgers.nomoreparties.site/reset-password'

    @allure.title("Тест переключения видимости пароля")
    @allure.description("Проверка функциональности переключения видимости пароля на странице сброса пароля")
    def test_toggle_password_visibility(self, driver):
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.go_to_forgot_password_page()
        forgot_password.set_email_to_recover()
        forgot_password.click_recovery_button()
        reset_password = ResetPasswordPage(driver)
        reset_password.visibility_of_password_recovery_table()
        reset_password.enter_new_password()
        reset_password.click_visibility_icon()
        assert "input_status_active" in reset_password.get_value_attribute()
