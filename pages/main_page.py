import allure
from data import URLs, INGREDIENTS
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Перейти на главную страницу")
    def open_main_page(self):
        self.get_url(URLs.main_page)
    
    @allure.step("Перейти на страницу 'Конструктор'")
    def click_on_constructor(self):
        self.click_on_element(MainPageLocators.constructor_button)

    @allure.step("Перейти на страницу 'Лента заказов'")
    def open_order_feed(self):
        self.click_on_element(MainPageLocators.order_feed)  

    @allure.step("Дождаться загрузки Ленты заказов")
    def wait_for_order_feed_page_load(self):
        self.wait_for_page_load(URLs.order_feed_page)
    
    @allure.step("Проверить отображение конструктора")
    def is_constructor_visible(self):
        title = self.find_visible_element(MainPageLocators.constructor_title).is_displayed()
        basket = self.find_visible_element(MainPageLocators.constructor_area).is_displayed()
        return title and basket

    @allure.step("Перейти на страницу 'Личный кабинет'")
    def click_on_profile(self):
        self.click_on_element(MainPageLocators.profile_button)
    
    @allure.step("Дождаться загрузки Личного кабинета")
    def wait_for_profile_page_load(self):
        self.wait_for_page_load(URLs.profile_page)
    
    @allure.step("Кликнуть по ингредиенту {name}")
    def click_on_ingredient(self, name):
        locator = MainPageLocators.ingredient_by_name(name)
        self.click_on_element(locator)

    @allure.step("Кликнуть по кнопке 'Оформить заказ'")
    def click_on_order_button(self):
        self.click_on_element(MainPageLocators.order_button)
    
    @allure.step("Проверить открытие модального окна")
    def is_ingredient_modal_open(self):
        return self.find_visible_element(MainPageLocators.ingredient_modal_header)
    
    @allure.step("Закрыть модальное окно с деталями ингредиента")
    def close_ingredient_modal(self):
        self.click_on_element(MainPageLocators.ingredient_modal_close)

    @allure.step("Проверить закрытие модального окна с деталями ингредиента")
    def is_ingredient_modal_closed(self):
        return self.find_invisible_element(MainPageLocators.ingredient_modal_header)
    
    @allure.step("Проверить готовность оформления заказа")
    def is_order_completed(self):
        return self.find_visible_element(MainPageLocators.order_prepared).is_displayed()
    
    @allure.step("Дождаться подтверждения заказа")    
    def wait_for_order_accept(self):
        self.find_visible_element(MainPageLocators.order_prepared)
    
    @allure.step("Закрыть модальное окно")
    def close_order_modal(self):
        self.js_click(MainPageLocators.ingredient_modal_close)
    
    @allure.step("Получить значение счетчика ингредиента {ingredient_name}")
    def get_ingredient_counter(self, ingredient_name):
        locator = MainPageLocators.ingredient_counter_by_name(ingredient_name)
        counter_text = self.get_element_text(locator)
        return int(counter_text)

    @allure.step("Добавить ингредиенты в конструктор через drag & drop")
    def add_ingredient_to_constructor(self, ingredient_name):
        ingredient_locator = MainPageLocators.ingredient_by_name(ingredient_name)
        self.move_element(ingredient_locator, MainPageLocators.constructor_area)

    @allure.step("Создать заказ")
    def create_order(self):
        self.click_on_constructor()
        for ingredient_name in INGREDIENTS:
            self.add_ingredient_to_constructor(ingredient_name)
        self.click_on_order_button()
        order_id = self.get_order_id_in_modal()        
        self.close_order_detail_modal()
        self.wait_for_order_feed_to_be_clickable()
        self.wait_overlay_to_close(MainPageLocators.overlay_modal)
        return order_id
    
    @allure.step("Проверить наличие заказа с id {order_id} в ленте")
    def is_order_in_feed(self,  order_id):
        formatted_id = f"#{order_id}"
        order_id_in_feed_locator = (By.XPATH, f"//ul[contains(@class, 'OrderFeed_list')]//p[contains(@class, 'text_type_digits-default') and text()='{formatted_id}']")
        element = self.find_visible_element(order_id_in_feed_locator)
        return element.is_displayed()
    
    @allure.step("Получить id заказа в окне с деталями заказа")
    def get_order_id_in_modal(self):
        element = self.find_visible_element(MainPageLocators.order_id)
        self.wait_for_text_to_change(MainPageLocators.order_id, '9999')
        text = self.driver.execute_script("return arguments[0].textContent.trim();", element)
        return text.lstrip('0') or '0'        
    
    @allure.step("Закрыть окно с деталями заказа")
    def close_order_detail_modal(self):
        self.click_on_element(MainPageLocators.order_detail_close_button)
