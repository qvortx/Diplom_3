import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу: {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Найти видимый элемент по локатору: {locator}")
    def find_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Кликнуть по элементу: {locator}")
    def click_element(self, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст в поле: {locator}")
    def send_keys_to_element(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator, timeout=15):
        return self.find_element(locator, timeout=timeout).text

    @allure.step("Проверить видимость элемента: {locator}")
    def is_element_visible(self, locator, timeout=10):
        try:
            self.find_element(locator, timeout=timeout)
            return True
        except TimeoutException:
            return False

    @allure.step("Дождаться скрытия элемента: {locator}")
    def wait_for_element_invisible(self, locator, timeout=15):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            return False

    @allure.step("Перетащить элемент {source_locator} в область {target_locator}")
    def drag_and_drop_element(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();

            source.dispatchEvent(new DragEvent('dragstart', {
                bubbles: true, cancelable: true, dataTransfer: dataTransfer
            }));
            target.dispatchEvent(new DragEvent('dragenter', {
                bubbles: true, cancelable: true, dataTransfer: dataTransfer
            }));
            target.dispatchEvent(new DragEvent('dragover', {
                bubbles: true, cancelable: true, dataTransfer: dataTransfer
            }));
            target.dispatchEvent(new DragEvent('drop', {
                bubbles: true, cancelable: true, dataTransfer: dataTransfer
            }));
            source.dispatchEvent(new DragEvent('dragend', {
                bubbles: true, cancelable: true, dataTransfer: dataTransfer
            }));
            """,
            source,
            target
        )
