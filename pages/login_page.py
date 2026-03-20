import allure
from data import URLs, Credentials
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage

class LoginPage(BasePage):

    @allure.step("Открыть страницу логина")
    def open_login_page(self):
        self.get_url(URLs.login_page)

    @allure.step("Заполнить поле Email")
    def fill_email_field(self, email_address):
        self.send_keys_to_field(LoginPageLocators.email_field, email_address)

    @allure.step("Заполнить поле Пароль")
    def fill_password_field(self, password):
        self.send_keys_to_field(LoginPageLocators.password_field, password)

    @allure.step("Кликнуть по кнопке Войти")
    def click_login_button(self):
        self.js_click(LoginPageLocators.login_button)
    
    @allure.step("Дождаться успешной авторизации")
    def wait_for_successful_login(self):
        self.wait_for_page_load(URLs.main_page)

    @allure.step("Кликнуть по кнопке 'Восстановить'")
    def click_on_recovery_button(self):
        self.click_on_element(LoginPageLocators.recover_button)

    @allure.step("Выполнить авторизацию пользователя")
    def login(self):
        self.wait_for_page_load(URLs.login_page)
        self.fill_email_field(Credentials.email)
        self.fill_password_field(Credentials.password)
        self.click_login_button()
        self.wait_for_successful_login()
