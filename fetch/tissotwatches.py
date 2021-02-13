from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests


def find_url_tissotwatches(art: str) -> str:
    ''' Description: finds the url on the site by article
        Input: article
        Output: desired url

    '''
    url = 'https://www.tissotwatches.com/ru-ru/shop/{}.html'.format(art)
    if requests.get(url).history:
        url = 'https://www.tissotwatches.com/ru-ru/shop/catalogsearch/result/?q={}'.format(
            art)
        if requests.get(url).history:
            return None
        req = requests.get(url)
        req = Request(url)
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "lxml")
        product_item_link = soup.find(
            'a', attrs={'class': 'product-thumbnail product-item-link'}).attrs
        return product_item_link['href']
    return url


def find_price(bad_price: str):
    ''' Description: clean price
        Input: bad price
        Output: price
    '''

    result = ''
    for symbol in bad_price:
        try:
            int(symbol)
            result += symbol
        except Exception as ex:
            pass
    return result


def find_article(bad_article: str):
    ''' Description: clean article
        Input: bad article
        Output: article

    '''
    result = ''
    for symbol in bad_article:
        if symbol != ' ' and symbol != '\n':
            result += symbol
    return result


def fetch_tissotwatches(art: str) -> dict:
    ''' Description: parses data and returns it in the format of the publication
        Input: article
        Output: product details

    '''
    result = {'vendor': '', 'coll': '',
              'seoSuffix': '', 'article': '', 'sex': '', 'mechanism': '', 'diametr': '',
              'thicknes': '', 'corpus': '', 'glass': '', 'braslet': '', 'water': '', 'function': '',
              'dopoform_fake': '', 'dopoform': '', 'form': '', 'caliber': '', 'colorDial': '', 'colorWristlet': '',
              'exit': '', 'price': '', 'youtube': '', 'id': '', 'update': ''}
    url = find_url_tissotwatches(art)
    if url is None:
        return result
    req = Request(url)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")
    for key, value in result.items():
        try:
            if key == 'price':
                result['price'] = find_price(soup.body.find(
                    'span', attrs={'class': 'product-price'}).text)
            elif key == 'vendor':
                result['vendor'] = 'Tissot'
            elif key == 'article':
                result['article'] = find_article(soup.body.find(
                    'p', attrs={'class': 'product-sku'}).text)
            elif key == 'caliber':
                result['caliber'] = soup.body.find(
                    'h4', text='Модель').find_next_siblings()[0].text
            elif key == 'sex':
                result['sex'] = soup.body.find(
                    'h4', text='Пол').find_next_siblings()[0].text
            elif key == 'diametr':
                result['diametr'] = soup.body.find(
                    'h4', text='Длина').find_next_siblings()[0].text
            elif key == 'coll':
                result['coll'] = soup.body.find(
                    'h4', text='Коллекция').find_next_siblings()[0].text
            elif key == 'mechanism':
                result['mechanism'] = soup.body.find(
                    'h4', text='Механизм').find_next_siblings()[0].text
            elif key == 'colorDial':
                result['colorDial'] = soup.body.find(
                    'h4', text='Цвет циферблата').find_next_siblings()[0].text
            elif key == 'corpus':
                result['corpus'] = soup.body.find(
                    'h4', text='Материал корпуса').find_next_siblings()[0].text
            elif key == 'glass':
                result['glass'] = soup.body.find(
                    'h4', text='Стекло').find_next_siblings()[0].text
            elif key == 'water':
                result['water'] = soup.body.find(
                    'h4', text='Водонепроницаемость').find_next_siblings()[0].text
            elif key == 'colorWristlet':
                result['colorWristlet'] = soup.body.find(
                    'h4', text='Цвет ремешка/браслета').find_next_siblings()[0].text
            elif key == 'thicknes':
                result['thicknes'] = soup.body.find(
                    'h4', text='Толщина').find_next_siblings()[0].text
            elif key == 'braslet':
                result['braslet'] = soup.body.find(
                    'h4', text='Оформление ремешка/браслета').find_next_siblings()[0].text
            elif key == 'form':
                result['form'] = soup.body.find(
                    'h4', text='Форма корпуса').find_next_siblings()[0].text
            elif key == 'seoSuffix':
                result['seoSuffix'] = soup.body.find(
                    'div', attrs={'class': 'reserve-product'}).text
        except Exception as ex:
            print(ex)
            continue
    return result
