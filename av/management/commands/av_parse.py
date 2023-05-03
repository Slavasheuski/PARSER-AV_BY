from django.core.management.base import BaseCommand
from av.models import Product

import requests
from bs4 import BeautifulSoup

import datetime
from collections import namedtuple

InnerBlock = namedtuple('Block', 'marka,model,price,year,url')

class Block(InnerBlock):

    def __str__(self):
        return f'{self.marka}\t\t{self.model}\t\t{self.price}\t\t{self.year}\t\t{self.url}'


class AVParser:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,tr;q=0.6',
        }

    def get_page(self, page = None):
        params = {
            'year[min]': 2018,
            'year[max]': 2020,
            'seller_type[0]': 1,
        }
        if page and page > 1:
            params['page'] = page

        url = 'https://cars.av.by/filter'
        r = self.session.get(url, params = params)
        return r.text


    def parse_block(self, item):
        url_block = item.select_one('a.listing-item__link')
        href = url_block.get('href')
        if href:
            url = 'https://cars.av.by' + href
        else:
            url = None
            
        model = ' '.join(item.find('span', class_ = 'link-text').text.strip().split(' ')[1:])
        marka = item.find('span', class_ = 'link-text').text.strip().split(' ')[0]
        price = int(''.join(item.find('div', class_ = 'listing-item__priceusd').text.strip().split())[1:-1])
        year = int(item.find('div', class_ = 'listing-item__params').text.strip()[:4])


        lot = Block(
            marka = marka,
            model = model,
            price = price,
            year = year,
            url = url
        )

        #Проверяем, нет ли такого объявления, если есть, обновляем его, если нет - добавляем
        try:
            p = Product.objects.get(url=url)
            p.marka = marka
            p.model = model
            p.price = price
            p.year = year
            p.url = url
            p.save()
            print(f'product {p}')

        except Product.DoesNotExist:
            p = Product(
                marka = marka,
                model = model,
                price = price,
                year = year,
                url = url
            ).save()
            print(f'product {p}')

    #Парсим данные
    def get_blocks(self, page=None):
        text = self.get_page(page=page)
        soup = BeautifulSoup(text, 'lxml')
        
        container = soup.find_all('div', class_='listing-item__wrap')
        for item in container:
            block = self.parse_block(item = item)

    #Парсим данные со всех страниц
    def parse_all(self):
        limit = 500
        for i in range(1, limit + 1):
            self.get_blocks(page = i)


class Command(BaseCommand):
    help = 'Парсинг AV.by'

    def handle(self, *args, **kwargs): 
        p = AVParser()
        p.parse_all()