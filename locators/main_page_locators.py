from selenium.webdriver.common.by import By

class MainPageLocators:
    profile_button = (By.XPATH, "//p[text()='Личный Кабинет']")
    order_button = (By.XPATH, "//button[text()='Оформить заказ']")
    constructor_button = (By.XPATH, "//p[text()='Конструктор']")
    order_feed = (By.XPATH, "//p[text()='Лента Заказов']")
    order_id = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")
    order_prepared = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
    order_detail_close_button = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")

    # Конструктор заказов
    ingredient_modal_header = (By.XPATH, "//h2[text()='Детали ингредиента']")
    ingredient_modal_close = (By.XPATH, "//button[contains(@class, 'Modal_modal__close') and contains(@class, 'Modal_modal__close_modified')]")
    ingredient_counter = (By.XPATH, ".//p[contains(@class, 'counter_counter')]")
    constructor_area = (By.XPATH, "//section[contains(@class, 'BurgerConstructor')]")
    constructor_title = (By.XPATH, "//h1[text()='Соберите бургер']")

    overlay_loading = (By.XPATH, ".//*[contains(@class,'Modal_modal__loading')]")
    overlay_modal = (By.XPATH, ".//*[contains(@class,'Modal_modal_overlay__x2ZCr')]")

    @staticmethod
    def ingredient_by_name(name):
        return (By.XPATH, f"//p[text()='{name}']/parent::a[contains(@class, 'BurgerIngredient')]")
    
    @staticmethod
    def ingredient_counter_by_name(name):
        return (By.XPATH, f"//p[text()='{name}']/ancestor::a[contains(@class, 'BurgerIngredient')]//p[contains(@class, 'counter_counter__num')]")
    
    @staticmethod
    def order_in_feed_by_id(order_id):
        formatted_id = f"#{order_id}"
        return (By.XPATH, f"//ul[contains(@class, 'OrderFeed_list')]//p[contains(@class, 'text_type_digits-default') and text()='{formatted_id}']")