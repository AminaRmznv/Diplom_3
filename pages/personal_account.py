from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
from urls import Urls
import allure


class PersonalAccountPage(BasePage):

    @allure.step("Проверка видимости навигации личного кабинета")
    def visibility_of_account_navigation(self):
        return self.wait_for_element_visibility(PersonalAccountLocators.ACCOUNT_NAV)

    @allure.step("Клик по кнопке истории заказов")
    def click_order_history_button(self):
        self.click_on_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Переход на страницу личного кабинета")
    def go_to_personal_account_page(self):
        self.go_to_page(Urls.personal_account_url)

    @allure.step("Клик по кнопке выхода из личного кабинета")
    def click_on_exit_button(self):
        self.click_on_element(PersonalAccountLocators.EXIT_FROM_PERSONAL_ACCOUNT_BUTTON)
