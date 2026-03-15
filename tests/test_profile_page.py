import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from data import URLs

@allure.suite("Личный кабинет")
class TestProfilePage:

    @allure.title("Переход на страницу профиля пользователя по клику на 'Личный кабинет'")
    def test_navigation_to_profile_page(self, login):
        main_page = MainPage(login)
        main_page.click_on_profile()
        main_page.wait_for_profile_page_load()

        assert main_page.get_current_url() == URLs.profile_page

    @allure.title("Переход в раздел 'История заказов' профиля")
    def test_navigation_to_order_history_page(self, login):
        main_page = MainPage(login)
        profile_page = ProfilePage(login)
        main_page.click_on_profile()
        main_page.wait_for_profile_page_load()
        profile_page.click_on_order_history()
        profile_page.wait_for_order_history_page_load()
        
        assert main_page.get_current_url() == URLs.order_history_page

    @allure.title("Выход из аккаунта по кнопке 'Выход'")
    def test_successful_logout_from_account(self, login):
        main_page = MainPage(login)
        profile_page = ProfilePage(login)
        main_page.click_on_profile()
        main_page.wait_for_profile_page_load()
        profile_page.click_logout_button()
        profile_page.wait_for_logout_completion()

        assert main_page.get_current_url() == URLs.login_page
