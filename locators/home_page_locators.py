from selenium.webdriver.common.by import By


class HomePageLocators:
    PRIVATE_ACCOUNT_TEXT = (By.XPATH, '//p[text()="Личный Кабинет"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')
    BURGER_INGREDIENTS_SECTION = (By.XPATH, '//h1[text()="Соберите бургер"]')
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]')
    INGREDIENT = (By.XPATH, "//ul[1]/a[1]")
    MODAL_WINDOW_WITH_INGREDIENT_DETAILS = (By.CLASS_NAME, "Modal_modal__contentBox__sCy8X")
    OPENED_MODAL_WINDOW = (By.CLASS_NAME, 'Modal_modal_opened__3ISw4')
    MODAL_WINDOW_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'modal__close')]")
    BURGER_CONSTRUCTOR_BASKET = (By.CLASS_NAME, 'BurgerConstructor_basket__list__l9dp_')
    COUNTER = (By.CLASS_NAME, 'counter_counter__num__3nue1')
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    ORDER_PREPARED_MODAL_WINDOW = (By.CLASS_NAME, "Modal_modal__contentBox__sCy8X")
    ORDER_NUMBER_IN_MODAL_WINDOW = (By.CSS_SELECTOR, '.Modal_modal__title__2L34m')
