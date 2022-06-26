from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements
from selenium.webdriver.common.keys import Keys


class Main_Page(WebPage):

    def __init__(self, web_driver, url=''):
        url = "https://aliexpress.ru/"
        self._web_driver = web_driver
        notif_banner = '//div[@class="WebPush_WebPush__reject__1eiqb WebPush_WebPush__webpushBase__1eiqb"]'
        web_driver.get('chrome://settings/')
        web_driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.8);')
        self.get(url)

        web_driver.find_element_by_xpath(notif_banner).click()


    def get(self, url):
        self._web_driver.get(url)
        self.wait_page_loaded()

    main_menu_top = WebElement(xpath="//span[@class='TopHeadV2_TopHeadV2__wrapper__1c1dq']")
    categories_menu = WebElement(xpath='//a[@class="CategoriesMenu_styles__title__znldk"]')
    search_input = WebElement(name='SearchText')
    search_btn = WebElement(xpath='//button[@type="submit"]')
    logo = WebElement(class_name="Header_Logo__mainLogo__1gbu2")
    footer = WebElement(class_name="Footer_FooterNavigation__copyright__1atl6")
    welcome_block = WebElement(xpath="//div[contains(@class, 'IntroductionEntrance_WelcomeBlock__wrap__')]")
    carusel = WebElement(class_name="carousel_Carousel__pagesContainer__1jin61")
    product_cards = WebElement(xpath='//div[contains(@class, "Waterfall_ProductPreview__image__1comc")]')
    down_search_info = WebElement(xpath='//div[@class="SearchSeoInfo_SearchSeoInfo__seoInfo__16a10"]/p')
    age_check = WebElement(xpath='//span[contains(text(), "Я СТАРШЕ 18")]')
    searched_product_cards = ManyWebElements(xpath='//div[@class="SearchProductFeed_SearchProductFeed__productFeed__tznhm'
                                               '"]')
    #Главное меню
    sell_on_aliexpress = WebElement(xpath='//div[contains(text(), "Продавайте на AliExpress")]')
    cabinet_link = WebElement(link_text='Личный кабинет')
    become_seller = WebElement(link_text='Стать продавцом')
    help_menu = WebElement(xpath='//div[contains(text(), "Помощь")]')
    support_menu = WebElement(xpath='//li/a[contains(text(), "Служба поддержки")]')
    disputes_complaints = WebElement(xpath='//li/a[contains(text(), "Споры и жалобы")]')
    authors_rights = WebElement(xpath='//li/a[contains(text(), "Сообщить о нарушении авторских прав")]')
    customer_protection = WebElement(xpath='//div/a[contains(text(), "Защита Покупателя")]')
    application = WebElement(xpath='//a/span[contains(text(), "Приложение")]')
    destination_selector = WebElement(class_name='TopHeadV2_TopHeadV2__shipTo__1c1dq')
    lang_options = ManyWebElements(class_name="TopHeadV2_LangSwitcherForm__formSection__1q6pu")
    save_lang_opt_btn = WebElement(xpath='//button[contains(text(),"Сохранить")]')
    my_wishes = WebElement(xpath='//span[contains(text(),"Мои желания")]')
    my_profile = WebElement(xpath='//span[contains(text(),"Мой Профиль")]')
    regisrt_btn_main = WebElement(xpath='//div/div/div/button[contains(text(),"Регистрация") and contains(@class, '
                                        '"TopHeadV2_ProfileEntryBlock__button__156t9")]')
    footer_policy_link = WebElement(xpath="//a[@class='ali-kit_Base__base__104pa1 ali-kit_Base__accent__104pa1 ali-kit_L"
                                          "ink__link__cmgtoz ali-kit_Link__size-s__cmgtoz accent Footer_FooterNavigation"
                                          "__copyrightLink__1atl6' and contains(text(), 'Политика Конфиденциальности')]")
    footer_site_map_link = WebElement(xpath="//a[@class='ali-kit_Base__base__104pa1 ali-kit_Base__accent__104pa1 ali-kit_L"
                                          "ink__link__cmgtoz ali-kit_Link__size-s__cmgtoz accent Footer_FooterNavigation"
                                          "__copyrightLink__1atl6' and contains(text(), 'Карта сайта')]")
    footer_user_agreement_link = WebElement(xpath="//a[@class='ali-kit_Base__base__104pa1 ali-kit_Base__accent__104pa1 a"
                                                  "li-kit_Link__link__cmgtoz ali-kit_Link__size-s__cmgtoz accent Footer_"
                                                  "FooterNavigation__copyrightLink__1atl6' and contains(text(), "
                                                  "'Пользовательские соглашения')]")


    #Другие страницы
    product_cards_searched = ManyWebElements(class_name="product-snippet_ProductSnippet__name__tusfnx")
    buisness_logo = WebElement(xpath='//img[@class="header_logo__1Mpw-"]')
    open_shop = WebElement(xpath='//span[contains(text(), "Открыть магазин")]')
    help_instructions = WebElement(xpath="//h2[contains(text(), 'Инструкции')]")
    application_links = ManyWebElements(xpath='//a[@target="_blank"]')
    reg_by_email_link = WebElement(xpath='//span[contains(text(), "Зарегистрироваться по Email")]')
    first_product_card = WebElement(xpath='//div[@class="product-snippet_ProductSnippet__name__tusfnx"][1]')
    add_to_basket = WebElement(xpath='//button[contains(text(), "Добавить в корзину")]')
    basket_banner = WebElement(class_name="Product_CartPopupHeader__header__1lfjs")
    like_button = WebElement(class_name="Product_LikeButton__heart__eiubz")
    log_in_register_window = WebElement(xpath='//span[contains(text(), "Вход по номеру телефона")]')
    policy_page = WebElement(xpath='//h1[contains(text(), "Политика Конфиденциальности AliExpress")]')
    cookie_banner_close = WebElement(class_name="PrivacyPolicyBanner_PrivacyPolicyBanner__close__5dnwg")
    user_agreement = WebElement(xpath='//div[contains(text(), "Юридические документы")]')
    input_username = WebElement(id="fm-login-id")
    input_password = WebElement(id="fm-login-password")
    enter = WebElement(xpath='//button[contains(text(), "Войти")]')
    #Локаторы
    notif_banner = '//div[@class="WebPush_WebPush__reject__1eiqb WebPush_WebPush__webpushBase__1eiqb"]'
    my_profile_loc = '//span[contains(text(), "Мой Профиль")]'
    repistr_btn_main_loc='//div/div/div/button[contains(text(),"Регистрация") and contains(@class, ' \
                         '"TopHeadV2_ProfileEntryBlock__button__156t9")]'
    reg_by_email_link_loc = '//span[contains(text(), "Зарегистрироваться по Email")]'
    log_in_btn_main_loc = '//div/div/div/button[contains(text(),"Войти") and contains(@class, ' \
                           '"TopHeadV2_ProfileEntryBlock__button__156t9")]'
    log_in_by_phone_loc = '//span[contains(text(), "Вход по номеру телефона")]'
    my_orders_main_loc = '//a[contains(text(), "Мои заказы")]'
    mess_center_main_loc = '//a[contains(text(), "Центр сообщений")]'
    my_wishes_profile_main_loc = '//a[contains(text(), "Мои желания")]'
    favorite_shops_main_loc = '//a[contains(text(), "Любимые магазины")]'
    my_coupons_main_loc = '//a[contains(text(), "Мои купоны")]'
    get_coupons_main_loc = '//a[contains(text(), "Получить купоны")]'

