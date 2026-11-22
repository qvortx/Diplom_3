import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators


class LoginPage(BasePage):

    @allure.step("Авторизоваться пользователем {email}")
    def login(self, email, password):
        self.send_keys_to_element(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys_to_element(LoginPageLocators.PASSWORD_INPUT, password)
        self.wait_for_element_invisible(MainPageLocators.MODAL_OVERLAY)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(MainPageLocators.CREATE_ORDER_BUTTON)
