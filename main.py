from baseparser import BaseParser
from database import DataBase
from time import time
from mixins import ProductDetailMixin


class TexnomartParser(BaseParser, ProductDetailMixin, DataBase):
    def __init__(self):
        BaseParser.__init__(self)
        ProductDetailMixin.__init__(self)
        DataBase.__init__(self)
        self.create_categories_table()
        self.create_products_table()

    def get_data(self):
        soup = self.get_soup(self.get_html())
        aside = soup.find('div', class_='content__wrap')
        categories = aside.find_all('div', class_='content__item')
        for category in categories:
            category_title = category.find('a').get_text(strip=True)
            print(category_title)
            self.save_category(category_title)
            category_link = self.host + category.find('a').get('href')
            print(category_link)
            self.products_page_parser(category_link, category_title)

    def products_page_parser(self, category_link, category_title):
        soup = self.get_soup(self.get_html(category_link))
        catalog = soup.find('div', class_='products-box')
        products = catalog.find_all('div', class_='col-3')
        category_id = self.get_category_id(category_title)
        for product in products:
            product_title = product.find('a',
                                         class_='product-name f-14 c-373 mb-1 768:mb-2 btn-link w-normal').get_text(
                strip=True)
            print(product_title)
            product_price_new = product.find('div', class_='product-price__current').get_text(strip=True)
            product_price_new = int(''.join([i for i in product_price_new if i.isdigit()]))
            print(product_price_new)
            product_link = self.host + product.find('a').get('href')
            print(product_link)
            product_soup = self.get_soup(self.get_html(product_link))
            detail = self.get_detail(product_soup)
            self.save_product(product_title=product_title,
                              product_detail=detail,
                              product_price=product_price_new,
                              product_link=product_link,
                              category_id=category_id)


def start_parsing():
    parser = TexnomartParser()
    start = time()
    parser.get_data()
    finish = time()
    print(f'Парсер отработал за {finish - start} секунд')


start_parsing()