import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    @allure.step("Проверить отображение заголовка 'Лента заказов'")
    def is_order_feed_title_displayed(self):
        return self.is_element_visible(OrderFeedLocators.ORDER_FEED_TITLE)

    @allure.step("Получить значение счётчика 'Выполнено за всё время'")
    def get_total_orders_count(self):
        return int(self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNT))

    @allure.step("Получить значение счётчика 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        return int(self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNT))

    @allure.step("Дождаться обновления счётчика 'Выполнено за всё время' выше {previous_value}")
    def wait_total_orders_count_increased(self, previous_value, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: self.get_total_orders_count() > previous_value
            )
        except TimeoutException:
            pass
        return self.get_total_orders_count()

    @allure.step("Дождаться обновления счётчика 'Выполнено за сегодня' выше {previous_value}")
    def wait_today_orders_count_increased(self, previous_value, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: self.get_today_orders_count() > previous_value
            )
        except TimeoutException:
            pass
        return self.get_today_orders_count()

    @allure.step("Дождаться появления заказа {order_number} в разделе 'В работе'")
    def wait_and_get_orders_in_progress(self, order_number, timeout=20):
        expected_number = str(order_number).lstrip("0")

        def order_present(driver):
            items = driver.find_elements(*OrderFeedLocators.ORDERS_IN_PROGRESS_ITEMS)
            numbers = [item.text.strip().lstrip("0") for item in items if item.text.strip().isdigit()]
            return numbers if expected_number in numbers else False

        try:
            return WebDriverWait(self.driver, timeout).until(order_present)
        except TimeoutException:
            items = self.driver.find_elements(*OrderFeedLocators.ORDERS_IN_PROGRESS_ITEMS)
            return [item.text.strip().lstrip("0") for item in items if item.text.strip().isdigit()]
