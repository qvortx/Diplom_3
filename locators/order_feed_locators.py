from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_FEED_TITLE = (By.XPATH, ".//h1[text()='Лента заказов']")
    TOTAL_ORDERS_COUNT = (
        By.XPATH,
        ".//p[contains(text(), 'Выполнено за вс')]/following-sibling::p"
    )
    TODAY_ORDERS_COUNT = (
        By.XPATH,
        ".//p[text()='Выполнено за сегодня:']/following-sibling::p"
    )
    ORDERS_IN_PROGRESS_ITEMS = (
        By.XPATH,
        ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li"
    )
