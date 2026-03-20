import allure
from pages.order_feed import OrderFeedPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage

@allure.suite("Лента заказов")
class TestOrderFeed:

   @allure.title("Проверка открытия деталей заказа при клике на заказ")
   def test_open_order_details(self, driver):
      main_page = MainPage(driver)
      order_feed_page = OrderFeedPage(driver)
      main_page.open_order_feed()
      order_feed_page.open_first_order()

      assert order_feed_page.is_order_modal_opened()

   @allure.title("Проверка отображения заказов пользователя в ленте заказов")
   def test_user_orders_appear_in_order_feed(self, login):
      main_page = MainPage(login)
      profile_page = ProfilePage(login)
      main_page.create_order()
      main_page.click_on_profile()
      main_page.wait_for_profile_page_load()
      profile_page.click_on_order_history()
      profile_page.wait_for_order_history_page_load()
      last_order_id = profile_page.get_id_of_last_order_in_history()

      main_page.open_order_feed()
      main_page.wait_for_order_feed_page_load()

      assert main_page.is_order_in_feed(last_order_id)

   @allure.title("Проверка увеличения счётчика 'Выполнено за всё время' при создании нового заказа")
   def test_total_orders_counter_increases_when_order_created(self, login):
      main_page = MainPage(login)
      order_feed_page = OrderFeedPage(login)
      main_page.open_order_feed()
      all_time_orders_count = order_feed_page.get_total_completed_orders()
      main_page.create_order()
      main_page.open_order_feed()
      all_time_orders_count_updated = order_feed_page.get_total_completed_orders()

      assert all_time_orders_count_updated == all_time_orders_count + 1

   @allure.title("Проверка увеличения счётчика 'Выполнено за сегодня' при создании нового заказа")
   def test_today_orders_counter_increases_when_order_created(self, login):
      main_page = MainPage(login)
      order_feed_page = OrderFeedPage(login)
      main_page.open_order_feed()
      today_orders_count = order_feed_page.get_today_orders()
      main_page.create_order()
      main_page.open_order_feed()
      today_orders_count_updated = order_feed_page.get_today_orders()

      assert today_orders_count_updated > today_orders_count

   @allure.title("Проверка отображения номера созданного заказа в разделе 'В работе'")
   def test_created_order_shows_up_in_orders_in_progress(self, login):
      main_page = MainPage(login)
      order_feed_page = OrderFeedPage(login)

      order_id = main_page.create_order()
      main_page.open_order_feed()
      main_page.wait_for_order_feed_page_load()

      order_feed_page.wait_for_specific_order_in_work_list(order_id)
      orders_in_work = order_feed_page.get_orders_id_in_work_list()

      assert int(order_id) in orders_in_work
