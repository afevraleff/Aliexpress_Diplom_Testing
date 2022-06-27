import time
import pytest
from pages.base import WebPage
from pages.main_page import Main_Page
from pages.elements import WebElement
from selenium.webdriver import ActionChains


#1 Наличие основных элементов на  главной странице
def test_start_page_main_elements(web_browser):
    page = Main_Page(web_browser)
    assert page.main_menu_top.is_visible()
    assert page.categories_menu.is_visible()
    assert page.search_input.is_clickable()
    assert page.logo.is_visible()
    assert page.welcome_block.is_visible()
    assert page.carusel.is_visible()
    assert page.product_cards.is_visible()
    assert page.footer.is_visible()

#2 Переходы по главным ссылкам меню категории
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

#3-15 Ссылки главного меню
def test_main_menu_cabinet(web_browser):
    page = Main_Page(web_browser)
    page.sell_on_aliexpress.click()
    page.cabinet_link.click()
    assert page.buisness_logo.is_visible()

#4 Стать продавцом
def test_main_become_seller(web_browser):
    page = Main_Page(web_browser)
    page.sell_on_aliexpress.click()
    page.become_seller.click()
    assert page.open_shop.is_visible()

#5 Помощь
def test_main_support(web_browser):
    page = Main_Page(web_browser)
    page.help_menu.click()
    page.support_menu.click()
    assert page.help_instructions.is_visible()

#6 Споры и жалобы
def test_main_disputes_complains(web_browser):
    page = Main_Page(web_browser)
    page.help_menu.click()
    page.disputes_complaints.click()
    assert "https://login.aliexpress.com" in page.get_current_url()

#7 Сообщить о нарушении авторских прав
def test_main_authors_rights(web_browser):
    page = Main_Page(web_browser)
    page.help_menu.click()
    page.authors_rights.click()
    assert "https://ipp.alibabagroup.com/" in page.get_current_url()

#8 Защита покупателя
def test_main_customer_protection(web_browser):
    page = Main_Page(web_browser)
    page.customer_protection.click()
    assert "https://ru.aliexpress.com/p/buyerprotection/" in page.get_current_url()


#9 Приложения
def test_main_application(web_browser):
    page = Main_Page(web_browser)
    page.application.click()
    assert page.application_links.is_visible()

#10 Селектор язык
def test_main_lang_selector(web_browser):
    page = Main_Page(web_browser)
    page.destination_selector.click()
    assert page.lang_options.is_visible()
    assert page.save_lang_opt_btn.is_visible()

# 11 Мои желания
def test_main_my_wishes(web_browser):
    page = Main_Page(web_browser)
    page.my_wishes.click()
    assert 'https://login.aliexpress.ru/' in page.get_current_url()

# 12 Ссылка Мой профиль
def test_main_my_profile(web_browser):
    page = Main_Page(web_browser)
    page.my_profile.click()
    assert 'https://login.aliexpress.ru/' in page.get_current_url()

# 13 Регистрация на сайте  через меню Мой профиль
def test_main_my_profile_menu_reg(web_browser):
    web_browser.get("https://aliexpress.ru/")
    web_browser.find_element_by_xpath(Main_Page.notif_banner).click()
    hoverable = web_browser.find_element_by_xpath(Main_Page.my_profile_loc)
    button_reg = web_browser.find_element_by_xpath(Main_Page.repistr_btn_main_loc)
    ActionChains(web_browser).move_to_element(hoverable).click(button_reg).perform()
    assert web_browser.find_element_by_xpath(Main_Page.reg_by_email_link_loc).is_displayed()

# 14 Вход на сайт через меню Мой профиль
def test_main_my_profile_menu_log_in(web_browser):
    web_browser.get("https://aliexpress.ru/")
    web_browser.find_element_by_xpath(Main_Page.notif_banner).click()
    hoverable = web_browser.find_element_by_xpath(Main_Page.my_profile_loc)
    button_log_in = web_browser.find_element_by_xpath(Main_Page.log_in_btn_main_loc)
    ActionChains(web_browser).move_to_element(hoverable).click(button_log_in).perform()
    assert web_browser.find_element_by_xpath(Main_Page.log_in_by_phone_loc).is_displayed()

