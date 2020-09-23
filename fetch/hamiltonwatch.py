import csv
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def find_url_hamiltonwatch(art):
    url = 'https://www.hamiltonwatch.com/ru-ru/catalogsearch/result/?q={}'.format(
        art)
    req = Request(url)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")
    product_item_link = soup.find(
        'a', attrs={'class': 'product-item-link'}).attrs['href']
    return product_item_link


def fetch_hamiltonwatch(art):
    result = [art]
    try:
        url = find_url_hamiltonwatch(art)
        req = Request(url)
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "lxml")
        price = soup.body.find(
            'span', attrs={'data-price-type': 'finalPrice'}).attrs['data-price-amount']
        result.append(price)
        caliber = soup.body.find('td', attrs={'data-th': 'Caliber'}).text
        result.append(caliber)
        collection = soup.body.find('td', attrs={
                                    'data-th': 'Коллекция'}).text
        result.append(collection)
        mechanism = soup.body.find('td', attrs={'data-th': 'Механизм'}).text
        result.append(mechanism)
        size = soup.body.find('td', attrs={'data-th': 'Размеры корпуса'}).text
        result.append(size)
        color = soup.body.find('td', attrs={'data-th': 'Цвет циферблата'}).text
        result.append(color)
        material = soup.body.find(
            'td', attrs={'data-th': 'Материал корпуса'}).text
        result.append(material)
        glass = soup.body.find(
            'td', attrs={'data-th': 'Стекло циферблата'}).text
        result.append(glass)
        water = soup.body.find(
            'td', attrs={'data-th': 'Водонепроницаемость'}).text
        result.append(water)
        print(result)
        strap = soup.body.find('td', attrs={'data-th': 'Цвет ремешка'}).text
        print(result)
        result.append(strap)
        return(result)
    except Exception as ex:
        result += ['NULL' for _ in range(11 - len(result))]
    finally:
        return result


def write_hamiltonwatch():
    with open('fetch/input/hamiltonwatch.csv', 'r', encoding='utf-8') as csvinput:
        with open('fetch/output/output_hamiltonwatch.csv', 'a', encoding='utf-8') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)
            for row in reader:
                if row[0] == 'article':
                    headers = ["article", "vendor", "coll", "seoSuffix", "sex", "mechanism", "diametr", "thickness", "corpus",
                               "glass", "braslet", "water", "function", "dopoform_fake", "dopoform", "form",
                               "caliber", "colorDial", "colorWristlet", "exit", "price", "youtube", "id", "update"]
                    writer.writerow(headers)
                else:
                    data = fetch_hamiltonwatch(row[0])
                    writer.writerow(data)
