import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.suite("Раздел 'Лента заказов'")
class TestOrderFeed:

    @allure.title("Увеличение счётчика 'Выполнено за всё время' при создании нового заказа")
    def test_create_order_increases_total_orders_counter(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        order_feed_page = OrderFeedPage(authorized_driver)

        main_page.click_order_feed_button()
        count_before = order_feed_page.get_total_orders_count()

        main_page.click_constructor_button()
        main_page.create_order_and_get_number()

        main_page.click_order_feed_button()
        count_after = order_feed_page.wait_total_orders_count_increased(count_before)

        assert count_after > count_before

    @allure.title("Увеличение счётчика 'Выполнено за сегодня' при создании нового заказа")
    def test_create_order_increases_today_orders_counter(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        order_feed_page = OrderFeedPage(authorized_driver)

        main_page.click_order_feed_button()
        count_before = order_feed_page.get_today_orders_count()

        main_page.click_constructor_button()
        main_page.create_order_and_get_number()

        main_page.click_order_feed_button()
        count_after = order_feed_page.wait_today_orders_count_increased(count_before)

        assert count_after > count_before

    @allure.title("Появление номера оформленного заказа в разделе 'В работе'")
    def test_created_order_number_appears_in_progress_section(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        order_feed_page = OrderFeedPage(authorized_driver)

        order_number = main_page.create_order_and_get_number()
        main_page.click_order_feed_button()
        orders_in_progress = order_feed_page.wait_and_get_orders_in_progress(order_number)

        assert order_number.lstrip("0") in orders_in_progress
    