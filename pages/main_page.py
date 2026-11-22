import allure
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import OrderData


class MainPage(BasePage):

    @allure.step("Перейти в раздел 'Конструктор'")
    def click_constructor_button(self):
        self.wait_for_element_invisible(MainPageLocators.MODAL_OVERLAY)
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Перейти в раздел 'Лента заказов'")
    def click_order_feed_button(self):
        self.wait_for_element_invisible(MainPageLocators.MODAL_OVERLAY)
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Проверить отображение заголовка 'Соберите бургер'")
    def is_constructor_title_displayed(self):
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step("Кликнуть по первому ингредиенту в списке")
    def click_first_bun_ingredient(self):
        self.wait_for_element_invisible(MainPageLocators.MODAL_OVERLAY)
        self.click_element(MainPageLocators.FIRST_BUN_INGREDIENT)

    @allure.step("Проверить отображение всплывающего окна с деталями ингредиента")
    def is_ingredient_modal_displayed(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step("Закрыть всплывающее окно кликом по крестику")
    def close_modal(self):
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)
        return self.wait_for_element_invisible(MainPageLocators.MODAL_OPENED)

    @allure.step("Получить значение счётчика первого ингредиента")
    def get_first_bun_counter_value(self):
        return int(self.get_text(MainPageLocators.FIRST_BUN_COUNTER))

    @allure.step("Перетащить первую булку в конструктор заказа")
    def add_first_bun_to_order(self):
        self.wait_for_element_invisible(MainPageLocators.MODAL_OVERLAY)
        self.drag_and_drop_element(
            MainPageLocators.FIRST_BUN_INGREDIENT,
            MainPageLocators.CONSTRUCTOR_BASKET
        )

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_create_order_button(self):
        self.wait_for_element_invisible(MainPageLocators.MODAL_OVERLAY)
        self.click_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Дождаться присвоения и получить номер оформленного заказа")
    def get_created_order_number(self, timeout=30):
        def order_number_is_ready(driver):
            elements = driver.find_elements(*MainPageLocators.ORDER_MODAL_NUMBER)
            if not elements or not elements[0].is_displayed():
                return False
            text = elements[0].text.strip()
            return text if text.isdigit() and text != OrderData.PLACEHOLDER_ORDER_NUMBER else False

        return WebDriverWait(self.driver, timeout).until(order_number_is_ready)

    @allure.step("Оформить новый заказ с булкой и вернуть его номер")
    def create_order_and_get_number(self):
        self.add_first_bun_to_order()
        self.click_create_order_button()
        order_number = self.get_created_order_number()
        self.close_modal()
        return order_number
