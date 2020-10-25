from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def find_url_longines(art: str) -> str:
    ''' Description: finds the url on the site by article
        Input: article
        Output: desired url

    '''
    url = 'https://www.longines.com/ru/search/{}'.format(art)
    req = Request(url)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")

    product_item_link = soup.find(
        'div', attrs={'class': 'novelty-label'}).find_next_siblings()[0].attrs['href']
    return 'https://www.longines.com/' + product_item_link


def find_param(bad_caliber: str, start: int, end: int) -> str:
    ''' Description: clears the string of unnecessary characters
        Input: bad string, index first good word, index end good word
        Output: good string

    '''
    list_words = bad_caliber.split()
    result = ''
    for elem in list_words[start:end]:
        result += elem + ' '
    return result[:-1]


def find_coll(bad_coll: str) -> str:
    ''' Description: clears the string of empty characters
        Input: bad string
        Output: good string

    '''
    result = ''
    for symbol in bad_coll:
        if symbol != ' ' and symbol != '\n' and symbol != '\t':
            result += symbol
    return result


def fetch_longines(art: str) -> dict:
    ''' Description: parses data and returns it in the format of the publication
        Input: article
        Output: product details

    '''
    result = {'vendor': '', 'coll': '',
              'seoSuffix': '', 'article': '', 'sex': '', 'mechanism': '', 'diametr': '',
              'thicknes': '', 'corpus': '', 'glass': '', 'braslet': '', 'water': '', 'function': '',
              'dopoform_fake': '', 'dopoform': '', 'form': '', 'caliber': '', 'colorDial': '', 'colorWristlet': '',
              'exit': '', 'price': '', 'youtube': '', 'id': '', 'update': ''}

    url = find_url_longines(art)
    req = Request(url)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")

    for key, value in result.items():
        try:
            if key == 'vendor':
                result['vendor'] = 'Longines'
            elif key == 'article':
                result['article'] = soup.body.find(
                    'div', attrs={'class': 'watch-ref'}).text
            elif key == 'caliber':
                result['caliber'] = find_param(soup.body.find(
                    'li', attrs={'data-pimkey': 'mvt_fct_calibre_name'}).text, 2, 3)
            elif key == 'coll':
                result['coll'] = find_coll(soup.body.find(
                    'h2', attrs={'class': 'title'}).text)
            elif key == 'mechanism':
                result['mechanism'] = find_param(soup.body.find(
                    'li', attrs={'data-pimkeyparent': 'mvt_fct'}).text, 3, 4)
            elif key == 'colorDial':
                result['colorDial'] = find_param(soup.body.find(
                    'li', attrs={'data-pimkey': 'dial_color'}).text, 2, 3)
            elif key == 'corpus':
                result['corpus'] = find_param(soup.body.find(
                    'li', attrs={'data-pimkey': 'case_material'}).text, 2, 4)
            elif key == 'glass':
                result['glass'] = find_param(soup.body.find(
                    'li', attrs={'data-pimkey': 'case_glass'}).text, 2, 12)
            elif key == 'water':
                result['water'] = find_param(soup.body.find(
                    'li', attrs={'data-pimkey': 'case_water_resistance'}).text, 2, 6)
            elif key == 'colorWristlet':
                result['colorWristlet'] = find_param(soup.body.find(
                    'li', attrs={'data-pimkey': 'bracelet_color'}).text, 2, 3)
            # elif key == 'thicknes':
            #     result['thicknes'] = soup.body.find(
            #         'h4', text='Толщина').find_next_siblings()[0].text
            elif key == 'braslet':
                result['braslet'] = find_param(soup.body.find(
                    'li', attrs={'data-pimkey': 'bracelet_buckle'}).text, 2, 9)
            elif key == 'form':
                result['form'] = find_param(soup.body.find(
                    'li', attrs={'data-pimkey': 'case_shape'}).text, 3, 4)
            elif key == 'diametr':
                result['diametr'] = find_param(soup.body.find(
                    'li', attrs={'data-pimkey': 'case_dimension'}).text, 3, 5)
            # elif key == 'seoSuffix':
            #     result['seoSuffix'] = soup.body.find(
            #         'div', attrs={'class': 'reserve-product'}).text
        except Exception as ex:
            print(ex)
            continue
    return result
