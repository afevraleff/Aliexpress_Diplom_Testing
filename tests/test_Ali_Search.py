import time
import pytest
from pages.base import WebPage
from pages.main_page import Main_Page
from pages.elements import WebElement
from selenium.webdriver import ActionChains
from pages.search_page import Search_Page


#1-4 Cортировки. 1 По возрастанию цены

def test_search_sort_by_price_up(web_browser):
    page = Search_Page(web_browser)
    page.search_input.send_keys('мышь')
    page.search_button.click()
    page.price.click()
    page.wait_page_loaded()
    page.screenshot("sort_by_price_up.png")

#2 По убыванию цены

def test_search_sort_by_price_down(web_browser):
    page = Search_Page(web_browser)
    page.search_input.send_keys('мышь')
    page.search_button.click()
    page.price.click()
    page.wait_page_loaded()
    page.price.click()
    page.age_check.click()
    page.wait_page_loaded()
    page.screenshot("sort_by_price_down.png")

#3 Сначала новинки

def test_search_sort_by_new(web_browser):
    page = Search_Page(web_browser)
    page.search_input.send_keys('мышь')
    page.search_button.click()
    page.news.click()
    page.wait_page_loaded()
    page.screenshot("sort_by_new.png")

#4 По количеству заказов

def test_search_sort_by_orders(web_browser):
    page = Search_Page(web_browser)
    page.search_input.send_keys('мышь')
    page.search_button.click()
    page.orders.click()
    page.wait_page_loaded()
    page.screenshot("sort_by_orders.png")

#5-8 Фильтры поиска по одному
#5 Распродажа
def test_sale_filter(web_browser):
    page = Search_Page(web_browser)
    page.search_input.send_keys("чайник")
    page.search_button.click()
    page.wait_page_loaded()
    page.sale_filter.click()
    page.sale_product_card_mark.is_visible()

#6 Tmall
def test_tmall_filter(web_browser):
    page = Search_Page(web_browser)
    page.search_input.send_keys("чайник")
    page.search_button.click()
    page.wait_page_loaded()
    page.tmall_filter.click()
    page.wait_page_loaded()
    assert "https://aliexpress.ru/wholesale?CatId=0&isTmall=y&isFreeShip=n&isFavorite=n&page=1&SearchText=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA"\
           in page.get_current_url()

#7 Бесплатная доставка
def test_free_delivery_filter(web_browser):
    page = Search_Page(web_browser)
    page.search_input.send_keys("чайник")
    page.search_button.click()
    page.wait_page_loaded()
    page.cookie_banner_close.click()
    page.free_delivery_filter.click()
    page.wait_page_loaded()
    assert "https://aliexpress.ru/wholesale?CatId=0&isTmall=n&isFreeShip=y&isFavorite=n&page=1&SearchText=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA" \
           in page.get_current_url()

#8 4 звезды и более
def test_four_stars_filter(web_browser):
    page = Search_Page(web_browser)
    page.search_input.send_keys("чайник")
    page.search_button.click()
    page.wait_page_loaded()
    page.cookie_banner_close.click()
    page.four_stars_filter.click()
    page.wait_page_loaded()
    assert "https://aliexpress.ru/wholesale?CatId=0&isTmall=n&isFreeShip=n&isFavorite=y&page=1&SearchText=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA" \
           in page.get_current_url()

#9-10 Фильтры поиска по методу Pairwase
#9 Распродажа, Tmall, Плюс, Бесплатная доставка, 4+звезды
def test_all_filters(web_browser):
    page = Search_Page(web_browser)
    page.search_input.send_keys("чайник")
    page.search_button.click()
    page.wait_page_loaded()
    page.cookie_banner_close.click()
    page.four_stars_filter.click()
    page.wait_page_loaded()
    page.tmall_filter.click()
    page.plus_delivery_filter.click()
    page.wait_page_loaded()
    page.free_delivery_filter.click()
    page.wait_page_loaded()
    page.sale_filter.click()
    page.wait_page_loaded()
    assert "https://aliexpress.ru/wholesale?CatId=0&isPlus=y&isTmall=y&isFreeShip=y&isFavorite=y&page=1&SearchText=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA" \
           in page.get_current_url()

#10 Tmall, Плюс, Бесплатная доставка
def test_tmall_plus_free_delivery_filters(web_browser):
    page = Search_Page(web_browser)
    page.search_input.send_keys("чайник")
    page.search_button.click()
    page.wait_page_loaded()
    page.cookie_banner_close.click()
    page.tmall_filter.click()
    page.wait_page_loaded()
    page.plus_delivery_filter.click()
    page.wait_page_loaded()
    page.free_delivery_filter.click()
    page.wait_page_loaded()
    assert "https://aliexpress.ru/wholesale?CatId=0&isPlus=y&isTmall=y&isFreeShip=y&isFavorite=n&page=1&SearchText=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA" \
           in page.get_current_url()

#11 Цена позитивные
@pytest.mark.parametrize("min", [1, 100, 1000])
@pytest.mark.parametrize("max", [1000, 100000, 1000000])
def test_price_positive(web_browser, min, max):
    page = Search_Page(web_browser)
    page.search_input.send_keys("чайник")
    page.search_button.click()
    page.min_price.send_keys(str(min))
    page.max_price.send_keys(str(max))
    page.ok_price_button.click()
    page.wait_page_loaded()
    assert f"https://aliexpress.ru/wholesale?CatId=0&minPrice={min}&maxPrice={max}&page=1&SearchText=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA" \
           in page.get_current_url()







