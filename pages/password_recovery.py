import allure
from data import URLs
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage

class PasswordRecoveryPage(BasePage):

    @allure.step("Перейти на страницу восстановления пароля")
    def open_recover_password_page(self):
        self.get_url(URLs.password_recovery_page)
    
    @allure.step("Заполнить поля Email")
    def fill_email_field(self, email_address):
        self.send_keys_to_field(PasswordRecoveryPageLocators.email_field, email_address)

    @allure.step("Кликнуть по кнопке 'Восстановить'")
    def click_on_recovery_button(self):
        self.click_on_element(PasswordRecoveryPageLocators.recover_button)

    @allure.step("Дождаться загрузки страницы после ввода пароля")
    def wait_for_reset_page_load(self):
        self.wait_for_page_load(URLs.password_reset_page)

    @allure.step("Кликнуть по элементу 'Показать/Скрыть пароль'")
    def click_on_show_password_button(self):
        self.click_on_element(PasswordRecoveryPageLocators.show_password)

    @allure.step("Проверить активность поля с паролем")
    def is_input_field_active(self):
        return self.find_visible_element(PasswordRecoveryPageLocators.active_password_field)
    
    @allure.step("Дождаться загрузки страницы восстановления пароля")
    def wait_for_recovery_page_load(self):
        self.wait_for_page_load(URLs.password_recovery_page)
    
    @allure.step("Дождаться загрузки страницы установки нового пароля")
    def wait_for_reset_page_load(self):
        self.wait_for_page_load(URLs.password_reset_page)
