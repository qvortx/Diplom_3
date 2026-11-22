from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']/parent::a")
    ORDER_FEED_BUTTON = (By.XPATH, ".//a[@href='/feed']")
    CONSTRUCTOR_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

    FIRST_BUN_INGREDIENT = (By.XPATH, "(.//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")
    FIRST_BUN_COUNTER = (
        By.XPATH,
        "(.//a[contains(@class, 'BurgerIngredient_ingredient')])[1]//p[contains(@class, 'counter_counter__num')]"
    )
    CONSTRUCTOR_BASKET = (By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]")

    MODAL_OPENED = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]")
    MODAL_OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay')]")
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        ".//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]"
    )
    INGREDIENT_MODAL_TITLE = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    ORDER_MODAL_NUMBER = (
        By.XPATH,
        ".//section[contains(@class, 'Modal_modal_opened')]//h2[contains(@class, 'Modal_modal__title')]"
    )
