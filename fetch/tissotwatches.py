from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
from googleapiclient.discovery import build

autorization_data = {
"api_key": "AIzaSyANUOyyWbw-mnsCHM15HerBlk2tsMtRQdQ",
"cse_id": "ea5b078f2fc0024f0"}

def find_url_tissotwatches(art: str) -> str:
    ''' Description: finds the url on the site by article
        Input: article
        Output: desired url

    '''
    search_term = "{} site:https://www.tissotwatches.com/ru-ru/".format(art)
    service = build("customsearch", "v1", developerKey=autorization_data["api_key"])
    res = service.cse().list(q=search_term, cx=autorization_data["cse_id"]).execute()
    return res['items'][0]['link']

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
    log.debug('Tissot bad price is ' + bad_price)
    log.debug('Tissot good price is ' + result)
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
    log.debug('Tissot bad article is ' + bad_article)
    log.debug('Tissot good article is ' + result)
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
        log.warning('Tissot clock not found!')
        return result
    req = Request(url)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")
    for key, value in result.items():
        try:
            if key == 'price':
                result['price'] = find_price(soup.body.find(
                    'span', attrs={'class': 'product-price'}).text)
                log.debug('Tissot price for article ' + art + 'is '+  result['price'])
            elif key == 'vendor':
                result['vendor'] = 'Tissot'
                log.debug('Tissot vendor for article ' + art + 'is ' + result['vendor'])
            elif key == 'article':
                result['article'] = find_article(soup.body.find(
                    'p', attrs={'class': 'product-sku'}).text)
                log.debug('Tissot article for article ' + art + 'is ' + result['article'])
            elif key == 'caliber':
                result['caliber'] = soup.body.find(
                    'h4', text='Модель').find_next_siblings()[0].text
                log.debug('Tissot caliber for article ' + art + 'is ' + result['caliber'])
            elif key == 'sex':
                result['sex'] = soup.body.find(
                    'h4', text='Пол').find_next_siblings()[0].text
                log.debug('Tissot sex for article ' + art + 'is ' + result['sex'])
            elif key == 'diametr':
                result['diametr'] = soup.body.find(
                    'h4', text='Длина').find_next_siblings()[0].text
                log.debug('Tissot diametr for article ' + art + 'is ' + result['diametr'])
            elif key == 'coll':
                result['coll'] = soup.body.find(
                    'h4', text='Коллекция').find_next_siblings()[0].text
                log.debug('Tissot collection for article ' + art + 'is ' + result['coll'])
            elif key == 'mechanism':
                result['mechanism'] = soup.body.find(
                    'h4', text='Механизм').find_next_siblings()[0].text
                log.debug('Tissot mechanism for article ' + art + 'is ' + result['mechanism'])
            elif key == 'colorDial':
                result['colorDial'] = soup.body.find(
                    'h4', text='Цвет циферблата').find_next_siblings()[0].text
                log.debug('Tissot color dial for article ' + art + 'is ' + result['colorDial'])
            elif key == 'corpus':
                result['corpus'] = soup.body.find(
                    'h4', text='Материал корпуса').find_next_siblings()[0].text
                log.debug('Tissot corpus for article ' + art + 'is ' + result['corpus'])
            elif key == 'glass':
                result['glass'] = soup.body.find(
                    'h4', text='Стекло').find_next_siblings()[0].text
                log.debug('Tissot glass for article ' + art + 'is ' + result['glass'])
            elif key == 'water':
                result['water'] = soup.body.find(
                    'h4', text='Водонепроницаемость').find_next_siblings()[0].text
                log.debug('Tissot water for article ' + art + 'is ' + result['water'])
            elif key == 'colorWristlet':
                result['colorWristlet'] = soup.body.find(
                    'h4', text='Цвет ремешка/браслета').find_next_siblings()[0].text
                log.debug('Tissot color wristlet for article ' + art + 'is ' + result['colorWristlet'])
            elif key == 'thicknes':
                result['thicknes'] = soup.body.find(
                    'h4', text='Толщина').find_next_siblings()[0].text
                log.debug('Tissot thicknes for article ' + art + 'is ' + result['thicknes'])
            elif key == 'braslet':
                result['braslet'] = soup.body.find(
                    'h4', text='Оформление ремешка/браслета').find_next_siblings()[0].text
                log.debug('Tissot braslet for article ' + art + 'is ' + result['braslet'])
            elif key == 'form':
                result['form'] = soup.body.find(
                    'h4', text='Форма корпуса').find_next_siblings()[0].text
                log.debug('Tissot form for article ' + art + 'is ' + result['form'])
            elif key == 'seoSuffix':
                result['seoSuffix'] = soup.body.find(
                    'div', attrs={'class': 'reserve-product'}).text
                log.debug('Tissot seo suffix for article ' + art + 'is ' + result['seoSuffix'])
        except Exception as ex:
            log.error(ex)
            print(ex)
            continue
    return result
