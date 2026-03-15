import allure
from data import URLs
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage

class ProfilePage(BasePage):
    
    @allure.step("Перейти на страницу профиля")
    def open_profile_page(self):
        self.get_url(URLs.profile_page)

    @allure.step("Кликнуть по разделу 'История заказов'")
    def click_on_order_history(self):
        self.click_on_element(ProfilePageLocators.order_history)

    @allure.step("Выполнить логаут")
    def click_logout_button(self):
        self.click_on_element(ProfilePageLocators.logout_button)
    
    @allure.step("Дождаться успешного выполнения логаута")
    def wait_for_logout_completion(self):
        self.wait_for_page_load(URLs.login_page)
    
    @allure.step("Дождаться загрузки страницы 'История заказов'")
    def wait_for_order_history_page_load(self):
        self.wait_for_page_load(URLs.order_history_page)
    
    @allure.step("Получить id последнего заказа в истории заказов")
    def get_id_of_last_order_in_history(self):
        order_text = self.get_element_text(ProfilePageLocators.last_order_id)
        return order_text.replace('#', '') if order_text else None
    