from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def get_product_link(art:str):
    url = 'https://www.certina.com/ru/search-results?token={}'.format(art)
    req = Request(url)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")
    product_item_link = soup.find('a', attrs={'class': 'hover-image-scale'}).attrs['href']
    return 'https://www.certina.com' + product_item_link

def get_clear_diametr(soup):
    elem = soup.find('div', attrs={'class': 'field field--name-field-watch-diameter-3h-9h field--type-float field--label-above'})
    elem = elem.findChild().find_next().text
    return elem[:-2]

def get_clear_article(bad_article:str):
    result = ''
    for symbol in bad_article:
        if symbol != ' ' and symbol != '\n' and symbol != '\t':
            result += symbol
    return result[8:]
    
def get_mechanism(soup):
    elem = soup.find('div', attrs={'class': 'field field--name-field-watch-movement-types field--type-entity-reference field--label-above'})
    elem  = elem.findChild().find_next().findChild().text
    if elem == 'Автоматические':
        return 'Механический с автоматическим подзаводом'
    elif elem == '':
        return ''
    return elem

def get_clear_thickness(soup):
    elem = soup.find('div', attrs={'class': 'field field--name-field-watch-box-height field--type-float field--label-above'})
    elem = elem.findChild().find_next().text
    return elem[:-2]

def get_clear_glass(soup):
    elem = soup.find('div', attrs={'class': 'field field--name-field-watch-glasses field--type-entity-reference field--label-above'})
    elem = elem.findChild().find_next().text
    if elem[0] == ' ' or elem[0] == '\n' or elem[0] == '\t':
        elem = elem[1:]
    if elem[-1] == ' ' or elem[-1] == '\n' or elem[-1] == '\t':
        elem = elem[:-1]
    return elem

def get_clear_corpus(soup):
    elem = soup.find('div', attrs={'class': 'field field--name-field-watch-case-materials field--type-entity-reference field--label-above'})
    elem = elem.findChild().find_next().text
    if elem[0] == ' ' or elem[0] == '\n' or elem[0] == '\t':
        elem = elem[1:]
    if elem[-1] == ' ' or elem[-1] == '\n' or elem[-1] == '\t':
        elem = elem[:-1]
    if elem[:11] == 'Нержавеющая':
        return 'Нержавеющая сталь'
    return elem

def get_clear_braslet(soup):
    elem = soup.find('div', attrs={'class': 'field field--name-field-watch-bracelet-materials field--type-entity-reference field--label-above'})
    elem = elem.findChild().find_next().text
    if elem[0] == ' ' or elem[0] == '\n' or elem[0] == '\t':
        elem = elem[1:]
    if elem[-1] == ' ' or elem[-1] == '\n' or elem[-1] == '\t':
        elem = elem[:-1]
    if elem[:11] == 'Нержавеющая':
        return 'Нержавеющая сталь'
    return elem

def get_clear_water(soup):
    elem = soup.find('div', attrs={'class': 'field field--name-field-watch-water-resistance field--type-entity-reference field--label-above'})
    elem = elem.findChild().find_next().text
    return elem
    
def get_clear_function(soup):
    elem = soup.find('div', attrs={'class': 'field field--name-field-watch-movement-features field--type-entity-reference field--label-above'})
    elem = elem.findChild().find_next().text
    if elem[0] == ' ' or elem[0] == '\n' or elem[0] == '\t':
        elem = elem[1:]
    if elem[-1] == ' ' or elem[-1] == '\n' or elem[-1] == '\t':
        elem = elem[:-1]
    return elem

def get_clear_caliber(soup):
    elem = soup.find('div', attrs={'class': 'field field--name-field-watch-movement-model field--type-string field--label-above'})
    elem = elem.findChild().find_next().text
    if elem[0] == ' ' or elem[0] == '\n' or elem[0] == '\t':
        elem = elem[1:]
    if elem[-1] == ' ' or elem[-1] == '\n' or elem[-1] == '\t':
        elem = elem[:-1]
    return elem

def get_clear_colorDial(soup):
    elem = soup.find('div', attrs={'class': 'field field--name-field-watch-dial-colors field--type-entity-reference field--label-above'})
    elem = elem.findChild().find_next().text
    if elem[0] == ' ' or elem[0] == '\n' or elem[0] == '\t':
        elem = elem[1:]
    if elem[-1] == ' ' or elem[-1] == '\n' or elem[-1] == '\t':
        elem = elem[:-1]
    return elem

def get_clear_price(soup):
    elem = soup.find('div', attrs={'class': 'field field--name-field-watch-prices field--type-certina-price field--label-hidden field--items'})
    elem = elem.findChild().text
    result = ''
    for i in elem:
        try:
            int(i)
            result += i
        except:
            pass
    return result

def fetch_certina(art:str):
    result = {'vendor': 'Certina', 'coll': '',
              'seoSuffix': '', 'article': '', 'sex': '', 'mechanism': '', 'diametr': '',
              'thickness': '', 'corpus': '', 'glass': '', 'braslet': '', 'water': '', 'function': '',
              'dopoform_fake': '', 'dopoform': '', 'form': '', 'caliber': '', 'colorDial': '', 'colorWristlet': '',
              'exit': '', 'price': '', 'youtube': '', 'id': '', 'update': ''}
    try:
        url = get_product_link(art)
        req = Request(url)
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "lxml")
        result['coll'] = soup.find('div', attrs={'class': 'field field--name-field-watch-subfamily field--type-entity-reference field--label-hidden field--item'}).text
        print(result['coll'])
        result['seoSuffix'] = soup.find('div', attrs={'class': 'field field--name-field-watch-label-suffix field--type-string field--label-hidden field--item'}).text
        print(result['seoSuffix'])
        result['article'] = get_clear_article(soup.find('div', attrs={'class': 'watch-reference'}).text)
        print(result['article'])
        result['mechanism'] = get_mechanism(soup)
        print(result['mechanism'])
        result['diametr'] = get_clear_diametr(soup)
        print(result['diametr'])
        result['thickness'] = get_clear_thickness(soup)
        print(result['thickness'])
        result['corpus'] = get_clear_corpus(soup)
        print(result['corpus'])
        result['glass'] = get_clear_glass(soup)
        print(result['glass'])
        result['braslet'] = get_clear_braslet(soup)
        print(result['braslet'])
        result['water'] = get_clear_water(soup)
        print(result['water'])
        result['function'] = get_clear_function(soup)
        print(result['function'])
        result['dopoform'] = soup.find('div', attrs={'class': 'col-md-8 offset-md-2'}).text
        if result['dopoform'][0] == ' ' or result['dopoform'][0] == '\n' or result['dopoform'][0] == '\t':
            result['dopoform'] = result['dopoform'][1:]
        if result['dopoform'][-1] == ' ' or result['dopoform'][-1] == '\n' or result['dopoform'][-1] == '\t':
            result['dopoform'] = result['dopoform']
        print(result['dopoform'])
        result['caliber'] = get_clear_caliber(soup)
        print(result['caliber'])
        result['colorDial'] = get_clear_colorDial(soup)
        print(result['colorDial'])
        result['price'] = get_clear_price(soup)
        print(result['price'])
    except Exception as ex:
        print(ex)

