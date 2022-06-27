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
def test_price_negative(web_browser, start, finish):
    page_search = Search_Page(web_browser)
    page_search.search_input.send_keys("чайник")
    page_search.search_button.click()
    page_search.min_price.send_keys(str(start))
    page_search.max_price.send_keys(str(finish))
    page_search.ok_price_button.click()
    page_search.wait_page_loaded()
    assert f"https://aliexpress.ru/wholesale?CatId=0&minPrice={start}&maxPrice={finish}&page=1&SearchText=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA" \
           not in page_search.get_current_url()

#2 Регистрация по номеру телефона. Невалидный номер
@pytest.mark.xfail
@pytest.mark.parametrize('phone', [123456789, 12345678900, "a123456789", '$123456789', "ф123456789"])
def test_register_main(web_browser, phone):
    page = Main_Page(web_browser)
    page.regisrt_btn_main_page.click()
    page.input_phone.send_keys(str(phone))
    page.send_sms_btn.click()
    page.wait_page_loaded()
    assert page.enter_phone_msg.is_visible()

#3 Вход по невалидному email
@pytest.mark.parametrize('email', ["asdffasd", "sdfsdfs@", "sadfsdaf.com", '@#$%', "**@mail.ru"])
def test_register_main(web_browser, email):
    page = Main_Page(web_browser)
    enter = page.enter_btn_main_page.__getitem__(1)
    enter.click()
    page.input_password.send_keys("12345")
    page.input_username.send_keys(email)
    enter_btn = page.enter_btn_main_page.__getitem__(2)
    enter_link = page.register_window_enter.__getitem__(0)
    enter_link.click()
    enter_btn.click()
    page.wait_page_loaded()
    assert page.invalid_log_pass_msg.is_visible()
