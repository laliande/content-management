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
    url = find_url_hamiltonwatch(art)
    req = Request(url)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")

    for key, value in result.items():
        try:
            if key == 'price':
                result['price'] = soup.body.find(
                    'span', attrs={'data-price-type': 'finalPrice'}).attrs['data-price-amount']
            elif key == 'caliber':
                result['caliber'] = soup.body.find(
                    'td', attrs={'data-th': 'Caliber'}).text
            elif key == 'coll':
                result['coll'] = soup.body.find('td', attrs={
                    'data-th': 'Коллекция'}).text
            elif key == 'mechanism':
                result['mechanism'] = soup.body.find(
                    'td', attrs={'data-th': 'Механизм'}).text
            elif key == 'diametr':
                result['diametr'] = soup.body.find(
                    'td', attrs={'data-th': 'Размеры корпуса'}).text
            elif key == 'colorDial':
                result['colorDial'] = soup.body.find(
                    'td', attrs={'data-th': 'Цвет циферблата'}).text
            elif key == 'corpus':
                result['corpus'] = soup.body.find(
                    'td', attrs={'data-th': 'Материал корпуса'}).text
            elif key == 'glass':
                result['glass'] = soup.body.find(
                    'td', attrs={'data-th': 'Стекло циферблата'}).text
            elif key == 'water':
                result['water'] = soup.body.find(
                    'td', attrs={'data-th': 'Водонепроницаемость'}).text
            elif key == 'colorWristlet':
                result['colorWristlet'] = soup.body.find(
                    'td', attrs={'data-th': 'Цвет ремешка'}).text
        except Exception as ex:
            print(ex)
            continue
    return result
