
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements
class Search_Page(WebPage):

    def __init__(self, web_driver, url=''):
        url = "https://aliexpress.ru/all-wholesale-products.html"
        self._web_driver = web_driver
        web_driver.get('chrome://settings/')
        web_driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.8);')
        self.get(url)

    def get(self, url):
        self._web_driver.get(url)
        self.wait_page_loaded()



    search_input = WebElement(id='search-key')
    search_button = WebElement(class_name='search-button')
    price = WebElement(xpath='//button[contains(text(), "Цена")]')
    age_check = WebElement(xpath='//span[contains(text(), "Я СТАРШЕ 18")]')
    news = WebElement(xpath='//button[contains(text(), "Новинки")]')
    orders = WebElement(xpath='//button[contains(text(), "По заказам")]')
    sale_filter = WebElement(xpath='//span[contains(text(), "Товары на распродаже")]')
    sale_product_card_mark = ManyWebElements(xpath='//span[contains(text(), "Товары на распродаже")]')
    tmall_filter = WebElement(xpath='//img[@class="SearchMainFilters_FeaturesFilterTag__img__1h98u" and @width=40]')
    free_delivery_filter = WebElement(xpath='//div[@exp_type="free_shipping"]')
    four_stars_filter = WebElement(xpath='//span[contains(text(), "или более")]')
    plus_delivery_filter = WebElement(xpath='//img[@class="SearchMainFilters_FeaturesFilterTag__img__1h98u" and @width="29"]')
    cookie_banner_close = WebElement(class_name="PrivacyPolicyBanner_PrivacyPolicyBanner__close__5dnwg")
    min_price = WebElement(xpath='//input[@placeholder="мин"]')
    max_price = WebElement(xpath='//input[@placeholder="макс"]')
    ok_price_button = WebElement(xpath='//button[@type="submit" and contains(text(), "OK")]')