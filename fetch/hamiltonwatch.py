import os
import csv
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def find_url_hamiltonwatch(art: str) -> str:
    ''' Description: finds the url on the site by article
        Input: article
        Output: desired url

    '''
    url = 'https://www.hamiltonwatch.com/ru-ru/catalogsearch/result/?q={}'.format(
        art)
    req = Request(url)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")
    product_item_link = soup.find(
        'a', attrs={'class': 'product-item-link'}).attrs['href']
    return product_item_link


def fetch_hamiltonwatch(art: str) -> dict:
    ''' Description: parses data and returns it in the format of the publication
        Input: article
        Output: product details

    '''
    result = {'vendor': '', 'coll': '',
              'seoSuffix': '', 'article': art, 'sex': '', 'mechanism': '', 'diametr': '',
              'thicknes': '', 'corpus': '', 'glass': '', 'braslet': '', 'water': '', 'function': '',
              'dopoform_fake': '', 'dopoform': '', 'form': '', 'caliber': '', 'colorDial': '', 'colorWristlet': '',
              'exit': '', 'price': '', 'youtube': '', 'id': '', 'update': ''}

    try:
        url = find_url_hamiltonwatch(art)
        req = Request(url)
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "lxml")
        result['price'] = soup.body.find(
            'span', attrs={'data-price-type': 'finalPrice'}).attrs['data-price-amount']
        result['caliber'] = soup.body.find(
            'td', attrs={'data-th': 'Caliber'}).text
        result['coll'] = soup.body.find('td', attrs={
            'data-th': 'Коллекция'}).text
        result['mechanism'] = soup.body.find(
            'td', attrs={'data-th': 'Механизм'}).text
        result['diametr'] = soup.body.find(
            'td', attrs={'data-th': 'Размеры корпуса'}).text
        result['colorDial'] = soup.body.find(
            'td', attrs={'data-th': 'Цвет циферблата'}).text
        result['corpus'] = soup.body.find(
            'td', attrs={'data-th': 'Материал корпуса'}).text
        result['glass'] = soup.body.find(
            'td', attrs={'data-th': 'Стекло циферблата'}).text
        result['water'] = soup.body.find(
            'td', attrs={'data-th': 'Водонепроницаемость'}).text
        result['colorWristlet'] = soup.body.find(
            'td', attrs={'data-th': 'Цвет ремешка'}).text
    except Exception as ex:
        print(ex)
    finally:
        return result


def write_hamiltonwatch() -> None:
    ''' Description: writes data to a file for return
        Output: None

    '''
    len_output = os.path.getsize(
        'fetch/output/output_hamiltonwatch.csv')
    headers = False
    if len_output == 0:
        headers = True
    with open('fetch/input/input_hamiltonwatch.csv', 'r', encoding='utf-8') as csvinput:
        with open('fetch/output/output_hamiltonwatch.csv', 'a', encoding='utf-8') as csvoutput:
            reader = csv.reader(csvinput)
            for row in reader:
                if row[0] != 'article':
                    data = fetch_hamiltonwatch(row[0])
                    writer = csv.DictWriter(csvoutput, fieldnames=data)
                    if headers:
                        headers = False
                        writer.writeheader()
                    writer.writerow(data)
