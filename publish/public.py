import urllib.parse
import requests
import json
from publish.login import login
from publish.headers import set_publish_headers
import sys
import csv



def get_data() -> list:
    ''' Description: retrieves data from the edited file
        Output: data from the file

    '''
    log.info('Start get edited file')
    all = []
    with open(sys.path[0] + '/fetch/output/output.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            log.debug('Row in file: ' + row)
            all.append(row)
    return all


def encode(data: dict) -> str:
    ''' Description: decodes the Cyrillic alphabet and returns data in the request format
        Input: data from file
        Output: request string

    '''
    result = ''
    log.debug('Start encoding data')
    for key, value in data.items():
        value = urllib.parse.quote(value.encode('cp1251'))
        result = result + key + '=' + value + '&'
        log.debug('Encoding data is ' + result)
    return result[0:-1]


def publish() -> str:
    ''' Description: publishes data on the site
        Output: publish logs

    '''
    cookies = login()
    data = get_data()
    logs = []
    response = ''
    log.info('Start publish')
    for item in data:
        log.debug('Item for publish ' + item)
        item = encode(item)
        logs.append(item)
        URL = 'https://www.haroldltd.ru/cms2/cat/inscore.php'
        headers = set_publish_headers()
        response = requests.post(
            url=URL, data=item, headers=headers, cookies=cookies)
        log.debug('Response from server ' + str(response.text))
        logs.append(str(response.text))
    for log in logs:
        response += log + ' '
    return response
