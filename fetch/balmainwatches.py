from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def get_product_link(art:str) -> str:
    ''' Description: finds the url on the site by article
        Input: article
        Output: desired url
    '''
    url = 'https://www.balmainwatches.com/ru/catalogsearch/result/?q={}'.format(art)
    req = Request(url)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")
    product_item_link = soup.find(
        'a', attrs={'class': 'product-item-link'}).attrs['href']
    print(product_item_link)
    result = ''
    for sym in product_item_link:
        if sym == ' ':
            result += '%20'
        else:
            result += sym
    return result

def get_params(soup, result):
    labels = soup.findAll('th', attrs={'class': 'col label'})
    for label in labels:
        if label.text == 'Пол':
            result['sex'] = label.find_next().text
        elif label.text == 'Механизм':
            result['mechanism'] = label.find_next().text
        elif label.text == 'Диаметр (мм)':
            result['diametr'] = label.find_next().text
        elif label.text == 'Корпус':
            result['corpus'] = label.find_next().text
        elif label.text == 'Стекло':
            result['glass'] = label.find_next().text
        elif label.text == 'Ремешок':
            result['braslet'] = label.find_next().text
        elif label.text == 'Водонепроницаемость':
            result['water'] = label.find_next().text
        elif label.text == 'Форма корпуса':
            result['form'] = label.find_next().text
        elif label.text == 'Калибр':
            result['caliber'] = label.find_next().text
        elif label.text == 'Циферблат':
            result['colorDial'] = label.find_next().text
        

def fetch_balmainwatches(art:str) -> dict:
    ''' Description: finds the url on the site by article
        Input: article
        Output: desired url
    '''
    product_link = get_product_link(art)
    result = {'vendor': 'Balmain', 'coll': '',
              'seoSuffix': '', 'article': art, 'sex': '', 'mechanism': '', 'diametr': '',
              'thicknes': '', 'corpus': '', 'glass': '', 'braslet': '', 'water': '', 'function': '',
              'dopoform_fake': '', 'dopoform': '', 'form': '', 'caliber': '', 'colorDial': '', 'colorWristlet': '',
              'exit': '', 'price': '', 'youtube': '', 'id': '', 'update': ''}
    req = Request(product_link)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")
    result['coll'] = soup.find('span', attrs={'data-ui-id': 'page-title-wrapper'}).text
    print(result['coll'])
    all_params = soup.find('tbody')
    get_params(all_params, result)
    print(result)
    return result

