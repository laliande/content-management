from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests



def clear_price(bad_price: str) -> str:
    ''' Description: clears the string of unfit symbols
        Input: bad string
        Output: good string

    '''
    result = ''
    for symbol in bad_price:
        try:
            int(symbol)
            result += symbol
        except:
            if symbol == ',' or symbol == '.':
                break
    return result

def remove_backspaces(bad_str: str) -> str:
    ''' Description: remove backspaces in string
        Input: bad string
        Output: good string
    '''
    result = ''
    for symbol in bad_str:
        if symbol != ' ' and symbol != '\n' and symbol != '\t':
            result += symbol
    return result


def find_url_longines(art: str) -> str:
    ''' Description: finds the url on the site by article
        Input: article
        Output: desired url

    '''
    url = 'https://www.longines.com/ru/search/?q={}'.format(art)
    print(url)
    req = Request(url)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")

    product_item_link = soup.find(
        'p', attrs={'class': 'product-list-item-name'}).findChild().attrs['href']
    print(product_item_link)
    return product_item_link

def get_params(soup: BeautifulSoup, result: dict):
    ''' Description: find params about product
        Input: html, all params
        Output: None

    '''
    flag_color_first = True
    titles = soup.body.find_all('dt', attrs = {'class': 'label'})
    for title in titles:
        try:
            if title.findChild().text == 'Калибр ':
                result['caliber'] = title.find_next('dd').text
            elif title.findChild().text == 'Тип механизма ':
            result['mechanism'] = title.find_next('dd').text
            elif title.findChild().text == 'Цвет ' and flag_color_first:
                flag_color_first = False
                result['colorDial'] = title.find_next('dd').text
            elif title.findChild().text == 'Стекло ':
                result['glass'] = title.find_next('dd').text
            elif title.findChild().text == 'Водонепроницаемость ':
                result['water'] = title.find_next('dd').text
            elif title.findChild().text == 'Материал:' and flag_material_first:
                result['corpus'] = title.find_next('dd').text
            elif title.findChild().text == 'Цвет ' and flag_color_first == False:
                result['colorWristlet'] = title.find_next('dd').text
            elif title.findChild().text == 'Материал ':
                result['braslet'] = title.find_next('dd').text
            elif title.findChild().text == 'Форма корпуса ':
                result['form'] = title.find_next('dd').text
            elif title.findChild().text == 'Функции ':
                result['function'] = title.find_next('dd').text
            elif title.findChild().text == 'Размеры ':
                result['diametr'] = title.find_next('dd').text
        except Exception as ex:
            print(ex)
        

def fetch_longines(art: str) -> dict:
    ''' Description: parses data and returns it in the format of the publication
        Input: article
        Output: product details

    '''
    result = {'vendor': '', 'price': '', 'article': '', 'coll': '',
              'seoSuffix': '', 'sex': '', 'mechanism': '', 'diametr': '',
              'thicknes': '', 'corpus': '', 'glass': '', 'braslet': '', 'water': '', 'function': '',
              'dopoform_fake': '', 'dopoform': '', 'form': '', 'caliber': '', 'colorDial': '', 'colorWristlet': '',
              'exit': '', 'youtube': '', 'id': '', 'update': ''}
    url = find_url_longines(art)
    try:
        url = find_url_longines(art)
        req = Request(url)
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "lxml")
    except Exception as ex:
        print(ex)

    for key, value in result.items():
        try:
            if key == 'vendor':
                result['vendor'] = 'Longines'
            elif key == 'price':
                result['price'] = clear_price(soup.body.find(
                    'span', attrs={'class': 'price'}).text)
                print(result['price'])
            elif key == 'article':
                result['article'] = remove_backspaces(soup.body.find(
                    'span', attrs={'class': 'lg-product__title-sku'}).text)
                print(result['article'])
            elif key == 'coll':
                result['coll'] =  soup.body.find(
                    'h1', attrs={'class': 'lg-product__title'}).findChild().text
            else:
                get_params(soup, result)
                break
        except Exception as ex:
            print(ex)
            continue
    return result

