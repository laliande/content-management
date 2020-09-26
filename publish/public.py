import urllib.parse
import requests
import json
from publish.login import login
from publish.headers import set_publish_headers
import sys
import csv


def get_data(fetch_site):
    all = []
    with open(sys.path[0] + '/fetch/output/output_{}.csv'.format(fetch_site), 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            all.append(row)
    return all


def encode(data):
    result = ''
    for key, value in data.items():
        value = urllib.parse.quote(value.encode('cp1251'))
        result = result + key + '=' + value + '&'
    return result[0:-1]


def publish(fetch_site):
    cookies = login()
    data = get_data(fetch_site)
    logs = []
    response = ''
    for item in data:
        item = encode(item)
        logs.append(item)
        URL = 'https://www.haroldltd.ru/cms2/cat/inscore.php'
        headers = set_publish_headers()
        response = requests.post(
            url=URL, data=item, headers=headers, cookies=cookies)
        logs.append(response.text)
    for log in logs:
        response += log + ' '
    return response
