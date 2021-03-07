from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from config import log



def find_url_hamiltonwatch(art: str) -> str:
    ''' Description: finds the url on the site by article
        Input: article
        Output: desired url

    '''
    url = 'https://www.hamiltonwatch.com/ru-ru/catalogsearch/result/?q={}'.format(
        art)
    log.debug('Hamiltonwatch find url is ' + url)
    req = Request(url)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")
    product_item_link = soup.find(
        'a', attrs={'class': 'product-item-link'}).attrs['href']
    log.debug('Hamiltoneatch priduct item link is ' + product_item_link )
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
    except Exception as ex:
        log.error(ex)
        print(ex)
    for key, value in result.items():
        try:
            if key == 'price':
                result['price'] = soup.body.find(
                    'span', attrs={'data-price-type': 'finalPrice'}).attrs['data-price-amount']
                log.debug('Hamiltonwatch price for article ' + art + ' is ' + result['price'])
            elif key == 'caliber':
                result['caliber'] = soup.body.find(
                    'td', attrs={'data-th': 'Caliber'}).text
                log.debug('Hamiltonwatch caliber for article ' + art + ' is ' + result['caliber'])
            elif key == 'seoSuffix':
                result['seoSuffix'] = soup.body.find(
                    'span', attrs={'data-ui-id': 'page-title-wrapper'}).text
                log.debug('Hamiltonwatch seoSuffix for article ' + art + ' is ' + result['seoSuffix'])
            elif key == 'dopoform':
                result['dopoform'] = soup.body.find(
                    'div', attrs={'class': 'value'}).text
                log.debug('Hamiltonwatch dopoform for article ' + art + ' is ' + result['dopoform'])
            elif key == 'coll':
                result['coll'] = soup.body.find('td', attrs={
                    'data-th': 'Коллекция'}).text
                log.debug('Hamiltonwatch coll for article ' + art + ' is ' + result['coll'])
            elif key == 'braslet':
                result['braslet'] = soup.body.find('td', attrs={
                    'data-th': 'Тип ремешка'}).text
                log.debug('Hamiltonwatch braslet for article ' + art + ' is ' + result['braslet'])
            elif key == 'sex':
                result['sex'] = soup.body.find('td', attrs={
                    'data-th': 'Пол'}).text
                log.debug('Hamiltonwatch sex for article ' + art + ' is ' + result['sex'])
            elif key == 'function':
                result['function'] = soup.body.find('td', attrs={
                    'data-th': 'Запас хода'}).text
                log.debug('Hamiltonwatch functuion for article ' + art + ' is ' + result['function'])
            elif key == 'mechanism':
                result['mechanism'] = soup.body.find(
                    'td', attrs={'data-th': 'Механизм'}).text
                log.debug('Hamiltonwatch mechanism for article ' + art + ' is ' + result['mechanism'])
            elif key == 'diametr':
                result['diametr'] = soup.body.find(
                    'td', attrs={'data-th': 'Размеры корпуса'}).text
                log.debug('Hamiltonwatch diametr for article ' + art + ' is ' + result['diametr'])
            elif key == 'colorDial':
                result['colorDial'] = soup.body.find(
                    'td', attrs={'data-th': 'Цвет циферблата'}).text
                log.debug('Hamiltonwatch colorDial for article ' + art + ' is ' + result['colorDial'])
            elif key == 'corpus':
                result['corpus'] = soup.body.find(
                    'td', attrs={'data-th': 'Материал корпуса'}).text
                log.debug('Hamiltonwatch corpus for article ' + art + ' is ' + result['corpus'])
            elif key == 'glass':
                result['glass'] = soup.body.find(
                    'td', attrs={'data-th': 'Стекло циферблата'}).text
                log.debug('Hamiltonwatch glass for article ' + art + ' is ' + result['glass'])
            elif key == 'water':
                result['water'] = soup.body.find(
                    'td', attrs={'data-th': 'Водонепроницаемость'}).text
                log.debug('Hamiltonwatch water for article ' + art + ' is ' + result['water'])
            elif key == 'colorWristlet':
                result['colorWristlet'] = soup.body.find(
                    'td', attrs={'data-th': 'Цвет ремешка'}).text
                log.debug('Hamiltonwatch colorWristlet for article ' + art + ' is ' + result['colorWristlet'])
        except Exception as ex:
            log.error(ex)
            print(ex)
            continue
    return result
