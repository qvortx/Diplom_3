class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru/"
    LOGIN_URL = f"{BASE_URL}login"
    FEED_URL = f"{BASE_URL}feed"

    API_REGISTER_ENDPOINT = f"{BASE_URL}api/auth/register"
    API_USER_ENDPOINT = f"{BASE_URL}api/auth/user"


class OrderData:
    PLACEHOLDER_ORDER_NUMBER = "9999"
