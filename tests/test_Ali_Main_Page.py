import time
import pytest
from pages.base import WebPage
from pages.main_page import Main_Page
from pages.elements import WebElement
from pages.search_page import Search_Page


#1 Наличие основных элементов на  главной странице
def test_start_page_main_elements(web_browser):
    page = Main_Page(web_browser)
    time.sleep(5)
    assert page.main_menu_top.is_visible()
    assert page.categories_menu.is_visible()
    assert page.search_input.is_clickable()
    assert page.logo.is_visible()
    assert page.welcome_block.is_visible()
    assert page.carusel.is_visible()
    assert page.product_cards.is_visible()
    page.search_input.send_keys('loh')
    page.search_btn.click()
    page.scroll_down()
    assert page.footer.is_visible()

    time.sleep(5)

#2 Переходы по главным ссылкам
@pytest.mark.parametrize("locator", ['Телефоны и аксессуары', 'Компьютеры и оргтехника', 'Электроника',
                                     'Бытовая техника', 'Одежда для женщин', 'Одежда для мужчин', 'Всё для детей',
                                     'Украшения', 'часы', 'Сумки',  'обувь', 'Дом', 'зоотовары', 'Автотовары',
                                     'Красота и здоровье', 'Спорт и развлечения'])
def test_categories_links(web_browser, locator):
    page = Main_Page(web_browser)
    page._web_driver.find_element_by_link_text(locator).click()
    if page.age_check.is_presented():
        page.age_check.click()
    page.scroll_down()
    assert page.searched_product_cards.is_visible()
#3- Ссылки главного меню
def test_main_menu_cabinet(web_browser):
    page = Main_Page(web_browser)
    page.sell_on_aliexpress.click()
    page.cabinet_link.click()
    assert page.buisness_logo.is_visible()
#4
def test_main_become_seller(web_browser):
    page = Main_Page(web_browser)
    page.sell_on_aliexpress.click()
    page.become_seller.click()
    assert page.open_shop.is_visible()
#5
def test_main_support(web_browser):
    page = Main_Page(web_browser)
    page.help_menu.click()
    page.support_menu.click()
    assert page.help_instructions.is_visible()
#6
def test_main_disputes_complains(web_browser):
    page = Main_Page(web_browser)
    page.help_menu.click()
    page.disputes_complaints.click()
    assert "https://login.aliexpress.com" in page.get_current_url()

#7
def test_main_authors_rights(web_browser):
    page = Main_Page(web_browser)
    page.help_menu.click()
    page.authors_rights.click()
    assert "https://ipp.alibabagroup.com/" in page.get_current_url()

#8
def test_main_customer_protection(web_browser):
    page = Main_Page(web_browser)
    page.customer_protection.click()
    assert "https://ru.aliexpress.com/p/buyerprotection/" in page.get_current_url()


#9
def test_main_application(web_browser):
    page = Main_Page(web_browser)
    page.application.click()
    assert page.application_links.is_visible()

#10
def test_main_lang_selector(web_browser):
    page = Main_Page(web_browser)
    page.destination_selector.click()
    assert page.lang_options.is_visible()
    assert page.save_lang_opt_btn.is_visible()
















def test_search_in_python_chrome(setUp):
    # Assigning a local variable for the global driver
    # Go to google.com
    driver = setUp
    driver.get('http://www.google.com')

    # Pauses the screen for 5 seconds so we have time to confirm it arrived at the right page
    time.sleep(5)

    # Find and select the search box element on the page
    search_box = driver.find_element_by_name('q')

    # Enter text into the search box
    search_box.send_keys('Devin Mancuso')