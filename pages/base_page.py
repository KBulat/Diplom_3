import allure
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу {url}")
    def get_url(self, url):
        self.driver.get(url)

    @allure.step("Узнать адрес текущей страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Дождаться видимость элемента {locator}")
    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step("Дождаться видимость элементов")
    def find_visible_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Дождаться невидимости элемента {locator}")
    def find_invisible_element(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Дождаться кликабельности элемента {locator}")
    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step("Дождаться загрузки страницы")
    def wait_for_page_load(self, expected_url):
        self.wait.until(EC.url_to_be(expected_url))
    
    @allure.step("Дождаться закрытия оверлея")
    def wait_overlay_to_close(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Кликнуть по элементу")
    def click_on_element(self, locator):
        self.wait_overlay_to_close(MainPageLocators.overlay_loading)
        self.find_clickable_element(locator).click()

    @allure.step("Ввести данных в поле")
    def send_keys_to_field(self, locator, text):
        self.find_visible_element(locator).send_keys(text)

    @allure.step("Получить текст элемента")
    def get_element_text(self, locator):
        return self.find_visible_element(locator).text
    
    @allure.step("Кликнуть через JavaScript")
    def js_click(self, locator):
        element = self.find_visible_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
        
    @allure.step("Переместить элемент (drag & drop)")
    def move_element(self, source_locator, target_locator):
        source = self.find_visible_element(source_locator)
        target = self.find_visible_element(target_locator)

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", source)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target)

        drag_and_drop(self.driver, source, target)

    @allure.step("Проверить отображения элемента")
    def check_element_display(self, locator):
        return self.find_visible_element(locator).is_displayed()

    @allure.step("Дождаться изменения текста элемента")
    def wait_for_text_to_change(self, locator, text_value):
        return self.wait.until_not(EC.text_to_be_present_in_element(locator, text_value))
    
    @allure.step("Дождаться кликабельности ссылки на ленту заказов")
    def wait_for_order_feed_to_be_clickable(self):
        self.find_clickable_element(MainPageLocators.order_feed)
        