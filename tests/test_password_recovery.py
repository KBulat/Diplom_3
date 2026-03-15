import allure
from data import URLs
from pages.login_page import LoginPage
from pages.password_recovery import PasswordRecoveryPage

@allure.suite("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title("Проверка перехода на страницу восстановления пароля по клику на 'Восстановить пароль'")
    def test_password_recovery_button(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_on_recovery_button()

        assert driver.current_url == URLs.password_recovery_page

    @allure.title("Проверка перехода на страницу сброса пароля при вводе почты и клике по кнопке 'Восстановить'")
    def test_password_reset_button(self, driver):
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.open_recover_password_page()
        recovery_page.fill_email_field("test@mail.ru")
        recovery_page.click_on_recovery_button()
        recovery_page.wait_for_reset_page_load()

        assert driver.current_url == URLs.password_reset_page

    @allure.title("Проверка активности поля с паролем после клика по кнопке показать/скрыть пароль")
    def test_password_field_activation_after_click_on_switcher(self, driver):
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.open_recover_password_page()
        recovery_page.fill_email_field("test@mail.ru")
        recovery_page.click_on_recovery_button()
        recovery_page.wait_for_reset_page_load()
        recovery_page.click_on_show_password_button()

        assert recovery_page.is_input_field_active()
