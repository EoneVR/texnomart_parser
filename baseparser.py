from bs4 import BeautifulSoup
import requests


class BaseParser:
    def __init__(self):
        self.url = 'https://texnomart.uz/ru/katalog/'
        self.host = 'https://texnomart.uz'

    def get_html(self, url=None):
        if url:
            return requests.get(url).text
        else:
            return requests.get(self.url).text

    def get_soup(self, html):
        return BeautifulSoup(html, 'html.parser')
