import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Клик по элементу")
    def click_on_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        # self.driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('click', {bubbles: true}));", element)
        # self.driver.execute_script("arguments[0].click();", element)
        element.click()

    @allure.step("Отправка данных в элемент")
    def send_keys(self, locator, value):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        element.send_keys(value)

    @allure.step("Переход на страницу")
    def go_to_page(self, url):
        self.driver.get(url)

    @allure.step("Поиск элемента")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Ожидание видимости элемента")
    def wait_for_element_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание скрытия элемента")
    def wait_for_element_invisibility(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))

    @allure.step("Ожидание появления элемента")
    def wait_for_element_located(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    @allure.step("Прокрутка к элементу")
    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Получение текущего URL с ожиданием")
    def get_current_url_with_wait(self):
        WebDriverWait(self.driver, 10).until(EC.url_changes(self.driver.current_url))
        return self.driver.current_url

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получение атрибута элемента")
    def get_attribute(self, locator, value):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.get_attribute(value)

    @allure.step("Установка элемента в локальное хранилище")
    def set_local_storage_item(self, key, value):
        self.driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")

    @allure.step("Обновление страницы")
    def refresh_page(self):
        self.driver.refresh()

    @allure.step("Получение текста элемента")
    def get_element_text(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)).text

    @allure.step("Ожидание URL содержащего текст")
    def wait_for_url_to_contain(self, text, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.url_contains(text))

    @allure.step("Перетаскивание элемента")
    def drag_and_drop(self, source_locator, target_locator):
        source_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(source_locator))
        target_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(target_locator))
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    @allure.step("Получение номеров заказов")
    def get_order_numbers(self, locator):
        order_numbers = []
        order_elements = self.driver.find_elements(*locator)
        for order_element in order_elements:
            order_number_text = order_element.text
            order_numbers.append(order_number_text)
        return order_numbers
