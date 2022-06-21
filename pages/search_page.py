from pages.base import WebPage
from pages.elements import  WebElement
class Search_Page(WebPage):
    category_search_header = WebElement(xpath='//h1[@class="SearchBreadcrumbs_SearchBreadcrumbs__category__b61od"]')