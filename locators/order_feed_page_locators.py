from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    order_card = (By.XPATH, './/*[contains(@class, "OrderHistory_link") and @href]')
    order_number = (By.XPATH, ".//p[contains(text()='#')]")
    order_modal = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    total_completed_orders = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    today_orders_count = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    completed_orders_count = (By.XPATH, "//p[text()='Готовы:']/following-sibling::ul[1]/li")
    order_id = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")
    orders_in_progress = (By.XPATH, ".//ul[contains(@class,'OrderFeed_orderListReady')]/li[contains(@class,'text_type_digits-default')]")