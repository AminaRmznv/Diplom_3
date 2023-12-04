from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from urls import Urls
import allure

class LoginPage(BasePage):

    @allure.step("Переход на страницу входа")
    def go_to_login_page(self):
        self.go_to_page(Urls.login_url)
        self.wait_for_element_visibility(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Клик по кнопке 'Забыли пароль?'")
    def click_on_forgot_password_button(self):
        self.click_on_element(LoginPageLocators.FORGOT_PASSWORD_LINK)
