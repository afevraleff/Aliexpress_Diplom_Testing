import time
import pytest
from pages.base import WebPage
from pages.main_page import Main_Page
from pages.elements import WebElement
from selenium.webdriver import ActionChains
from pages.search_page import Search_Page



#1 Страница поиска. Фильтр цена. Негативные
@pytest.mark.parametrize("start", [-1, "p", '$', "ц"])
@pytest.mark.parametrize("finish", [-1000, 'f', "@", "щ"])
def test_price_negative(web_browser_neg, start, finish):
    page_search = Search_Page(web_browser_neg)
    page_search.search_input.send_keys("чайник")
    page_search.search_button.click()
    page_search.min_price.send_keys(str(start))
    page_search.max_price.send_keys(str(finish))
    page_search.ok_price_button.click()
    page_search.wait_page_loaded()
    assert f"https://aliexpress.ru/wholesale?CatId=0&minPrice={start}&maxPrice={finish}&page=1&SearchText=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA" \
           not in page_search.get_current_url()