#15 Меню Мой профиль
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
    page.product_cards_searched.is_visible()
    for elem in page.product_cards_searched.get_text():
        assert 'чайник' or 'Чайник' in elem

#17 Добавление товара в корзину без авторизции
def test_add_to_basket(web_browser):
    page = Main_Page(web_browser)
    page.search_input.send_keys("чайник")
    page.search_btn.click()
    page.product_cards_searched.is_visible()
    page.first_product_card.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.scroll_down(300)
    page.add_to_basket.click()
    page.wait_page_loaded()
    assert page.basket_banner.is_visible()

#18 Добавление товара в Мои желания без авторизции
def test_add_to_my_wishes(web_browser):
    page = Main_Page(web_browser)
    page.search_input.send_keys("чайник")
    page.search_btn.click()
    page.product_cards_searched.is_visible()
    page.first_product_card.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.scroll_down(300)
    page.like_button.click()
    assert page.log_in_register_window_enter_by_phone.is_visible()


#19-23 Ссылки внизу страницы сразу над подвалом
#19 Навигация по Aliexpress
@pytest.mark.parametrize('locator', ["Служба поддержки", "Споры и жалобы", "Защита Покупателя" ,
                                     "Сообщить о нарушении авторских прав", "Пользовательские соглашения",
                                     "Блог для покупателей", "Купоны AliExpress"])
def test_navigation_links(web_browser, locator):
    web_browser.get("https://aliexpress.ru/")
    web_browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    web_browser.find_element_by_link_text(locator).click()

@pytest.mark.parametrize('locator', ['Популярное', 'Кабинет продавца', 'ЧЕРНАЯ ПЯТНИЦА', 'Распродажа 11.11',
                                     'Коронавирус'])
#20 Категории товаров
def test_goods_categories_links(web_browser, locator):
    web_browser.get("https://aliexpress.ru/")
    web_browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    web_browser.find_element_by_link_text(locator).click()

#21 Категории товаров, Tmall
def test_goods_categories_tmall_link(web_browser):
    page = Main_Page(web_browser)
    page.scroll_down()
    page.tmall_link_goods_categories.click()

#22 Aliexpress на других языках
@pytest.mark.parametrize('locator', ['Русский', 'Португальский', 'Испанский', 'Французский', 'Немецкий', 'Итальянский',
                                     'Нидерландский', 'Турецкий', 'Японский', 'Корейский', 'Тайский язык',
                                     'Вьетнамский', 'Арабский', 'Иврит', 'Польский'])

def test_Ali_languages_links(web_browser, locator):
    web_browser.get("https://aliexpress.ru/")
    web_browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    web_browser.find_element_by_link_text(locator).click()

#23 Группа компаний Alibaba
@pytest.mark.parametrize('locator', ['Работа в AliExpress', 'Сайт Alibaba Group', 'AliExpress', 'Alimama', 'Alipay',
                                     'Fliggy', 'Alibaba Cloud', 'Alibaba International', 'AliTelecom', 'DingTalk',
                                     'Juhuasuan', 'Taobao Marketplace', 'Xiami', 'AliOS', '1688', 'Lazada Indonesia',
                                     'Lazada Thailand', 'Lazada Malaysia', 'Lazada Philippines', 'Lazada Singapore',
                                     'Lazada Vietnam'])

def test_Ali_languages_links(web_browser, locator):
    web_browser.get("https://aliexpress.ru/")
    web_browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    web_browser.find_element_by_link_text(locator).click()

#24-27 Кнопки социальных сетей
#24 Twitter
def test_twitter_btn(web_browser):
    page = Main_Page(web_browser)
    page.scroll_down()
    twitter_btn = page.social_btn.__getitem__(0)
    twitter_btn.click()
    page.wait_page_loaded()
    assert "https://twitter.com/aliexpress" in page.get_current_url()

#25 VK
def test_vk_btn(web_browser):
    page = Main_Page(web_browser)
    page.scroll_down()
    vk_btn = page.social_btn.__getitem__(1)
    vk_btn.click()
    page.wait_page_loaded()
    assert "https://vk.com/aliexpress" in page.get_current_url()

