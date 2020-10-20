from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def find_url_tissotwatches(art: str) -> str:
    ''' Description: finds the url on the site by article
        Input: article
        Output: desired url

    '''
    url = 'https://www.tissotwatches.com/ru-ru/shop/catalogsearch/result/?q={}'.format(
        art)
    req = Request(url)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")
    try:
        not_found = soup.find(
            'p', attrs={'class': 'collection-header__message'}).text
        if 'По вашему запросу ничего не найдено.' in not_found:
            return 'fail'
    except:
        pass
    product_item_link = soup.find(
        'a', attrs={'class': 'product-thumbnail product-item-link'}).attrs
    return product_item_link['href']


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

    try:
        url = find_url_tissotwatches(art)
        if url == 'fail':
            return result
        req = Request(url)
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "lxml")
        result['vendor'] = 'Tissot'
        result['price'] = find_price(soup.body.find(
            'span', attrs={'class': 'product-price'}).text)
        result['article'] = find_article(soup.body.find(
            'p', attrs={'class': 'product-sku'}).text)
        result['caliber'] = soup.body.find(
            'h4', text='Модель').find_next_siblings()[0].text
        result['coll'] = soup.body.find(
            'h4', text='Коллекция').find_next_siblings()[0].text
        result['mechanism'] = soup.body.find(
            'h4', text='Механизм').find_next_siblings()[0].text
        # result['diametr'] = soup.body.find(
        #     'td', attrs={'data-th': 'Размеры корпуса'}).text
        result['colorDial'] = soup.body.find(
            'h4', text='Цвет циферблата').find_next_siblings()[0].text
        result['corpus'] = soup.body.find(
            'h4', text='Материал корпуса').find_next_siblings()[0].text
        result['glass'] = soup.body.find(
            'h4', text='Стекло').find_next_siblings()[0].text
        result['water'] = soup.body.find(
            'h4', text='Водонепроницаемость').find_next_siblings()[0].text
        result['colorWristlet'] = soup.body.find(
            'h4', text='Цвет ремешка/браслета').find_next_siblings()[0].text
        result['thicknes'] = soup.body.find(
            'h4', text='Толщина').find_next_siblings()[0].text
        result['braslet'] = soup.body.find(
            'h4', text='Оформление ремешка/браслета').find_next_siblings()[0].text
        result['form'] = soup.body.find(
            'h4', text='Форма корпуса').find_next_siblings()[0].text
        result['seoSuffix'] = soup.body.find(
            'div', attrs={'class': 'reserve-product'}).text
    except Exception as ex:
        print(ex)
    finally:
        return result
