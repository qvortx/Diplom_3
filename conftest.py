import pytest
import allure
from selenium import webdriver
from data import Urls
from helpers import generate_user_payload, UserApi
from pages.login_page import LoginPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """
    Инициализирует браузер (Chrome или Firefox) перед тестом
    и закрывает его после завершения теста.
    """
    if request.param == "chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()

    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def created_user():
    """
    Создаёт уникального пользователя через API перед тестом
    и удаляет его после завершения теста.
    """
    user_data = generate_user_payload()
    response = UserApi.create_user(user_data)
    access_token = response.json().get("accessToken")

    yield {
        **user_data,
        "access_token": access_token
    }

    with allure.step("Пост-условие (Teardown): удалить тестового пользователя через API"):
        if access_token:
            UserApi.delete_user(access_token)


@pytest.fixture
def authorized_driver(driver, created_user):
    """
    Авторизует созданного через API пользователя в браузере
    и возвращает готовый к работе драйвер на главной странице.
    """
    login_page = LoginPage(driver)
    login_page.open_url(Urls.LOGIN_URL)
    login_page.login(created_user["email"], created_user["password"])
    return driver
