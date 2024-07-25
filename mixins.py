

class ProductDetailMixin:

    def get_detail(self, soup):
        detail = soup.find('div', class_='product__characteristic d-none d-block-1024').get_text()
        return detail