#26 Одноклассники
def test_ok_btn(web_browser):
    page = Main_Page(web_browser)
    page.scroll_down()
    ok_btn = page.social_btn.__getitem__(2)
    ok_btn.click()
    page.wait_page_loaded()
    assert "https://ok.ru/aliexpress" in page.get_current_url()

#27 Youtube
def test_youtube_btn(web_browser):
    page = Main_Page(web_browser)
    page.scroll_down()
    youtube_btn = page.social_btn.__getitem__(3)
    youtube_btn.click()
    page.wait_page_loaded()
    assert "https://www.youtube.com/channel/UChQr9A5-7MdpypJwxDGLKMQ" in page.get_current_url()

#27-29 Переход по ссылкам подвала
#27 Политика конфиденциальности
def test_footer_policy(web_browser):
    page = Main_Page(web_browser)
    page.scroll_down()
    page.cookie_banner_close.click()
    page.footer_policy_link.click()
    assert page.policy_page.is_visible()

#28 Карта сайта
def test_footer_siteMap(web_browser):
    page = Main_Page(web_browser)
    page.scroll_down()
    page.cookie_banner_close.click()
    page.footer_site_map_link.click()
    assert "https://aliexpress.ru/sitemap.html" in page.get_current_url()

#29 Пользовательское соглашение
def test_footer_user_aggree(web_browser):
    page = Main_Page(web_browser)
    page.scroll_down()
    page.cookie_banner_close.click()
    page.footer_user_agreement_link.click()
    assert page.user_agreement.is_visible()

#30-36 Форма войти/зарегистрироваться.
# Вход через соцсети
#30 VK
def test_register_main_vk_enter(web_browser):
    page = Main_Page(web_browser)
    page.regisrt_btn_main_page.click()
    vk_btn = page.social_enter_links.__getitem__(0)
    vk_btn.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.wait_page_loaded()
    assert "https://oauth.vk.com/" in page.get_current_url()

#31 OK
def test_register_main_ok_enter(web_browser):
    page = Main_Page(web_browser)
    page.regisrt_btn_main_page.click()
    ok_btn = page.social_enter_links.__getitem__(1)
    ok_btn.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.wait_page_loaded()
    assert "https://connect.ok.ru/" in page.get_current_url()

#32 apple
def test_register_main_apple_enter(web_browser):
    page = Main_Page(web_browser)
    page.regisrt_btn_main_page.click()
    apple_btn = page.social_enter_links.__getitem__(2)
    apple_btn.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.wait_page_loaded()
    assert "https://appleid.apple.com/" in page.get_current_url()

#33 Google
def test_register_main_google_enter(web_browser):
    page = Main_Page(web_browser)
    page.regisrt_btn_main_page.click()
    google_btn = page.social_enter_links.__getitem__(3)
    google_btn.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.wait_page_loaded()
    assert "https://accounts.google.com/" in page.get_current_url()

#34 Регистрация с валидным номером телефона
def test_register_main_valid_phone(web_browser):
    page = Main_Page(web_browser)
    page.regisrt_btn_main_page.click()
    page.input_phone.send_keys("9777543210")
    page.send_sms_btn.click()
    page.wait_page_loaded()
    assert page.sms_code_window.is_visible()

#35 Ссылка Забыли пароль
def test_password_repair_link(web_browser):
    page = Main_Page(web_browser)
    enter = page.enter_btn_main_page.__getitem__(1)
    enter.click()
    page.wait_page_loaded()
    page.forgotten_password_link.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.wait_page_loaded()
    assert page.repair_password.is_visible()

#36 Ссылка Рассказываем что делать, если вход через соцсети не работает
def test_if_soc_net_doesnt_work_link(web_browser):
    page = Main_Page(web_browser)
    enter = page.enter_btn_main_page.__getitem__(1)
    enter.click()
    page.wait_page_loaded()
    page.what_to_do_link.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.wait_page_loaded()
    assert page.what_to_do_header.is_visible()
