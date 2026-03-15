from selenium.webdriver.common.by import By

class LoginPageLocators:
    email_field = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    password_field = (By.XPATH, "//input[@type='password']")
    login_button = (By.XPATH, "//button[text()='Войти']")
    recover_button = (By.XPATH, "//a[text()='Восстановить пароль']")
