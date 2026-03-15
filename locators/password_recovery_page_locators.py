from selenium.webdriver.common.by import By

class PasswordRecoveryPageLocators:
    recover_button = (By.XPATH, "//button[text()='Восстановить']")
    email_field = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    show_password = (By.XPATH, "//div[contains(@class, 'icon-action')]")
    active_password_field = (By.XPATH, "//div[contains(@class, 'input_status_active')]/label")