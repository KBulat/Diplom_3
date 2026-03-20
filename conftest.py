import pytest
from selenium import webdriver
from data import BASE_URL
from pages.login_page import LoginPage

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login()
    return driver
