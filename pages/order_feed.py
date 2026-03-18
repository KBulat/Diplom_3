import allure
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage

class OrderFeedPage(BasePage):
        
    @allure.step("Кликнуть по первому заказу в ленте")
    def open_first_order(self):
        self.click_on_element(OrderFeedPageLocators.order_card)

    @allure.step("Проверить открытие модального окна с деталями заказа")
    def is_order_modal_opened(self):
        return self.find_visible_element(OrderFeedPageLocators.order_modal).is_displayed()
    
    @allure.step("Получить количество выполненных заказов за всё время")
    def get_total_completed_orders(self):
        return int(self.get_element_text(OrderFeedPageLocators.total_completed_orders))
    
    @allure.step("Получить количество выполненных заказов за сегодня")
    def get_today_orders(self):
        return int(self.get_element_text(OrderFeedPageLocators.today_orders_count))
        
    @allure.step("Получить список заказов в работе")
    def get_orders_in_progress(self):
        orders = self.find_visible_elements(OrderFeedPageLocators.orders_in_progress)

        order_texts = []
        for order in orders:
            order_texts.append(order.text)
        return order_texts    
    
    @allure.step("Получить список номеров заказов со статусом В работе")
    def get_orders_id_in_work_list(self):
        orders_id = self.find_visible_elements(OrderFeedPageLocators.orders_in_progress)
        orders_ids = []
        for order in orders_id:
            text = order.text
            number = int(text[1:])
            orders_ids.append(number)
        return orders_ids
        
    @allure.step("Дождаться появления конкретного заказа в списке 'В работе'")
    def wait_for_specific_order_in_work_list(self, order_id):
        locator = OrderFeedPageLocators.order_in_work_by_id(order_id)
        self.find_visible_element(locator)