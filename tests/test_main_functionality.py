import allure
from data import Urls
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.suite("Основная функциональность")
class TestMainFunctionality:

    @allure.title("Переход по клику на раздел 'Конструктор'")
    def test_navigate_to_constructor_opens_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.FEED_URL)

        main_page.click_constructor_button()

        assert (
            main_page.get_current_url() == Urls.BASE_URL
            and main_page.is_constructor_title_displayed()
        )

    @allure.title("Переход по клику на раздел 'Лента заказов'")
    def test_navigate_to_order_feed_opens_feed_page(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.open_url(Urls.BASE_URL)

        main_page.click_order_feed_button()

        assert (
            order_feed_page.get_current_url() == Urls.FEED_URL
            and order_feed_page.is_order_feed_title_displayed()
        )

    @allure.title("Появление всплывающего окна с деталями при клике на ингредиент")
    def test_click_ingredient_opens_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.BASE_URL)

        main_page.click_first_bun_ingredient()

        assert main_page.is_ingredient_modal_displayed()

    @allure.title("Закрытие всплывающего окна с деталями ингредиента по клику на крестик")
    def test_close_ingredient_modal_by_cross_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.BASE_URL)
        main_page.click_first_bun_ingredient()

        is_closed = main_page.close_modal()

        assert is_closed is True

    @allure.title("Увеличение счётчика ингредиента при добавлении его в заказ")
    def test_add_ingredient_to_order_increases_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.BASE_URL)
        initial_count = main_page.get_first_bun_counter_value()

        main_page.add_first_bun_to_order()
        updated_count = main_page.get_first_bun_counter_value()

        assert updated_count > initial_count
