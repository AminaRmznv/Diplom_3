from pages.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators
from faker import Faker
import allure

fake = Faker()


class ResetPasswordPage(BasePage):

    @allure.step("Проверка видимости таблицы восстановления пароля")
    def visibility_of_password_recovery_table(self):
        self.wait_for_element_visibility(ResetPasswordLocators.PASSWORD_RECOVERY_TABLE)

    @allure.step("Проверка текущего URL страницы сброса пароля")
    def check_current_reset_password_url(self):
        return self.get_current_url_with_wait()

    @allure.step("Ввод нового пароля")
    def enter_new_password(self):
        self.send_keys(ResetPasswordLocators.NEW_PASSWORD_INPUT, value=fake.password())

    @allure.step("Клик по иконке видимости")
    def click_visibility_icon(self):
        self.click_on_element(ResetPasswordLocators.VISIBILITY_ICON)

    @allure.step("Получение значения атрибута")
    def get_value_attribute(self):
        return self.get_attribute(ResetPasswordLocators.FOCUS, value='class')
