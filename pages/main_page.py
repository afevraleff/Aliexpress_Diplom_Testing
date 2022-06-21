from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements
from selenium.webdriver.common.keys import Keys


class Main_Page(WebPage):

    def __init__(self, web_driver, url=''):
        url = "https://aliexpress.ru/"
        self._web_driver = web_driver
        web_driver.get('chrome://settings/')
        web_driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.8);')
        self.get(url)
        web_driver.find_element_by_xpath('//div[@class="WebPush_WebPush__reject__1eiqb WebPush_WebPush__webpushBase__1'
                                         'eiqb"]').click()
        web_driver.maximize_window()

    def get(self, url):
        self._web_driver.get(url)
        self.wait_page_loaded()

    main_menu_top = WebElement(xpath="//span[@class='TopHeadV2_TopHeadV2__wrapper__1c1dq']")
    categories_menu = WebElement(xpath='//a[@class="CategoriesMenu_styles__title__znldk"]')
    search_input = WebElement(name="SearchText")
    search_btn = WebElement(xpath='//button[@type="submit"]')
    logo = WebElement(class_name="Header_Logo__mainLogo__1gbu2")
    footer = WebElement(class_name="Footer_FooterNavigation__copyright__1atl6")
    welcome_block = WebElement(xpath="//div[contains(@class, 'IntroductionEntrance_WelcomeBlock__wrap__')]")
    carusel = WebElement(class_name="carousel_Carousel__pagesContainer__1jin61")
    product_cards = WebElement(xpath='//div[contains(@class, "Waterfall_ProductPreview__image__1comc")]')
    down_search_info = WebElement(xpath='//div[@class="SearchSeoInfo_SearchSeoInfo__seoInfo__16a10"]/p')
    age_check = WebElement(xpath='//span[contains(text(), "Я СТАРШЕ 18")]')
    searched_product_cards = WebElement(xpath='//div[@class="SearchProductFeed_SearchProductFeed__productFeed__tznhm'
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


    #Другие страницы
    buisness_logo = WebElement(xpath='//img[@class="header_logo__1Mpw-"]')
    open_shop = WebElement(xpath='//span[contains(text(), "Открыть магазин")]')
    help_instructions = WebElement(xpath="//h2[contains(text(), 'Инструкции')]")
    application_links = ManyWebElements(xpath='//a[@target="_blank"]')
