import time
import pytest
from pages.base import WebPage
from pages.main_page import Main_Page
from pages.elements import WebElement
from selenium.webdriver import ActionChains


#1 Наличие основных элементов на  главной странице
def test_start_page_main_elements(web_browser):
    page = Main_Page(web_browser)
    assert page.main_menu_top.are_visible()
    assert page.categories_menu.are_visible()
    assert page.search_input.is_clickable()
    assert page.logo.are_visible()
    assert page.welcome_block.are_visible()
    assert page.carusel.are_visible()
    assert page.product_cards.are_visible()
    assert page.footer.are_visible()

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
    assert page.searched_product_cards.are_visible()

#3-15 Ссылки главного меню
def test_main_menu_cabinet(web_browser):
    page = Main_Page(web_browser)
    page.sell_on_aliexpress.click()
    page.cabinet_link.click()
    assert page.buisness_logo.are_visible()
#4
def test_main_become_seller(web_browser):
    page = Main_Page(web_browser)
    page.sell_on_aliexpress.click()
    page.become_seller.click()
    assert page.open_shop.are_visible()
#5
def test_main_support(web_browser):
    page = Main_Page(web_browser)
    page.help_menu.click()
    page.support_menu.click()
    assert page.help_instructions.are_visible()
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
    assert page.application_links.are_visible()

#10
def test_main_lang_selector(web_browser):
    page = Main_Page(web_browser)
    page.destination_selector.click()
    assert page.lang_options.are_visible()
    assert page.save_lang_opt_btn.are_visible()

# 11
def test_main_my_wishes(web_browser):
    page = Main_Page(web_browser)
    page.my_wishes.click()
    assert 'https://login.aliexpress.ru/' in page.get_current_url()

# 12
def test_main_my_profile(web_browser):
    page = Main_Page(web_browser)
    page.my_profile.click()
    assert 'https://login.aliexpress.ru/' in page.get_current_url()

# 13
def test_main_my_profile_menu_reg(web_browser):
    web_browser.get("https://aliexpress.ru/")
    web_browser.find_element_by_xpath(Main_Page.notif_banner).click()
    hoverable = web_browser.find_element_by_xpath(Main_Page.my_profile_loc)
    button_reg = web_browser.find_element_by_xpath(Main_Page.repistr_btn_main_loc)
    ActionChains(web_browser).move_to_element(hoverable).click(button_reg).perform()
    assert web_browser.find_element_by_xpath(Main_Page.reg_by_email_link_loc).is_displayed()

# 14
def test_main_my_profile_menu_log_in(web_browser):
    web_browser.get("https://aliexpress.ru/")
    web_browser.find_element_by_xpath(Main_Page.notif_banner).click()
    hoverable = web_browser.find_element_by_xpath(Main_Page.my_profile_loc)
    button_log_in = web_browser.find_element_by_xpath(Main_Page.log_in_btn_main_loc)
    ActionChains(web_browser).move_to_element(hoverable).click(button_log_in).perform()
    assert web_browser.find_element_by_xpath(Main_Page.log_in_by_phone_loc).is_displayed()

#15
@pytest.mark.parametrize("locator", [Main_Page.my_orders_main_loc, Main_Page.mess_center_main_loc,
                                     Main_Page.my_wishes_profile_main_loc, Main_Page.favorite_shops_main_loc,
                                     Main_Page.my_coupons_main_loc, Main_Page.get_coupons_main_loc])
def test_main_my_profile_menu(web_browser, locator):
    web_browser.get("https://aliexpress.ru/")
    web_browser.find_element_by_xpath(Main_Page.notif_banner).click()
    hoverable = web_browser.find_element_by_xpath(Main_Page.my_profile_loc)
    hidden_menu = web_browser.find_element_by_xpath(locator)
    ActionChains(web_browser).move_to_element(hoverable).click(hidden_menu).perform()
    assert "https://login.aliexpress.ru/" in web_browser.current_url

#16 Простой поисковой запрос, в карточках товара есть искомый текст
def test_search_button(web_browser):
    page = Main_Page(web_browser)
    page.search_input.send_keys("чайник")
    page.search_btn.click()
    page.product_cards_searched.are_visible()
    for elem in page.product_cards_searched.get_text():
        assert 'чайник' or 'Чайник' in elem

#17 Добавление товара в корзину без авторизции
def test_add_to_basket(web_browser):
    page = Main_Page(web_browser)
    page.search_input.send_keys("чайник")
    page.search_btn.click()
    page.product_cards_searched.are_visible()
    page.first_product_card.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.scroll_down(300)
    page.add_to_basket.click()
    page.wait_page_loaded()
    assert page.basket_banner.are_visible()

#18 Добавление товара в Мои желания без авторизции
def test_add_to_my_wishes(web_browser):
    page = Main_Page(web_browser)
    page.search_input.send_keys("чайник")
    page.search_btn.click()
    page.product_cards_searched.are_visible()
    page.first_product_card.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.scroll_down(300)
    page.like_button.click()
    assert page.log_in_register_window.are_visible()

#19-21 Переход по ссылкам подвала
def test_footer_policy(web_browser):
    page = Main_Page(web_browser)
    page.scroll_down()
    page.cookie_banner_close.click()
    page.footer_policy_link.click()
    assert page.policy_page.are_visible()

#20
def test_footer_siteMap(web_browser):
    page = Main_Page(web_browser)
    page.scroll_down()
    page.cookie_banner_close.click()
    page.footer_site_map_link.click()
    assert "https://aliexpress.ru/sitemap.html" in page.get_current_url()

#21
def test_footer_user_aggree(web_browser):
    page = Main_Page(web_browser)
    page.scroll_down()
    page.cookie_banner_close.click()
    page.footer_user_agreement_link.click()
    assert page.user_agreement.are_visible()