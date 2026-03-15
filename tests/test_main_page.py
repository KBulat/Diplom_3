import allure
import pytest
from data import URLs, INGREDIENTS
from pages.main_page import MainPage

@allure.suite("Проверка основного функционала")
class TestMainPage:

    @allure.title("Переход по клику на «Конструктор»")
    def test_navigation_to_constructor_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_constructor()

        assert main_page.get_current_url() == URLs.main_page
        assert main_page.is_constructor_visible()

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_navigation_to_order_feed_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_order_feed()
        main_page.wait_for_order_feed_page_load()

        assert main_page.get_current_url() == URLs.order_feed_page

    @allure.title("Появление высплывающего окна при клике на ингредиент")
    @pytest.mark.parametrize("ingredient_name", INGREDIENTS)
    def test_click_on_ingredient_shows_modal_window(self, driver, ingredient_name):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_ingredient(ingredient_name)

        assert main_page.is_ingredient_modal_open()

    @allure.title("Закрытие всплывающего окна с деталями ингредиента")
    @pytest.mark.parametrize("ingredient_name", INGREDIENTS)
    def test_modal_closes_on_close_button_click(self, driver, ingredient_name):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_ingredient(ingredient_name)
        main_page.close_ingredient_modal()

        assert main_page.is_ingredient_modal_closed()

    @allure.title("Проверка увеличения каунтера при добавлении ингредиента в заказ")
    @pytest.mark.parametrize("ingredient_name", INGREDIENTS)    
    def test_add_ingredient_increases_counter(self, driver, ingredient_name):
        main_page = MainPage(driver)
        main_page.open_main_page()
        counter_before = main_page.get_ingredient_counter(ingredient_name)
        main_page.add_ingredient_to_constructor(ingredient_name)

        counter_after = main_page.get_ingredient_counter(ingredient_name)

        assert counter_after > counter_before

    @allure.title("Проверка возможности авторизованного пользователя создать заказ")
    def test_logged_user_can_create_order(self, login):
        main_page = MainPage(login)
        main_page.add_ingredient_to_constructor(INGREDIENTS[0])
        main_page.click_on_order_button()

        assert main_page.is_order_completed()
