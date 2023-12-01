from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators
from faker import Faker
from urls import Urls
import allure

fake = Faker()


class ForgotPasswordPage(BasePage):

    @allure.step("Установка электронной почты для восстановления пароля")
    def set_email_to_recover(self):
        self.send_keys(ForgotPasswordLocators.PASSWORD_RECOVERY_INPUT, fake.email())

    @allure.step("Клик по кнопке восстановления пароля")
    def click_recovery_button(self):
        self.click_on_element(ForgotPasswordLocators.RECOVERY_PASSWORD_BUTTON)

    @allure.step("Переход на страницу восстановления пароля")
    def go_to_forgot_password_page(self):
        self.go_to_page(Urls.forgot_password_url)
