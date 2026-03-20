from selenium.webdriver.common.by import By

class ProfilePageLocators:
    order_history = (By.XPATH, "//a[text()='История заказов']")
    logout_button = (By.XPATH, "//button[text()='Выход']")
    last_order_id = (By.XPATH, "(//ul[contains(@class, 'OrderHistory_list')]/li[last()]//p[contains(@class, 'text_type_digits-default')])[1]")